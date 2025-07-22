from crewai import Agent

message_agent = Agent(
    role="Networking Assistant",
    goal="Craft personalized messages for LinkedIn or email outreach",
    backstory="Experienced in professional communication",
    verbose=True
)