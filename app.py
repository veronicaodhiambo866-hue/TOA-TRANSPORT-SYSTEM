from pathlib import Path

from flask import Flask, jsonify, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__)

dashboard_data = {
    "vehicles": 18,
    "available_vehicles": 11,
    "drivers_on_duty": 14,
    "todays_trips": 16,
    "pending_requests": 3,
    "vehicles_on_standby": 2,
    "staff_late": 5,
    "departures": 9,
}


@app.route("/")
def hello_world():
    return send_from_directory(BASE_DIR, "TOA FRONTEND.HTML")


@app.get("/api/health")
def health_check():
    return jsonify({"status": "ok"})


@app.get("/api/dashboard")
def dashboard():
    return jsonify(dashboard_data)


if __name__ == "__main__":
    app.run(debug=True)