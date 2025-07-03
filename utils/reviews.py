import json
import os

def save_review(job_id, rating, review, filepath="data/ratings.json"):
    data = []
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    data.append({
        "job_id": job_id,
        "rating": rating,
        "review": review
    })

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)