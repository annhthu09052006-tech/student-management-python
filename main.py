from Menu import show_menu
from student import add_student, view_students

def main():
    while True:
        show_menu()

        choice = input("Nhập lựa chọn của bạn (0-9): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "0":
            print("\nCảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break

        else:
            print("\nLựa chọn không hợp lệ! Vui lòng nhập số từ 0 đến 9.")

# Điểm bắt đầu chương trình
if __name__ == "__main__":
    main()
