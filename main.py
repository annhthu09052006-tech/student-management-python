
from Menu import show_menu
from student import (
    add_student, view_students, sort_students,
    save_students_to_file, load_students_from_file,
    edit_student_by_mssv, view_my_info, view_my_score,
    view_my_schedule, view_my_exam
)
from account import change_password
from account import load_accounts
from auth import require_login, is_teacher, is_student, logout


def teacher_menu():
    while True:
        show_menu()
        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            edit_student_by_mssv()
        elif choice == "6":
            sort_students()
        elif choice == "7":
            save_students_to_file()
        elif choice == "8":
            load_students_from_file()
            print("✓ Đã tải dữ liệu từ file")
        elif choice == "0":
            logout()
            print("Tạm biệt giảng viên!")
            break
        else:
            print("Lựa chọn không hợp lệ!")




def main():
    load_students_from_file()
    load_accounts()

    while True:
        user = require_login()   # luôn quay lại đăng nhập

        if is_teacher():
            teacher_menu()
        elif is_student():
            student_menu()

if __name__ == "__main__":
    main()
