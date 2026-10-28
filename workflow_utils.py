import json
import os
import time
from datetime import datetime
from typing import Dict, List, Optional

class TimingTracker:
    """Class to track timing for workflow steps"""
    
    def __init__(self):
        self.step_times = {}
        self.start_times = {}
        self.total_start_time = None
    
    def start_total_timing(self):
        """Start timing the entire workflow"""
        self.total_start_time = time.time()
        print(f"⏱️  Starting total workflow timing at {datetime.now().strftime('%H:%M:%S')}")
    
    def start_step_timing(self, step_name: str):
        """Start timing a specific step"""
        self.start_times[step_name] = time.time()
        print(f"⏱️  Starting step: {step_name} at {datetime.now().strftime('%H:%M:%S')}")
    
    def end_step_timing(self, step_name: str):
        """End timing a specific step"""
        if step_name in self.start_times:
            duration = time.time() - self.start_times[step_name]
            self.step_times[step_name] = duration
            print(f"✅ Completed step: {step_name} in {duration:.3f} seconds")
            return duration
        return 0
    
    def get_total_time(self) -> float:
        """Get total elapsed time"""
        if self.total_start_time:
            return time.time() - self.total_start_time
        return 0
    
    def print_timing_summary(self):
        """Print a summary of all timing data"""
        print("\n" + "=" * 60)
        print("⏱️  DETAILED TIMING SUMMARY")
        print("=" * 60)
        
        total_time = self.get_total_time()
        
        if self.step_times:
            print("📊 Individual Step Times:")
            for step_name, duration in self.step_times.items():
                percentage = (duration / total_time * 100) if total_time > 0 else 0
                print(f"  • {step_name}: {duration:.3f}s ({percentage:.1f}%)")
            
            print(f"\n📈 Step Statistics:")
            step_durations = list(self.step_times.values())
            print(f"  • Fastest step: {min(step_durations):.3f}s")
            print(f"  • Slowest step: {max(step_durations):.3f}s")
            print(f"  • Average step time: {sum(step_durations)/len(step_durations):.3f}s")
            print(f"  • Total steps: {len(step_durations)}")
        
        print(f"\n🎯 Total Workflow Time: {total_time:.3f} seconds ({total_time/60:.2f} minutes)")
        print("=" * 60)

class WorkflowManager:
    """Utility class for managing workflow data"""
    
    def __init__(self, workflow_path: str = "workflow.json"):
        self.workflow_path = workflow_path
        self.workflow_data = None
        self.load_workflow()
    
    def load_workflow(self) -> Optional[Dict]:
        """Load workflow from JSON file"""
        if os.path.exists(self.workflow_path):
            try:
                with open(self.workflow_path, 'r', encoding='utf-8') as f:
                    self.workflow_data = json.load(f)
                print(f"Workflow loaded successfully from {self.workflow_path}")
                return self.workflow_data
            except Exception as e:
                print(f"Error loading {self.workflow_path}: {e}")
                return None
        else:
            print(f"{self.workflow_path} not found")
            return None
    
    def get_workflow_steps(self) -> List[Dict]:
        """Get all workflow steps"""
        if self.workflow_data:
            return self.workflow_data.get('workflow', {}).get('steps', [])
        return []
    
    def get_step_by_number(self, step_number: int) -> Optional[Dict]:
        """Get a specific step by its number"""
        steps = self.get_workflow_steps()
        for step in steps:
            if step.get('step_number') == step_number:
                return step
        return None
    
    def get_steps_by_operation(self, operation: str) -> List[Dict]:
        """Get all steps with a specific operation type"""
        steps = self.get_workflow_steps()
        return [step for step in steps if step.get('operation') == operation]
    
    def get_workflow_summary(self) -> str:
        """Get a summary of the workflow"""
        if not self.workflow_data:
            return "No workflow data available"
        
        workflow = self.workflow_data.get('workflow', {})
        steps = workflow.get('steps', [])
        
        summary = f"""
Workflow Summary:
- Name: {workflow.get('name', 'Unknown')}
- Description: {workflow.get('description', 'No description')}
- Total Steps: {len(steps)}
- Operations Used: {list(set(step.get('operation') for step in steps))}
"""
        return summary
    
    def find_similar_steps(self, target_operation: str, target_description: str = "") -> List[Dict]:
        """Find steps with similar operations or descriptions"""
        steps = self.get_workflow_steps()
        similar_steps = []
        
        for step in steps:
            if step.get('operation') == target_operation:
                similar_steps.append(step)
            elif target_description and target_description.lower() in step.get('name', '').lower():
                similar_steps.append(step)
        
        return similar_steps
    
    def export_workflow_for_agent(self) -> str:
        """Export workflow in a format suitable for agent instructions"""
        if not self.workflow_data:
            return "No workflow data available."
        
        workflow = self.workflow_data.get('workflow', {})
        steps = workflow.get('steps', [])
        
        formatted_workflow = f"""
Available Workflow: {workflow.get('name', 'Unknown')}
Description: {workflow.get('description', 'No description')}

Reference Steps:
"""
        
        for step in steps:
            element_info = step.get('element_info', {})
            parameters = step.get('parameters', {})
            
            formatted_workflow += f"""
Step {step['step_number']}: {step['name']}
- Operation: {step['operation']}
- Parameters: {parameters}
- Element: {element_info.get('description', 'N/A')}
- XPath: {element_info.get('xpath', 'N/A')}
- Expected Result: {step.get('result', 'N/A')}
"""
        
        return formatted_workflow

# Example usage functions
def demonstrate_workflow_usage():
    """Demonstrate how to use the workflow data"""
    print("=== Workflow Manager Demo ===")
    
    # Initialize workflow manager
    wm = WorkflowManager()
    
    # Print workflow summary
    print(wm.get_workflow_summary())
    
    # Get all click operations
    click_steps = wm.get_steps_by_operation("click_element_by_index")
    print(f"\nFound {len(click_steps)} click operations:")
    for step in click_steps:
        print(f"- Step {step['step_number']}: {step['name']}")
    
    # Get all input operations
    input_steps = wm.get_steps_by_operation("input_text")
    print(f"\nFound {len(input_steps)} input operations:")
    for step in input_steps:
        params = step.get('parameters', {})
        print(f"- Step {step['step_number']}: {step['name']} - Text: '{params.get('text', 'N/A')}'")
    
    # Find a specific step
    compose_step = wm.get_step_by_number(2)
    if compose_step:
        print(f"\nCompose button step details:")
        print(f"- XPath: {compose_step.get('element_info', {}).get('xpath', 'N/A')}")
        print(f"- Index: {compose_step.get('parameters', {}).get('index', 'N/A')}")

if __name__ == "__main__":
    demonstrate_workflow_usage()
