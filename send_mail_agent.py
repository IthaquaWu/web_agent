import asyncio
import json
import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatAnthropic
from workflow_utils import WorkflowManager

mail_name = "wujunhao20267@163.com"
mail_password = "wjh2026720040903"


async def main():
    # Start timing the entire process
    start_time = time.time()
    start_datetime = datetime.now()
    
    print(f"🚀 Starting SmarterAIAgent at {start_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    title = "Hello"
    content = "This is a test email sent by SmarterAIAgent. Please ignore it."
    target_email = "1693259252@qq.com"
    
    # Time workflow loading
    workflow_start = time.time()
    workflow_manager = WorkflowManager()
    workflow_info = workflow_manager.export_workflow_for_agent()
    workflow_load_time = time.time() - workflow_start
    
    # Print workflow summary for debugging
    print("=== Workflow Information ===")
    print(workflow_manager.get_workflow_summary())
    print(f"⏱️  Workflow loaded in {workflow_load_time:.3f} seconds")
    print("=" * 60)
    
    # Create task with workflow information
    task = f"""给 {target_email} 写邮件，主题是{title}，内容是{content},其中邮箱账号和密码分别是{mail_name}和{mail_password}。出现验证码时，用户自己填写验证码。

请参考以下已有的工作流程步骤：
{workflow_info}

执行任务时：
1. 优先参考上述工作流程中的步骤和XPath
2. 如果工作流程中有相应的操作，请使用相同的XPath和参数
3. 在执行每一步后，提取相应的XPath将其与操作类型 (click, type) 及相关参数（如输入的文本）和执行的功能一起，作为一个步骤存入你的工作流（workflow）中
4. 将新的工作流程以"workflow.txt"的形式保存在D:\Main\SmarterAIAgent\workflow.txt

⏰ 请在执行过程中记录每个步骤的时间，并在完成后报告总耗时。"""

    # Time agent execution
    agent_start = time.time()
    print(f"🤖 Starting agent execution at {datetime.now().strftime('%H:%M:%S')}")
    
    agent = Agent(
        task=task,
        llm=ChatAnthropic(model="claude-sonnet-4-20250514", temperature=1.0),
    )
    
    try:
        await agent.run()
        agent_end_time = time.time()
        agent_duration = agent_end_time - agent_start
        
        # Calculate total time
        total_time = time.time() - start_time
        end_datetime = datetime.now()
        
        print("=" * 60)
        print("⏱️  TIMING SUMMARY")
        print("=" * 60)
        print(f"📅 Start Time: {start_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📅 End Time: {end_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"⏱️  Workflow Loading: {workflow_load_time:.3f} seconds")
        print(f"🤖 Agent Execution: {agent_duration:.3f} seconds")
        print(f"🎯 Total Process Time: {total_time:.3f} seconds ({total_time/60:.2f} minutes)")
        print(f"📊 Process Duration: {str(timedelta(seconds=int(total_time)))}")
        print("=" * 60)
        
    except Exception as e:
        error_time = time.time() - start_time
        print("=" * 60)
        print("❌ PROCESS FAILED")
        print("=" * 60)
        print(f"Error: {str(e)}")
        print(f"⏱️  Time before failure: {error_time:.3f} seconds")
        print("=" * 60)
        raise

asyncio.run(main())
