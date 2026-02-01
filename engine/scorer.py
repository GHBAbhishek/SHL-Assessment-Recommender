from config import WEIGHTS

def normalize(value, max_value):
    return min(value / max_value, 1.0)

def score_assessment(skill_score, role_match, industry_match, type_match, duration_fit):
    return (
        WEIGHTS["skill_match"] * skill_score +
        WEIGHTS["role_level"] * role_match +
        WEIGHTS["industry"] * industry_match +
        WEIGHTS["assessment_type"] * type_match +
        WEIGHTS["duration"] * duration_fit
    )
