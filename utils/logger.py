import json
from datetime import datetime

def log_application(job_title, result):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "job_title": job_title,
        "output": result
    }
    with open("application_logs.json", "a") as f:
        f.write(json.dumps(log_entry) + "\n")