import requests

def fetch_jobs(keyword="data analyst", location="Remote"):
    query = f"{keyword} {location}"
    url = f"https://remotive.io/api/remote-jobs?search={query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["jobs"]
    else:
        return []
