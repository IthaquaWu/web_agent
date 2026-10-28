#!/usr/bin/env python3
"""
Test script to demonstrate workflow.json reading functionality
"""

from workflow_utils import WorkflowManager

def main():
    print("=== Testing Workflow JSON Reading ===\n")
    
    # Initialize WorkflowManager
    wm = WorkflowManager()
    
    if wm.workflow_data is None:
        print("❌ Failed to load workflow data")
        return
    
    print("✅ Workflow loaded successfully!\n")
    
    # Display workflow summary
    print("📋 Workflow Summary:")
    print(wm.get_workflow_summary())
    
    # Show all steps
    steps = wm.get_workflow_steps()
    print(f"\n📝 All Steps ({len(steps)} total):")
    for step in steps:
        print(f"  {step['step_number']}. {step['name']} ({step['operation']})")
    
    # Show click operations
    click_steps = wm.get_steps_by_operation("click_element_by_index")
    print(f"\n🖱️  Click Operations ({len(click_steps)} total):")
    for step in click_steps:
        params = step.get('parameters', {})
        element_info = step.get('element_info', {})
        print(f"  Step {step['step_number']}: {step['name']}")
        print(f"    - Index: {params.get('index', 'N/A')}")
        print(f"    - XPath: {element_info.get('xpath', 'N/A')}")
    
    # Show input operations
    input_steps = wm.get_steps_by_operation("input_text")
    print(f"\n⌨️  Input Operations ({len(input_steps)} total):")
    for step in input_steps:
        params = step.get('parameters', {})
        element_info = step.get('element_info', {})
        print(f"  Step {step['step_number']}: {step['name']}")
        print(f"    - Text: '{params.get('text', 'N/A')}'")
        print(f"    - Index: {params.get('index', 'N/A')}")
        print(f"    - XPath: {element_info.get('xpath', 'N/A')}")
    
    # Show URL navigation
    url_steps = wm.get_steps_by_operation("go_to_url")
    print(f"\n🌐 URL Navigation ({len(url_steps)} total):")
    for step in url_steps:
        params = step.get('parameters', {})
        print(f"  Step {step['step_number']}: {step['name']}")
        print(f"    - URL: {params.get('url', 'N/A')}")
    
    # Test finding specific step
    print(f"\n🔍 Finding Step 2 (Compose Button):")
    compose_step = wm.get_step_by_number(2)
    if compose_step:
        print(f"  ✅ Found: {compose_step['name']}")
        print(f"  - Operation: {compose_step['operation']}")
        print(f"  - Index: {compose_step.get('parameters', {}).get('index', 'N/A')}")
        print(f"  - XPath: {compose_step.get('element_info', {}).get('xpath', 'N/A')}")
    else:
        print("  ❌ Step 2 not found")
    
    # Show agent-formatted output
    print(f"\n🤖 Agent-Formatted Workflow:")
    print("=" * 50)
    agent_format = wm.export_workflow_for_agent()
    print(agent_format)
    
    print("\n✅ Test completed successfully!")

if __name__ == "__main__":
    main()
