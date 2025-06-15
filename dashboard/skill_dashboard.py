import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
projects = pd.read_csv("data/projects.csv")

# Top In-Demand Skills
all_skills = projects['required_skills'].str.split(';').explode()
top_skills = all_skills.value_counts().reset_index()
top_skills.columns = ['Skill', 'DemandCount']
fig1 = px.bar(top_skills, x='Skill', y='DemandCount', title='Top In-Demand Skills')

# Project Priority Distribution
priority_dist = projects['priority'].value_counts().reset_index()
priority_dist.columns = ['Priority', 'ProjectCount']
fig2 = px.pie(priority_dist, names='Priority', values='ProjectCount', title='Project Priority Distribution')

# Display
st.title("📊 SkillBridge Analytics Dashboard")
st.plotly_chart(fig1)
st.plotly_chart(fig2)
