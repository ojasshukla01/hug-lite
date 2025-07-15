import json
import os

def read_jobs(filepath="data/submitted_jobs.ndjson"):
    jobs = []
    with open(filepath, "r") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                jobs.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"⚠️ Skipping invalid line {i+1}: {e}")
    return jobs


def write_jobs(jobs, filepath="data/submitted_jobs.ndjson"):
    with open(filepath, "w") as f:
        for job in jobs:
            f.write(json.dumps(job) + "\n")

def delete_job(index, filepath="data/submitted_jobs.ndjson"):
    jobs = read_jobs(filepath)
    if 0 <= index < len(jobs):
        jobs.pop(index)
        write_jobs(jobs, filepath)

def update_job_status(index, new_status, filepath="data/submitted_jobs.ndjson"):
    jobs = read_jobs(filepath)
    if 0 <= index < len(jobs):
        jobs[index]["status"] = new_status
        write_jobs(jobs, filepath)
