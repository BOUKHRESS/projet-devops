from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

requests_total = Counter(
    "app_requests_total",
    "Nombre total de requêtes"
)

@app.route("/")
def home():
    requests_total.inc()
    return "Bonjour depuis mon application DevOps !"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

app.run(host="0.0.0.0", port=5000)
