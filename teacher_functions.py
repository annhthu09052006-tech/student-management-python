import json
from auth import get_current_user  # Lấy user hiện tại (sau khi login)
from role_base_access import has_permission  # Nếu có kiểm tra permission chi tiết (tùy chọn)

# Đường dẫn file dữ liệu (giống repo hiện tại)
STUDENTS_FILE = 'students.json'


def load_students():
    try:
        with open(STUDENTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(students, f, indent=4, ensure_ascii=False)


# Kiểm tra xem user hiện tại có phải là giảng viên không
def is_teacher():
    user = get_current_user()
    return user and user.get('role') == 'teacher'  # Repo dùng 'teacher' thay vì 'lecturer'


# 1. Nhập / sửa điểm cho sinh viên
def enter_or_update_grade(mssv: str, subject: str, grade: float):
    if not is_teacher():
        print("Quyền truy cập bị từ chối: Chỉ giảng viên mới được thực hiện.")
        return

    students = load_students()
    for student in students:
        if student.get('mssv') == mssv:
            if 'grades' not in student:
                student['grades'] = {}
            student['grades'][subject] = grade
            save_students(students)
            print(f"Đã cập nhật điểm môn {subject} = {grade} cho sinh viên {mssv}")
            return
    print(f"Không tìm thấy sinh viên có MSSV: {mssv}")


# 2. Cập nhật lịch thi cho sinh viên
def update_exam_schedule(mssv: str, subject: str, exam_date: str):
    if not is_teacher():
        print("Quyền truy cập bị từ chối: Chỉ giảng viên mới được thực hiện.")
        return

    students = load_students()
    for student in students:
        if student.get('mssv') == mssv:
            if 'exam_schedule' not in student:
                student['exam_schedule'] = {}
            student['exam_schedule'][subject] = exam_date
            save_students(students)
            print(f"Đã cập nhật lịch thi môn {subject}: {exam_date} cho sinh viên {mssv}")
            return
    print(f"Không tìm thấy sinh viên có MSSV: {mssv}")


# 3. Cập nhật lịch học cho sinh viên
def update_class_schedule(mssv: str, subject: str, class_time: str):
    if not is_teacher():
        print("Quyền truy cập bị từ chối: Chỉ giảng viên mới được thực hiện.")
        return

    students = load_students()
    for student in students:
        if student.get('mssv') == mssv:
            if 'class_schedule' not in student:
                student['class_schedule'] = {}
            student['class_schedule'][subject] = class_time
            save_students(students)
            print(f"Đã cập nhật lịch học môn {subject}: {class_time} cho sinh viên {mssv}")
            return
    print(f"Không tìm thấy sinh viên có MSSV: {mssv}")


# Menu dành riêng cho giảng viên (teacher_menu) - đã được cập nhật với các chức năng mới
def teacher_menu():
    if not is_teacher():
        print("Quyền truy cập bị từ chối.")
        return

    while True:
        print("\n" + "=" * 40)
        print(" MENU QUẢN LÝ SINH VIÊN - GIẢNG VIÊN")
        print("=" * 40)
        print("1. Thêm sinh viên")
        print("2. Xem danh sách sinh viên")
        print("3. Sửa thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm sinh viên theo tên")
        print("6. Sắp xếp sinh viên theo tên")
        print("7. Lưu danh sách sinh viên vào file")
        print("8. Tải danh sách sinh viên từ file")
        print("9. Nhập / sửa điểm sinh viên")
        print("10. Cập nhật lịch học cho sinh viên")
        print("11. Cập nhật lịch thi cho sinh viên")
        print("0. Thoát")
        print("=" * 40)

        choice = input("Nhập lựa chọn của bạn: ").strip()

        if choice == "1":
            from student_functions import add_student  # Import động để tránh circular
            add_student()
        elif choice == "2":
            from student_functions import view_students
            view_students()
        elif choice == "3":
            from student_functions import edit_student_by_mssv
            edit_student_by_mssv()
        elif choice == "4":
            from student_functions import delete_student  # Giả sử có hàm này, nếu chưa thì thêm tương tự
            mssv = input("Nhập MSSV sinh viên cần xóa: ")
            # delete_student(mssv)  # Uncomment khi có hàm
            print("Chức năng xóa đang phát triển...")
        elif choice == "5":
            from student_functions import search_student_by_name
            name = input("Nhập tên cần tìm: ")
            # search_student_by_name(name)
            print("Chức năng tìm kiếm đang phát triển...")
        elif choice == "6":
            from student_functions import sort_students
            sort_students()
        elif choice == "7":
            from student_functions import save_students_to_file
            save_students_to_file()
        elif choice == "8":
            from student_functions import load_students_from_file
            load_students_from_file()
            print("Đã tải dữ liệu từ file")
        elif choice == "9":
            mssv = input("Nhập MSSV sinh viên: ")
            subject = input("Nhập tên môn học: ")
            try:
                grade = float(input("Nhập điểm: "))
                enter_or_update_grade(mssv, subject, grade)
            except ValueError:
                print("Điểm phải là số!")
        elif choice == "10":
            mssv = input("Nhập MSSV sinh viên: ")
            subject = input("Nhập tên môn học: ")
            class_time = input("Nhập lịch học (vd: Thứ 2 7h-9h): ")
            update_class_schedule(mssv, subject, class_time)
        elif choice == "11":
            mssv = input("Nhập MSSV sinh viên: ")
            subject = input("Nhập tên môn học: ")
            exam_date = input("Nhập ngày thi (vd: 15/01/2026): ")
            update_exam_schedule(mssv, subject, exam_date)
        elif choice == "0":
            from auth import logout
            logout()
            print("Tạm biệt giảng viên!")
            break
        else:
            print("Lựa chọn không hợp lệ!")
