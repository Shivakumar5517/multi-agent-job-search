from crewai import Agent

job_description_agent = Agent(
    role="Job Analyzer",
    goal="Extract required qualifications and responsibilities from job description",
    backstory="Expert at job market trends and HR practices",
    verbose=True
)