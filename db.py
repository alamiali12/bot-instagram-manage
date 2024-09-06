import json
import os

ACCOUNTS_FILE = 'accounts.json'
PROXIES_FILE = 'proxies.json'

def init_db():
    if not os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'w') as f:
            json.dump([], f)
    if not os.path.exists(PROXIES_FILE):
        with open(PROXIES_FILE, 'w') as f:
            json.dump([], f)

def add_account(username, password, token):
    with open(ACCOUNTS_FILE, 'r') as f:
        accounts = json.load(f)

    accounts.append({"username": username, "password": password, "token": token})

    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def get_accounts():
    with open(ACCOUNTS_FILE, 'r') as f:
        return json.load(f)

def update_account_token(username, token):
    with open(ACCOUNTS_FILE, 'r') as f:
        accounts = json.load(f)

    for account in accounts:
        if account["username"] == username:
            account["token"] = token
            break

    with open(ACCOUNTS_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def add_proxy(proxy):
    with open(PROXIES_FILE, 'r') as f:
        proxies = json.load(f)

    proxies.append(proxy)

    with open(PROXIES_FILE, 'w') as f:
        json.dump(proxies, f, indent=4)

def get_proxies():
    with open(PROXIES_FILE, 'r') as f:
        return json.load(f)
