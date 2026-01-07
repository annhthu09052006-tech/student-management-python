
from Menu import show_menu
from student import (
    add_student, view_students, sort_students,
    save_students_to_file, load_students_from_file,
    edit_student_by_mssv,find_student_by_mssv,
    add_schedule_for_student, add_exam_for_student
)
from Add_student import (
    view_student_info, view_student_score, 
    view_student_schedule, view_student_exam,
    find_student_by_mssv
    )
from account import change_password
from auth import logout
import auth

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
            input("\nNhấn Enter để quay lại menu...")

        elif choice == "3":
            edit_student_by_mssv()

        elif choice == "6":
            sort_students()
            input("\nNhấn Enter để quay lại menu...")

        elif choice == "7":
            save_students_to_file()
            input("\nNhấn Enter để quay lại menu...")

        elif choice == "8":
            load_students_from_file()
            print("✓ Đã tải dữ liệu từ file")
            input("\nNhấn Enter để quay lại menu...")
        elif choice == "9":
            change_password(auth.current_user)
            logout()
            break

        elif choice == "10":
            add_schedule_for_student()

        elif choice == "11":
            add_exam_for_student()

        elif choice == "0":
            logout()
            print("👋 Tạm biệt giảng viên!")
            break

        else:
            print("❌ Lựa chọn không hợp lệ!")

def student_menu():
    mssv = auth.current_user["username"]  # ← CHUẨN, KHÔNG LỖI

    sv = find_student_by_mssv(mssv)
    if not sv:
        print("❌ Không tìm thấy thông tin sinh viên!")
        logout()
        return

    while True:
        print("\n===== MENU SINH VIÊN =====")
        print("1. Xem thông tin cá nhân")
        print("2. Xem điểm trung bình")
        print("3. Xem lịch học")
        print("4. Xem lịch thi")
        print("0. Đăng xuất")

        choice = input("Chọn: ").strip()

        if choice == "1":
            view_student_info(mssv)
        elif choice == "2":
            view_student_score(mssv)
        elif choice == "3":
            view_student_schedule(mssv)
        elif choice == "4":
            view_student_exam(mssv)
        elif choice == "0":
            logout()
            print("👋 Đã đăng xuất sinh viên!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ!")


def main():
    load_students_from_file()
    load_accounts()

    while True:
        require_login()

        if is_teacher():
            teacher_menu()
        elif is_student():
            student_menu()


if __name__ == "__main__":
    main()
