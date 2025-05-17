import json
import os

FILE_PATH = 'users_db.txt'

def load_users():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(FILE_PATH, 'w') as file:
        json.dump(users, file)

def get_user_by_username(username):
    users = load_users()
    return next((u for u in users if u['username'] == username), None)

def create_user(username, password):
    users = load_users()
    if get_user_by_username(username):
        return False
    users.append({'username': username, 'password': password})
    save_users(users)
    return True
