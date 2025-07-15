# utils/fix_jobs_file.py

import json

def clean_submitted_jobs(filepath="data/submitted_jobs.ndjson"):
    with open(filepath, "r") as f:
        lines = f.readlines()

    valid_jobs = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            job = json.loads(line)
            valid_jobs.append(job)
        except json.JSONDecodeError:
            print(f"❌ Invalid JSON line skipped: {line}")

    with open(filepath, "w") as f:
        for job in valid_jobs:
            f.write(json.dumps(job) + "\n")

    print(f"✅ Cleaned and rewrote {len(valid_jobs)} valid jobs.")

if __name__ == "__main__":
    clean_submitted_jobs()
