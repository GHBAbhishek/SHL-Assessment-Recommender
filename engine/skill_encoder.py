from rapidfuzz import fuzz
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class SkillEncoder:
    def __init__(self, corpus):
        self.vectorizer = TfidfVectorizer()
        self.matrix = self.vectorizer.fit_transform(corpus)

    def semantic_similarity(self, query, index):
        query_vec = self.vectorizer.transform([query])
        score = (query_vec @ self.matrix[index].T).toarray()[0][0]
        return float(score)

    @staticmethod
    def fuzzy_match(a, b):
        return fuzz.token_set_ratio(a, b)
