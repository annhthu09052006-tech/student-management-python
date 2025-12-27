
from Menu import show_menu
from student import add_student, view_students, sort_students, save_students_to_file
from student import load_students_from_file
from student import edit_student_by_mssv
def main():
    load_students_from_file()

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

# Điểm bắt đầu chương trình
if __name__ == "__main__":
    main()
