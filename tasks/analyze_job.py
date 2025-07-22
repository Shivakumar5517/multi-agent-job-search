from crewai import Task
from agents.job_analyzer import job_description_agent

analyze_task = Task(
    description="Analyze the following job description and summarize the requirements: {job_description}",
    agent=job_description_agent,
    expected_output="Bullet points of qualifications and responsibilities."
)