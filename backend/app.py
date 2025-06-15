from flask import Flask, request, jsonify
from matching_engine.matcher import load_data, match_employees_to_project

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
    data = request.json
    project = data.get("project")
    employees, _ = load_data("data/employees.csv", "data/projects.csv")
    matches = match_employees_to_project(employees, project).to_dict(orient="records")
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)
