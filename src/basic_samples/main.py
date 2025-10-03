from dotenv import load_dotenv
import os
from load_env import load_env
import asyncio
from agent_framework import ChatAgent, HostedCodeInterpreterTool
from agent_framework.azure import AzureAIAgentClient
from azure.identity.aio import AzureCliCredential

async def main():
    # Load environment variables from .env files
    load_env()

    print("\n.... Generating a joke ......")
    async with (
        AzureCliCredential() as credential,
        ChatAgent(
            chat_client=AzureAIAgentClient(async_credential=credential),
            instructions="You are good at telling jokes."
        ) as agent,
    ):
        result = await agent.run("Tell me a joke about a pirate.")
        print(result.text)


    print("\n.... Using code interpreter ......")
    async with (
        AzureCliCredential() as credential,
        ChatAgent(
            chat_client=AzureAIAgentClient(async_credential=credential),
            instructions="You are a helpful assistant that can execute Python code.",
            tools=HostedCodeInterpreterTool()
        ) as agent
    ):
        response = await agent.run("Calculate the factorial of 100 using Python")
        print(response.text)

if __name__ == "__main__":
    asyncio.run(main())
