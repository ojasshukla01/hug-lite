import json
import os

def read_jobs(filepath="data/submitted_jobs.json"):
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def write_jobs(jobs, filepath="data/submitted_jobs.json"):
    with open(filepath, "w") as f:
        for job in jobs:
            f.write(json.dumps(job) + "\n")

def delete_job(index, filepath="data/submitted_jobs.json"):
    jobs = read_jobs(filepath)
    if 0 <= index < len(jobs):
        jobs.pop(index)
        write_jobs(jobs, filepath)

def update_job_status(index, new_status, filepath="data/submitted_jobs.json"):
    jobs = read_jobs(filepath)
    if 0 <= index < len(jobs):
        jobs[index]["status"] = new_status
        write_jobs(jobs, filepath)
