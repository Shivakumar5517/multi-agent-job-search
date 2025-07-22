from crewai import Crew
from tasks.analyze_job import analyze_task
from tasks.resume_task import resume_task
from tasks.message_task import message_task

crew = Crew(
    agents=[analyze_task.agent, resume_task.agent, message_task.agent],
    tasks=[analyze_task, resume_task, message_task]
)

if __name__ == "__main__":
    job_description = "Paste a job description here"
    user_profile = "Paste your background information here"
    result = crew.run({"job_description": job_description, "user_profile": user_profile})
    print(result)