from crewai import Task
from agents.resume_writer import resume_agent

resume_task = Task(
    description="Generate a tailored resume and cover letter for the job: {job_description} and user profile: {user_profile}",
    agent=resume_agent,
    expected_output="Formatted resume and cover letter"
)