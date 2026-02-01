from pydantic import BaseModel
from typing import List

class Assessment(BaseModel):
    assessment_id: str
    assessment_name: str
    skills: List[str]
    job_level: str
    industry: str
    test_type: str
    duration_minutes: int
