# SkillBridge – Internal Project & Resource Matching Tool

SkillBridge is a simple internal tool built to help IT service organizations match the right people to the right projects based on their skills and preferences. It’s designed to solve a common issue in services companies: resource underutilization due to poor visibility of skillsets.

---

## 🔍 What It Does

- Lets managers define the skill requirements of upcoming or ongoing projects
- Helps employees discover internal projects aligned with their skills or growth goals
- Matches the two using a lightweight ML-based ranking system (cosine similarity on skill sets)
- Includes dashboards to show skill trends, gaps, and project priority distribution

---

## 🧩 Tech Stack

- **Frontend**: Streamlit
- **Matching Engine**: Python + scikit-learn
- **Backend API (optional)**: Flask
- **Data**: CSV files for employees and projects
- **Analytics**: Plotly (inside Streamlit)

---

## 📁 Folder Structure

```
.
├── backend/
│   └── app.py
├── dashboard/
│   └── skill_dashboard.py
├── data/
│   ├── employees.csv
│   └── projects.csv
├── frontend/
│   └── streamlit_app.py
├── matching_engine/
│   └── matcher.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the main matching app:
   ```bash
   streamlit run frontend/streamlit_app.py
   ```

3. To open the analytics dashboard:
   ```bash
   streamlit run dashboard/skill_dashboard.py
   ```

The app runs on [http://localhost:8501](http://localhost:8501) by default.

---

## 📊 Sample Dashboards

The dashboard includes:
- Top 5 most in-demand skills across all projects
- Project priority breakdown (high, medium, urgent, etc.)
- Interactive charts using Plotly

---

## 🔄 What's Next

- Resume parsing for auto-profile creation
- Integration with LinkedIn Learning or LMS
- Feedback loop from managers for match quality

---

## 👨‍💻 Author

Built by [Priyansh Sourav](https://www.linkedin.com/in/priyansh-sourav/)  
GitHub: [@ipriyansh](https://github.com/ipriyansh)

This project reflects real-world product thinking, team alignment, and backend + data understanding in a clean, demo-ready format.

---

## 📄 License

MIT – feel free to fork, build on top of, or adapt this project.
