from account import login, register_account

current_user = None

def require_login():
    global current_user

    while current_user is None:
        print("\n====== HỆ THỐNG ======")
        print("1. Đăng nhập")
        print("2. Đăng ký")
        print("0. Thoát")

        choice = input("Chọn: ").strip()

        if choice == "1":
            current_user = login()
            if current_user is None:
                print("⚠ Sai tài khoản hoặc mật khẩu!")
        elif choice == "2":
            register_account()
        elif choice == "0":
            print("👋 Tạm biệt!")
            exit()
        else:
            print("Lựa chọn không hợp lệ!")

    return current_user


def is_teacher():
    return current_user and current_user["role"] == "Giảng viên"


def is_student():
    return current_user and current_user["role"] == "Sinh viên"
def logout():
    global current_user
    current_user = None