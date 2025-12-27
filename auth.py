from account import login

current_user = None

def require_login():
    global current_user

    while current_user is None:
        print("\n====== ĐĂNG NHẬP HỆ THỐNG ======")
        current_user = login()
        if current_user is None:
            print("⚠ Vui lòng đăng nhập để tiếp tục!")

    return current_user


def is_teacher():
    return current_user and current_user["role"] == "Giảng viên"


def is_student():
    return current_user and current_user["role"] == "Sinh viên"