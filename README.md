# SmarterAIAgent

An intelligent automation agent for email sending and workflow management using Python and Playwright.

## Features

- Automated email sending through 163.com mail service
- Workflow management and execution tracking
- Time measurement and performance reporting
- Browser automation capabilities
- Integration with Anthropic's Claude AI model

## File Structure

```
SmarterAIAgent/
├── .env - Environment variables
├── agent.py - Main agent implementation
├── click_functions.py - Browser interaction functions
├── KnowledgeBase/ - Knowledge base files
├── send_mail_agent.py - Email sending functionality
├── test_baidu_search.py - Test for Baidu search
├── test_close_playwright.py - Playwright test
├── test_launch.py - Launch test
├── timing_demo.py - Timing demonstration
├── workflow_test.py - Workflow testing
├── workflow_utils.py - Workflow management utilities
```

## Setup

1. Clone the repository
2. Install dependencies:
```shell
pip install -r requirements.txt
```

3. Create a `.env` file with your credentials:
```
MAIL_NAME=your_163_email@163.com
MAIL_PASSWORD=your_password
```

4. Run the agent:
```shell
python agent.py
```

## Usage

The agent can be configured to:
- Send emails through 163.com
- Record and manage workflows
- Track execution times
- Handle browser automation tasks

Example workflow:
1. Log in to 163.com mail
2. Compose an email
3. Send the email
4. Close the browser
5. Save the workflow for future use

## Configuration

Edit `agent.py` to:
- Change target email addresses
- Modify email content
- Adjust timing settings
- Configure workflow parameters

## Dependencies

- Python 3.7+
- Playwright
- python-dotenv
- Anthropic SDK

## License

MIT License

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
