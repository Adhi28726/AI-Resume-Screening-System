import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_description = """
Python Developer required.
Skills: Python, SQL, APIs, Flask, Git, Data Structures.
Knowledge of Machine Learning is a plus.
"""

resumes = {
    "Adithya Reddy": """
    Python, SQL, Flask, Git, REST APIs,
    Machine Learning, Data Analysis,
    Problem Solving
    """,

    "Rahul Kumar": """
    Java, Spring Boot, MySQL,
    HTML, CSS, JavaScript
    """,

    "Priya Sharma": """
    Python, Django, SQL,
    GitHub, APIs, Data Structures
    """
}

documents = [job_description] + list(resumes.values())

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

job_vector = tfidf_matrix[0]

scores = []

for i, candidate in enumerate(resumes.keys()):
    similarity = cosine_similarity(job_vector, tfidf_matrix[i + 1])[0][0]
    scores.append((candidate, round(similarity * 100, 2)))

scores.sort(key=lambda x: x[1], reverse=True)

print("\n===== Resume Screening Results =====\n")

for rank, (candidate, score) in enumerate(scores, start=1):
    print(f"{rank}. {candidate}")
    print(f"Match Score: {score}%")
    print("-" * 30)

df = pd.DataFrame(scores, columns=["Candidate", "Match Score"])
df.to_csv("screening_results.csv", index=False)

print("\nResults saved to screening_results.csv")