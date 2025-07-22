"""import streamlit as st
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
    st.text_area("Output", value=result, height=400)"""
    
import streamlit as st
from utils.remotive_api import fetch_jobs
from main import run_job_pipeline
from utils.logger import log_application

st.title("🧠 AI-Powered Job Application Assistant (Remotive)")

keyword = st.text_input("Job Keyword", "data analyst")
location = st.text_input("Location", "Remote")
user_profile = st.text_area("Paste Your Background Info")

jobs = fetch_jobs(keyword, location)
if jobs:
    job_titles = [job["title"] for job in jobs]
    selected_job = st.selectbox("Choose a job", job_titles)
    job_obj = next(job for job in jobs if job["title"] == selected_job)
    job_description = job_obj["description"]

    st.markdown("### Job Description")
    st.markdown(job_description, unsafe_allow_html=True)

    if st.button("Generate Application Package"):
        result = run_job_pipeline(job_description, user_profile)
        log_application(selected_job, result)
        st.success("✅ Application Package Generated!")
        st.text_area("📄 Output", value=result, height=400)
else:
    st.warning("No jobs found for that keyword/location.")