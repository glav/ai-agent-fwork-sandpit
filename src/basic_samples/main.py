from dotenv import load_dotenv
import os
from load_env import load_env
import asyncio
from agent_framework import ChatAgent, HostedCodeInterpreterTool
from agent_framework.azure import AzureAIAgentClient, AzureOpenAIResponsesClient
from azure.identity.aio import AzureCliCredential

async def main():
    # Load environment variables from .env files
    load_env()

    print("\n.... Generating a joke via ChatAgent ......")
    async with (
        AzureCliCredential() as credential,
        ChatAgent(
            chat_client=AzureAIAgentClient(async_credential=credential),
            instructions="You are good at telling jokes."
        ) as agent,
    ):
        result = await agent.run("Tell me a joke about a pirate.")
        print(result.text)


    print("\n.... Using code interpreter via ChatAgent ......")
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

    print("\n.... Using AzureOpenAIResponsesClient ......")
    agent = AzureOpenAIResponsesClient(credential=AzureCliCredential()).create_agent(
        instructions="You are good at telling jokes.",
        name="Joker"
    )

    result = await agent.run("Tell me a joke about a pirate.")
    print(result.text)

if __name__ == "__main__":
    asyncio.run(main())
