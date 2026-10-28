"""
Demonstration script showing timing functionality for workflow processes
"""

import time
from workflow_utils import WorkflowManager, TimingTracker

def simulate_workflow_execution():
    """Simulate a workflow execution with timing"""
    
    # Initialize timing tracker
    timer = TimingTracker()
    timer.start_total_timing()
    
    # Load workflow
    timer.start_step_timing("Load Workflow")
    wm = WorkflowManager()
    time.sleep(0.1)  # Simulate loading time
    timer.end_step_timing("Load Workflow")
    
    # Get workflow steps
    steps = wm.get_workflow_steps()
    
    print(f"\n🎯 Simulating execution of {len(steps)} workflow steps...")
    print("=" * 50)
    
    # Simulate each step execution
    for step in steps:
        step_name = f"Step {step['step_number']}: {step['name']}"
        timer.start_step_timing(step_name)
        
        # Simulate different execution times based on operation type
        operation = step.get('operation', '')
        if operation == 'go_to_url':
            time.sleep(0.5)  # URL navigation takes longer
        elif operation == 'click_element_by_index':
            time.sleep(0.2)  # Click operations are quick
        elif operation == 'input_text':
            time.sleep(0.3)  # Input operations take moderate time
        else:
            time.sleep(0.1)  # Default time
        
        timer.end_step_timing(step_name)
    
    # Print final timing summary
    timer.print_timing_summary()

def demonstrate_timing_features():
    """Demonstrate all timing features"""
    print("🚀 Starting Timing Demonstration")
    print("=" * 60)
    
    # Show workflow information first
    wm = WorkflowManager()
    print("📋 Workflow Information:")
    print(wm.get_workflow_summary())
    
    # Run simulated workflow
    simulate_workflow_execution()
    
    print("\n✅ Timing demonstration completed!")

if __name__ == "__main__":
    demonstrate_timing_features()
