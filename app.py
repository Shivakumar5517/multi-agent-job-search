import streamlit as st
from main import crew
from utils.usajobs_api import fetch_jobs
from utils.logger import log_application

st.title("🧠 AI-Powered Job Application Assistant")

keyword = st.text_input("Job Keyword", "data analyst")
location = st.text_input("Location", "Remote")

jobs = fetch_jobs(keyword, location)
job_titles = [job["MatchedObjectDescriptor"]["PositionTitle"] for job in jobs["SearchResult"]["SearchResultItems"]]

selected_job = st.selectbox("Choose a job", job_titles)

selected_description = next(
    job["MatchedObjectDescriptor"]["UserArea"]["Details"]["MajorDuties"]
    for job in jobs["SearchResult"]["SearchResultItems"]
    if job["MatchedObjectDescriptor"]["PositionTitle"] == selected_job
)

user_profile = st.text_area("Paste Your Background Info")

if st.button("Generate Application Package"):
    result = crew.run({"job_description": selected_description, "user_profile": user_profile})
    log_application(selected_job, result)
    st.text_area("Output", value=result, height=400)