def generate_reason(row, inputs):
    reasons = []

    matched_skills = set(row["skills"].lower().split(",")) & set(inputs["skills"])
    if matched_skills:
        reasons.append(f"Matches required skills: {', '.join(matched_skills)}")

    if row["job_level"] == inputs["job_level"]:
        reasons.append("Aligned with target job seniority")

    if row["industry"] == inputs["industry"]:
        reasons.append("Relevant to selected industry")

    if row["test_type"] == inputs["test_type"]:
        reasons.append("Assessment type matches hiring need")

    if row["duration_minutes"] <= inputs["max_duration"]:
        reasons.append("Fits within preferred assessment duration")

    return reasons
