from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import asyncio


load_dotenv()

llm = ChatOpenAI(model="gpt-4.1")

async def main():
    print("Hello from mcp-test!")


if __name__ == "__main__":
    asyncio.run(main())