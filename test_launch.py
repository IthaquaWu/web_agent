import asyncio
from browser_use import Agent
from browser_use.llm import ChatAnthropic

# import os
# print(os.getenv('ANTHROPIC_API_KEY'))

async def main():
     agent = Agent(
         #task="Compare the price of gpt-4o and DeepSeek-V3",
        task="tell me the weather in Beijing",
        llm=ChatAnthropic(model="claude-sonnet-4-20250514", temperature=1.0),
    )
     await agent.run()

asyncio.run(main())