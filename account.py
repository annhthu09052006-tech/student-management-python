import json
import os

ACCOUNTS_FILE = "accounts.json"
accounts = []

# ==============================
# TẢI TÀI KHOẢN TỪ FILE
# ==============================
def load_accounts():
    global accounts
    if not os.path.exists(ACCOUNTS_FILE):
        accounts = []
        return

    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            accounts = json.load(f)
    except json.JSONDecodeError:
        accounts = []