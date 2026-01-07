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
# ==============================
# LƯU TÀI KHOẢN VÀO FILE
# ==============================
def save_accounts():
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
        json.dump(accounts, f, ensure_ascii=False, indent=4)
# ==============================
# TẠO TÀI KHOẢN MỚI
# ==============================
def register_account():
    print("\n--- Tạo tài khoản mới ---")
    role = input("Vai trò (sv/gv): ").strip().lower()

    if role == "sv":
        role = "Sinh viên"
        username = input("Nhập MSSV (dùng để đăng nhập): ").strip()

        from student import find_student_by_mssv
        if not find_student_by_mssv(username):
            print("❌ MSSV không tồn tại! Hãy thêm sinh viên trước.")
            return

    elif role == "gv":
        role = "Giảng viên"
        username = input("Tên đăng nhập giảng viên: ").strip()
    else:
        print("❌ Vai trò không hợp lệ!")
        return

    for acc in accounts:
        if acc["username"] == username:
            print("❌ Tài khoản đã tồn tại!")
            return

    password = input("Mật khẩu: ").strip()

    accounts.append({
        "username": username,   # ← MSSV
        "password": password,
        "role": role
    })

    save_accounts()
    print("✅ Tạo tài khoản thành công!")

# ==============================
# ĐĂNG NHẬP
# ==============================
def login():
    print("\n--- Đăng nhập ---")
    username = input("Tên đăng nhập: ").strip()
    password = input("Mật khẩu: ").strip()

    for acc in accounts:
        if acc["username"] == username and acc["password"] == password:
            print(f"\n✓ Đăng nhập thành công ({acc['role']})")
            return acc

    print("✘ Sai tên đăng nhập hoặc mật khẩu!")
    return None
def change_password(current_user):
    if not current_user:
        print("⚠ Chưa đăng nhập!")
        return

    old_pass = input("Mật khẩu cũ: ").strip()
    if old_pass != current_user["password"]:
        print("❌ Mật khẩu cũ không đúng!")
        return

    new_pass = input("Mật khẩu mới: ").strip()
    current_user["password"] = new_pass
    save_accounts()

    print("✅ Đổi mật khẩu thành công! Vui lòng đăng nhập lại.")

