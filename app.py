from flask import Flask, jsonify

app = Flask(__name__)

tech_points = {
    "java": "Java uses JVM which makes it platform independent.",
    "docker": "Docker packages applications with dependencies into containers.",
    "kubernetes": "Kubernetes automates container deployment, scaling, and management.",
    "jenkins": "Jenkins automates CI/CD pipelines for building and deploying applications.",
    "python": "Python is known for simple syntax and rapid development."
}

@app.route("/")
def home():
    return "Tech Key Point API"

@app.route("/tech/<name>")
def tech_info(name):
    name = name.lower()
    
    if name in tech_points:
        return jsonify({
            "technology": name,
            "key_point": tech_points[name]
        })
    else:
        return jsonify({
            "error": "Technology not found"
        }), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
