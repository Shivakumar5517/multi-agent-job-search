import os
import requests

def fetch_jobs(keyword="data analyst", location="Remote"):
    headers = {
        "User-Agent": os.getenv("USAJOBS_USER_AGENT"),
        "Authorization-Key": os.getenv("USAJOBS_API_KEY")
    }
    params = {
        "Keyword": keyword,
        "LocationName": location,
        "ResultsPerPage": 10
    }
    url = "https://data.usajobs.gov/api/search"
    response = requests.get(url, headers=headers, params=params)
    return response.json()