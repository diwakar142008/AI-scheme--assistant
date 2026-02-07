from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load schemes from JSON
with open("data.json", "r", encoding="utf-8") as f:
    schemes = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    results = None

    if request.method == "POST":
        occupation = request.form["occupation"]
        social_category = request.form["caste"]
        gender = request.form["gender"]
        income = int(request.form["income"])

        results = []

        for scheme in schemes:
            # Category match
            if scheme["category"] != occupation:
                continue

            # Social category match
            if scheme["social_category"] != social_category:
                continue

            # Gender match (allow 'any')
            if scheme["gender"] != "any" and scheme["gender"] != gender:
                continue

            # Income check
            if income > scheme["max_income"]:
                continue

            results.append(scheme)

    return render_template("index.html", results=results)

@app.route("/scheme/<int:scheme_id>")
def scheme_page(scheme_id):
    scheme = next((s for s in schemes if s["id"] == scheme_id), None)
    return render_template("scheme.html", scheme=scheme)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

