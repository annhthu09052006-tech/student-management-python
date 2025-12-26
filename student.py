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