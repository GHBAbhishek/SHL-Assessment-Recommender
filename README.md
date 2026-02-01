# SHL Assessment Recommendation Engine

## Problem Statement
Design an intelligent system that recommends suitable SHL assessments based on job requirements, skills, seniority, and hiring constraints.

## Approach
The solution uses a hybrid recommendation strategy combining:
- Semantic skill similarity using TF-IDF
- Rule-based compatibility checks
- Weighted multi-factor ranking

## Key Features
- Multi-dimensional scoring (skills, role level, industry, duration)
- Explainable recommendations
- Modular & testable architecture
- Streamlit-based interactive UI

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- RapidFuzz
- Pydantic

## How It Works
1. User provides job requirements
2. System encodes skill relevance using NLP
3. Each assessment is scored across multiple dimensions
4. Top-ranked assessments are returned with explanations

## Future Improvements
- Sentence-BERT for deep semantic matching
- Learning-to-rank models
- Real-time feedback loop from recruiters
- API-based deployment

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Live Application
The project is deployed and accessible at: https://shl-skillfit-recommender.streamlit.app/

