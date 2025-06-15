import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(employee_file, project_file):
    employees = pd.read_csv(employee_file)
    projects = pd.read_csv(project_file)
    return employees, projects

def match_employees_to_project(employees, project, top_n=3):
    vectorizer = TfidfVectorizer()
    employee_skills = employees['skills'].fillna('')
    combined = employee_skills.tolist() + [project['required_skills']]
    tfidf_matrix = vectorizer.fit_transform(combined)
    cosine_sim = cosine_similarity(tfidf_matrix[:-1], tfidf_matrix[-1:])
    employees['match_score'] = cosine_sim.flatten()
    matched = employees.sort_values(by='match_score', ascending=False).head(top_n)
    return matched
