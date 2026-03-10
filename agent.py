import os
from google.adk.agents import Agent

root_agent = Agent(
    name="qa_agent",
    model="gemini-2.0-flash-exp",
    description="A question answering agent",
    instruction=(
        "You are a helpful and knowledgeable assistant. "
        "Answer questions clearly, accurately, and concisely. "
        "If you don't know the answer, say so honestly."
    ),
)
