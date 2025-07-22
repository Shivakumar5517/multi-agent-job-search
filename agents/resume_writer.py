from crewai import Agent

resume_agent = Agent(
    role="Resume Generator",
    goal="Generate tailored resumes and cover letters based on a job and user's background",
    backstory="Expert in resume writing",
    verbose=True
)