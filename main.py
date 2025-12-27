
from Menu import show_menu
from student import add_student, view_students, sort_students, save_students_to_file
from student import load_students_from_file
from student import edit_student_by_mssv
from account import load_accounts, login, register_account
from account import load_accounts, register_account
from auth import require_login, is_teacher, is_student
def main():
    load_students_from_file()
    load_accounts()
    load_accounts()
    user = require_login()

    user = None
    while user is None:
        print("\n1. Đăng nhập")
        print("2. Đăng ký")
        choice = input("Chọn: ").strip()

        if choice == "1":
            user = login()
        elif choice == "2":
            register_account()
        else:
            print("Lựa chọn không hợp lệ!")

    while True:
        show_menu()
        choice = input("Nhập lựa chọn của bạn (0-9): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            edit_student_by_mssv()
        elif choice == "6":
            sort_students()
        elif choice == "7":
            save_students_to_file()  # Gọi hàm lưu file vừa tạo
        elif choice == "8":
            load_students_from_file() # Tải lại dữ liệu từ file
            print("\n✓ Đã tải dữ iệu từ file thành công!")
        elif choice == "0":
            print("\nCảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("\nLựa chọn không hợp lệ! Vui lòng nhập số từ 0 đến 9.")
        if choice == "1":
            if is_teacher():
                add_student()
            else:
                print("✘ Chỉ giảng viên mới được thêm sinh viên!")

        elif choice == "2":
            view_students()

        elif choice == "3":
            if is_teacher():
                edit_student_by_mssv()
            else:
                print("✘ Chỉ giảng viên mới được sửa sinh viên!")

        elif choice == "7":
            if is_teacher():
                save_students_to_file()
            else:
                print("✘ Sinh viên không được phép lưu file!")
# Điểm bắt đầu chương trình
if __name__ == "__main__":
    main()
