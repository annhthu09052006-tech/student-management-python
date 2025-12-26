import json
import os

students = []

# 1. Thêm sinh viên
def add_student():
    print("\n--- Thêm sinh viên mới ---")
    name = input("Nhập họ tên sinh viên: ").strip()
    age = input("Nhập tuổi: ").strip()
    score = input("Nhập điểm trung bình: ").strip()

    student = {
        "name": name,
        "age": age,
        "score": score
    }
    students.append(student)
    print("✓ Đã thêm sinh viên thành công!")

# 2. Xem danh sách sinh viên
def view_students():
    if not students:
        print("\nDanh sách sinh viên đang trống!")
        return

    print("\n--- Danh sách sinh viên ---")
    print(f"{'STT':<5} {'Họ tên':<20} {'Tuổi':<10} {'Điểm TB':<10}")
    print("-" * 50)
    for i, sv in enumerate(students, 1):
        print(f"{i:<5} {sv['name']:<20} {sv['age']:<10} {sv['score']:<10}")

# 6. Sắp xếp sinh viên
def sort_students():
    if not students:
        print("\nDanh sách sinh viên đang trống!")
        return

    print("\n--- Sắp xếp sinh viên ---")
    print("1. Sắp xếp theo tên (A → Z)")
    print("2. Sắp xếp theo điểm (tăng dần)")

    choice = input("Chọn kiểu sắp xếp (1-2): ").strip()

    if choice == "1":
        students.sort(key=lambda sv: sv["name"].lower())
        print("\n✓ Đã sắp xếp theo tên tăng dần!")

    elif choice == "2":
        students.sort(key=lambda sv: float(sv["score"]))
        print("\n✓ Đã sắp xếp theo điểm tăng dần!")

    else:
        print("\nLựa chọn không hợp lệ!")
        return

    # Hiển thị lại danh sách sau khi sắp xếp
    view_students()

def load_students_from_file():
    global students
    filename = "students.json"

    # Nếu file không tồn tại → danh sách rỗng
    if not os.path.exists(filename):
        students = []
        return

    # Nếu file tồn tại nhưng trống
    if os.path.getsize(filename) == 0:
        students = []
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            students = json.load(f)
    except json.JSONDecodeError:
        # File lỗi định dạng
        students = []
