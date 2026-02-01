def analyze_resume(text, job):
    text = text.lower()
    job = job.strip().upper()

    JOB_MAP = {
        "ARTIFICIAL INTELLIGENCE & DATA SCIENCE": "AI DATA SCIENCE",
        "ARTIFICIAL INTELLIGENCE & MACHINE LEARNING": "AI ML",
        "BIGDATA": "BIG DATA",
        "WEB DEVELOPMENT": "WEB DEVELOPER",
        "SOFTWARE": "SOFTWARE ENGINEER"
    }

    job = JOB_MAP.get(job, job)

    skills = {
        "AI DATA SCIENCE": ["python", "machine learning", "sql", "statistics"],
        "AI ML": ["machine learning", "deep learning"],
        "WEB DEVELOPER": ["html", "css", "javascript"],
        "SOFTWARE ENGINEER": ["java", "python", "c++"],
        "BIG DATA": ["python", "cloud"]
    }

    required = skills.get(job, [])
    found = [s for s in required if s in text]
    missing = [s for s in required if s not in found]

    score = int((len(found) / len(required)) * 100) if required else 0

    salary = (
        "₹8–12 LPA" if score > 75 else
        "₹5–8 LPA" if score > 50 else
        "₹3–5 LPA"
    )

    return {
        "score": score,
        "found_skills": found,
        "missing_skills": missing,
        "job_role": job,
        "salary": salary,
        "tips": [f"Add {s}" for s in missing]
    }
