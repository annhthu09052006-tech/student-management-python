from student_manager import StudentManager

manager = StudentManager()

while True:
    print("===== HỆ THỐNG QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách sinh viên")
    print("3. Tìm kiếm sinh viên")
    print("4. Xóa sinh viên")
    print("5. Thoát")

    choice = input("Chọn chức năng (1-5): ")

    if choice == "1":
        manager.add_student()
    elif choice == "2":
        manager.show_students()
    elif choice == "3":
        manager.search_student()
    elif choice == "4":
        manager.delete_student()
    elif choice == "5":
        print("Đã thoát chương trình!")
        break
    else:
        print("❌ Lựa chọn không hợp lệ, vui lòng chọn 1-5.\n")
