from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simulated device state
thermostat_state = {"temperature": 25}
users = {"admin": "admin"}  

@app.route('/')
def home():
    # HTML 
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username in users and users[username] == password:
        return jsonify({"status": "success", "message": "Login successful"}), 200
    return jsonify({"status": "error", "message": "Invalid credentials"}), 401

@app.route('/thermostat', methods=['GET', 'POST'])
def thermostat():
    global thermostat_state
    if request.method == 'GET':
        return jsonify(thermostat_state)
    elif request.method == 'POST':
        temp = request.form.get("temperature")
        if temp:
            thermostat_state["temperature"] = int(temp)
            return jsonify({"status": "success", "new_temperature": thermostat_state["temperature"]}), 200
        return jsonify({"status": "error", "message": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
