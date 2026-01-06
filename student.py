import json
import os

students = []

# 1. Thêm sinh viên
def add_student():
    print("\n--- Thêm sinh viên mới ---")
    mssv = input("Nhập MSSV: ").strip()
    name = input("Nhập họ tên sinh viên: ").strip()
    age = int(input("Nhập tuổi: ").strip())
    score = float(input("Nhập điểm trung bình: ").strip())

    student = {
        "mssv": mssv,
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
        input("Nhấn Enter để quay lại menu...")
        return

    while True:
        print("\n--- DANH SÁCH SINH VIÊN ---")
        print(f"{'STT':<5} {'MSSV':<10} {'Họ tên':<20} {'Tuổi':<6} {'Điểm TB':<8}")
        print("-" * 55)

        for i, sv in enumerate(students, 1):
            print(f"{i:<5} {sv.get('mssv','N/A'):<10} {sv['name']:<20} {sv['age']:<6} {sv['score']:<8}")

        print("\n0. Quay lại menu")
        choice = input("Chọn: ").strip()

        if choice == "0":
            break
        else:
            print("⚠ Lựa chọn không hợp lệ, hãy bấm 0 để quay lại!")

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

def edit_student_by_mssv():
    if not students:
        print("\nDanh sách sinh viên đang trống!")
        input("Nhấn Enter để quay lại menu...")
        return

    # 🔥 BƯỚC 1: HIỆN BẢNG DANH SÁCH
    show_students_table()

    print("\n0. Quay lại menu")
    choice = input("Nhập STT sinh viên cần sửa: ").strip()

    # 🔙 Quay lại menu
    if choice == "0":
        return

    # 🚨 Kiểm tra STT hợp lệ
    if not choice.isdigit():
        print("✘ STT không hợp lệ!")
        input("Nhấn Enter để quay lại menu...")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(students):
        print("✘ STT không tồn tại!")
        input("Nhấn Enter để quay lại menu...")
        return

    # ✅ LẤY SINH VIÊN THEO STT (CHỖ BẠN HỎI)
    sv = students[index]

    # 🔎 Hiển thị thông tin hiện tại
    print("\n--- THÔNG TIN HIỆN TẠI ---")
    print(f"MSSV   : {sv.get('mssv', 'N/A')}")
    print(f"Họ tên : {sv.get('name', 'N/A')}")
    print(f"Tuổi   : {sv.get('age', '-')}")
    print(f"Điểm TB: {sv.get('score', '-')}")


    print("\n--- Nhập thông tin mới (Enter để giữ nguyên) ---")
    new_mssv = input("MSSV mới: ").strip()
    new_name = input("Họ tên mới: ").strip()
    new_age = input("Tuổi mới: ").strip()
    new_score = input("Điểm TB mới: ").strip()

    if new_name:
        sv["name"] = new_name
    if new_age:
        sv["age"] = int(new_age)
    if new_score:
        sv["score"] = float(new_score)
    if new_mssv:
        sv["mssv"] = new_mssv


    print("\n✓ Cập nhật thông tin sinh viên thành công!")
    input("Nhấn Enter để quay lại menu...")

def show_students_table():
    print("\n--- DANH SÁCH SINH VIÊN ---")
    print(f"{'STT':<5} {'MSSV':<10} {'Họ tên':<20} {'Tuổi':<6} {'Điểm TB':<8}")
    print("-" * 55)

    for i, sv in enumerate(students, 1):
        print(
            f"{i:<5} "
            f"{sv.get('mssv','N/A'):<10} "
            f"{sv.get('name','N/A'):<20} "
            f"{sv.get('age','-'):<6} "
            f"{sv.get('score','-'):<8}"
        )
