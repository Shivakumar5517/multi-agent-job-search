from crewai import Task
from agents.message_agent import message_agent

message_task = Task(
    description="Create a short, friendly LinkedIn message to reach out about the job: {job_description}",
    agent=message_agent,
    expected_output="Message of ~100 words"
)