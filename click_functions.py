#!/usr/bin/env python3
"""
Click functions extracted from workflow.json for Gmail automation
This file contains all the click operation functions defined in the workflow
"""

import json
from typing import Dict, List, Optional

def load_click_functions_from_json(json_path: str = "workflow.json") -> Dict:
    """Load click functions from the workflow JSON file"""
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        click_functions = {}
        steps = data.get('workflow', {}).get('steps', [])
        
        for step in steps:
            if step.get('operation') == 'click_element_by_index' and 'function' in step:
                func_info = step['function']
                click_functions[func_info['name']] = {
                    'step_number': step['step_number'],
                    'step_name': step['name'],
                    'description': func_info['description'],
                    'implementation': func_info['implementation'],
                    'parameters': func_info['parameters'],
                    'return_type': func_info['return_type'],
                    'error_handling': func_info['error_handling'],
                    'xpath': step.get('element_info', {}).get('xpath', 'N/A'),
                    'index': step.get('parameters', {}).get('index', 'N/A')
                }
        
        return click_functions
    except Exception as e:
        print(f"Error loading click functions: {e}")
        return {}

# ============================================================================
# CLICK FUNCTIONS EXTRACTED FROM WORKFLOW.JSON
# ============================================================================

def click_compose_button(browser, index=17):
    """
    Click the Gmail compose button to open email composition interface
    
    Args:
        browser: Browser automation object
        index (int): Element index for the compose button (default: 17)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Method 1: Click by index
        element = browser.find_element_by_index(index)
        element.click()
        return True
    except:
        try:
            # Method 2: Click by XPath as fallback
            xpath = "//div[@role='button'][contains(text(),'写邮件')]"
            element = browser.find_element_by_xpath(xpath)
            element.click()
            return True
        except:
            return False

def select_recipient_from_dropdown(browser, email_address, index=189):
    """
    Select a recipient email from Gmail's dropdown suggestions
    
    Args:
        browser: Browser automation object
        email_address (str): The email address to select
        index (int): Element index for the dropdown option (default: 189)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Method 1: Click by index
        element = browser.find_element_by_index(index)
        element.click()
        return True
    except:
        try:
            # Method 2: Click by XPath with email address
            xpath = f"//div[@role='option'][contains(text(),'{email_address}')]"
            element = browser.find_element_by_xpath(xpath)
            element.click()
            return True
        except:
            try:
                # Method 3: Generic dropdown option selector
                xpath = "//div[@role='option']"
                elements = browser.find_elements_by_xpath(xpath)
                for elem in elements:
                    if email_address in elem.text:
                        elem.click()
                        return True
                return False
            except:
                return False

def click_send_button(browser, index=133):
    """
    Click the Gmail send button to send the composed email
    
    Args:
        browser: Browser automation object
        index (int): Element index for the send button (default: 133)
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Method 1: Click by index
        element = browser.find_element_by_index(index)
        element.click()
        return True
    except:
        try:
            # Method 2: Click by XPath with aria-label
            xpath = "//div[@role='button'][@aria-label='发送']"
            element = browser.find_element_by_xpath(xpath)
            element.click()
            return True
        except:
            try:
                # Method 3: Click by text content
                xpath = "//div[@role='button'][contains(text(),'发送')]"
                element = browser.find_element_by_xpath(xpath)
                element.click()
                return True
            except:
                try:
                    # Method 4: Generic send button selector
                    xpath = "//div[@role='button'][contains(@aria-label,'send') or contains(@aria-label,'Send') or contains(@aria-label,'发送')]"
                    element = browser.find_element_by_xpath(xpath)
                    element.click()
                    return True
                except:
                    return False

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_all_click_functions() -> List[str]:
    """Get list of all available click function names"""
    return ['click_compose_button', 'select_recipient_from_dropdown', 'click_send_button']

def get_function_info(function_name: str) -> Optional[Dict]:
    """Get detailed information about a specific click function"""
    click_functions = load_click_functions_from_json()
    return click_functions.get(function_name)

def print_all_click_functions():
    """Print information about all click functions"""
    click_functions = load_click_functions_from_json()
    
    print("=" * 80)
    print("GMAIL CLICK FUNCTIONS FROM WORKFLOW.JSON")
    print("=" * 80)
    
    for func_name, func_info in click_functions.items():
        print(f"\n📌 Function: {func_name}")
        print(f"   Step: {func_info['step_number']} - {func_info['step_name']}")
        print(f"   Description: {func_info['description']}")
        print(f"   Default Index: {func_info['index']}")
        print(f"   XPath: {func_info['xpath']}")
        print(f"   Return Type: {func_info['return_type']}")
        print(f"   Error Handling: {func_info['error_handling']}")
        print(f"   Parameters: {func_info['parameters']}")
        print("-" * 80)

def execute_click_workflow(browser, target_email: str = "213242352@seu.edu.cn"):
    """
    Execute the complete click workflow for Gmail email sending
    
    Args:
        browser: Browser automation object
        target_email (str): Email address to send to
    
    Returns:
        bool: True if all steps successful, False otherwise
    """
    print("🚀 Starting Gmail Click Workflow...")
    
    # Step 1: Click Compose Button
    print("📝 Step 1: Clicking compose button...")
    if not click_compose_button(browser):
        print("❌ Failed to click compose button")
        return False
    print("✅ Compose button clicked successfully")
    
    # Step 2: Select recipient (after filling recipient field)
    print("👤 Step 2: Selecting recipient from dropdown...")
    if not select_recipient_from_dropdown(browser, target_email):
        print("❌ Failed to select recipient from dropdown")
        return False
    print("✅ Recipient selected successfully")
    
    # Step 3: Send email (after filling subject and body)
    print("📧 Step 3: Clicking send button...")
    if not click_send_button(browser):
        print("❌ Failed to click send button")
        return False
    print("✅ Send button clicked successfully")
    
    print("🎉 Gmail Click Workflow completed successfully!")
    return True

# ============================================================================
# DEMO AND TESTING
# ============================================================================

def demo_click_functions():
    """Demonstrate the click functions (without actual browser)"""
    print("🎯 CLICK FUNCTIONS DEMO")
    print("=" * 50)
    
    # Load and display all click functions
    print_all_click_functions()
    
    # Show function usage examples
    print("\n💡 USAGE EXAMPLES:")
    print("=" * 50)
    
    print("\n# Example 1: Click compose button")
    print("success = click_compose_button(browser)")
    print("if success:")
    print("    print('Compose button clicked!')")
    
    print("\n# Example 2: Select recipient")
    print("email = '213242352@seu.edu.cn'")
    print("success = select_recipient_from_dropdown(browser, email)")
    print("if success:")
    print("    print(f'Selected {email} from dropdown!')")
    
    print("\n# Example 3: Send email")
    print("success = click_send_button(browser)")
    print("if success:")
    print("    print('Email sent successfully!')")
    
    print("\n# Example 4: Execute complete workflow")
    print("success = execute_click_workflow(browser, 'target@example.com')")
    print("if success:")
    print("    print('Complete workflow executed!')")

if __name__ == "__main__":
    demo_click_functions()
