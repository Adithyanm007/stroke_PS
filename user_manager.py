import json
import bcrypt
import os

USER_FILE = "users.json"

def load_users():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({}, f)
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def register_user(username, password):
    users = load_users()
    if username in users:
        return False, "User already exists"
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = hashed
    save_users(users)
    return True, "Account created successfully!"

def authenticate_user(username, password):
    users = load_users()
    if username in users:
        hashed = users[username].encode()
        if bcrypt.checkpw(password.encode(), hashed):
            return True
        else:
            return False
    else:
        return False
