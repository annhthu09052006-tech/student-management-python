import json
import os

students = []

# 1. Thêm sinh viên
def add_student():
    print("\n--- Thêm sinh viên mới ---")
    name = input("Nhập họ tên sinh viên: ").strip()
    age = int(input("Nhập tuổi: ")).strip()
    score = float(input("Nhập điểm trung bình: ")).strip()

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

    if not os.path.exists("students.json"):
        students.clear()
        return

    with open("students.json", "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            students.clear()
            students.extend(data)
        except json.JSONDecodeError:
            students.clear()

def save_students_to_file():
    if not students:
        print("\nDanh sách trống, không có dữ liệu để lưu!")
        return

    try:
        with open("students.json", "w", encoding="utf-8") as f:
            # indent=4 giúp file JSON dễ đọc hơn
            # ensure_ascii=False để lưu được tiếng Việt có dấu
            json.dump(students, f, ensure_ascii=False, indent=4)
        print("\n✓ Lưu dữ liệu thành công vào file 'students.json'!")
    except Exception as e:
        print(f"\n✘ Có lỗi xảy ra khi lưu file: {e}")