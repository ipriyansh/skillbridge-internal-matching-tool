import streamlit as st
import pandas as pd
from matching_engine.matcher import load_data, match_employees_to_project

st.title("🔍 SkillBridge - Internal Project Matcher")

employees, projects = load_data("data/employees.csv", "data/projects.csv")

project_selection = st.selectbox("Select a Project", projects['title'].tolist())
selected_project = projects[projects['title'] == project_selection].iloc[0]

if st.button("Find Matches"):
    matches = match_employees_to_project(employees, selected_project)
    st.subheader("Top Matching Employees:")
    st.dataframe(matches[['emp_id', 'name', 'skills', 'match_score']])
