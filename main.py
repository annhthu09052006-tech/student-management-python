
from Menu import show_menu
from student import (
    add_student, view_students, sort_students,
    save_students_to_file, load_students_from_file,
    edit_student_by_mssv
)
from account import load_accounts
from auth import require_login, is_teacher, is_student


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
            print("Tạm biệt giảng viên!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


def student_menu():
    while True:
        print("\n===== MENU SINH VIÊN =====")
        print("1. Xem danh sách sinh viên")
        print("0. Đăng xuất")

        choice = input("Chọn: ").strip()

        if choice == "1":
            view_students()
        elif choice == "0":
            print("Tạm biệt sinh viên!")
            break
        else:
            print("Lựa chọn không hợp lệ!")


def main():
    load_students_from_file()
    load_accounts()

    # 🔐 BẮT BUỘC ĐĂNG NHẬP
    user = require_login()

    # 🎭 PHÂN GIAO DIỆN THEO VAI TRÒ
    if is_teacher():
        teacher_menu()
    elif is_student():
        student_menu()


if __name__ == "__main__":
    main()
