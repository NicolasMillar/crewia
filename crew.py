import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_KEY"] = ""
os.environ['OPENAI_MODEL_NAME'] = 'gpt-3.5-turbo'

"""
como poner las credenciales para claude
Claude_3 = os.environ["ANTHROPIC_API_KEY"] = "aca va la apy key"
LLM = ChatAnthropic(temperature=0,model_name="claude-3-opus-2024229")
instalar langchain_anthropic

from langchain_anthropic import ChatAnthropic
"""

developer = Agent(
    role='developer',
    goal='consistently produce clean, functional, and readable code that not only meets the requirements of the project but also contributes to its maintainability and scalability. By adhering to best practices and continuously improving my coding skills, I aim to deliver software solutions that are efficient, reliable, and easy to understand for myself and fellow developers',
    backstory='You are an AI specialist in software development, specializing in python',
    verbose=True,
    allow_delegation=False
)

developer = Agent(
    role='developer',
    goal='consistently produce clean, functional, and readable code that not only meets the requirements of the project but also contributes to its maintainability and scalability. By adhering to best practices and continuously improving my coding skills, I aim to deliver software solutions that are efficient, reliable, and easy to understand for myself and fellow developers',
    backstory='You are an AI specialist in software development, specializing in python',
    verbose=True,
    allow_delegation=False
)

reviewer = Agent(
    role='reviewer',
    goal='consistently produce clean, functional, and readable code that not only meets the requirements of the project but also contributes to its maintainability and scalability. By adhering to best practices and continuously improving my coding skills, I aim to deliver software solutions that are efficient, reliable, and easy to understand for myself and fellow developers',
    backstory='You are an AI specialist in reviewing software development, specializing in python',
    verbose=True,
    allow_delegation=False
)

optimizer = Agent(
    role='optimizer',
    goal='consistently produce clean, functional, and readable code that not only meets the requirements of the project but also contributes to its maintainability and scalability. By adhering to best practices and continuously improving my coding skills, I aim to deliver software solutions that are efficient, reliable, and easy to understand for myself and fellow developers',
    backstory='You are an AI specialist in optimizing software development, specializing in python',
    verbose=True,
    allow_delegation=False
)

task1 = Task(description='Implement a sorting algorithm', expected_output='', agent=developer)
task2 = Task(description='Review and correct code from developer', expected_output='', agent=reviewer)
task3 = Task(description='Optimize code from reviewer', expected_output='', agent=optimizer)

crew = Crew(
    agents=[developer, reviewer, optimizer],
    tasks=[task1, task2, task3],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()