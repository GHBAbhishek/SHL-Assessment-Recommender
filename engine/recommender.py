import pandas as pd
from engine.skill_encoder import SkillEncoder
from engine.scorer import score_assessment

class AssessmentRecommender:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)
        self.df["skills_text"] = self.df["skills"].str.lower()
        self.encoder = SkillEncoder(self.df["skills_text"].tolist())

    def recommend(self, skills, job_level, industry, test_type, max_duration):
        results = []

        query = " ".join(skills).lower()

        for idx, row in self.df.iterrows():
            skill_score = self.encoder.semantic_similarity(query, idx)

            role_match = 1 if row["job_level"] == job_level else 0
            industry_match = 1 if row["industry"] == industry else 0
            type_match = 1 if row["test_type"] == test_type else 0
            duration_fit = 1 if row["duration_minutes"] <= max_duration else 0

            final_score = score_assessment(
                skill_score,
                role_match,
                industry_match,
                type_match,
                duration_fit
            )

            reasons = []
            if role_match:
                reasons.append("Job level match")
            if industry_match:
                reasons.append("Industry match")
            if type_match:
                reasons.append("Test type match")
            if duration_fit:
                reasons.append("Duration fits requirement")

            results.append({
                "assessment_id": row["assessment_id"],
                "name": row["assessment_name"],
                "score": round(final_score, 3),
                "reasons": reasons
            })

        return sorted(results, key=lambda x: x["score"], reverse=True)

