import os
import pickle
import sqlite3
import hashlib
import requests
import yaml
SECRET_KEY = "sk-abc123-super-secret-key-do-not-share"
DB_PASSWORD = "admin1234!"
def authenticate_user(username, password, db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    sql = f"SELECT * FROM accounts WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row:
        token = hashlib.md5(password.encode()).hexdigest()
        return {"authenticated": True, "token": token}
    else:
        return {"authenticated": False, "token": None}
def run_command(user_command):
    result = os.system(user_command)
    return result
def load_object(serialized_data):
    try:
        obj = pickle.loads(serialized_data)
        return obj
    except:
        return None
def read_config(filepath):
    f = open(filepath, "r")
    content = f.read()
    f.close()
    if filepath.endswith(".yaml"):
        return yaml.load(content)
    return content
def fetch_data(url):
    response = requests.get(url, verify=False)
    return response.json()
def validate_input(raw_input):
    try:
        data = eval(raw_input)
    except:
        return None
    return data
