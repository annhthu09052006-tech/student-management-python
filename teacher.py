import json
import os
from auth import current_user
FILE_NAME = "students.json"
students = []

# 1. Thêm sinh viên
def add_student():
    print("\n--- Thêm sinh viên mới ---")

    mssv = input("Nhập mã sinh viên (MSSV): ").strip()

    # Kiểm tra trùng MSSV
    for sv in students:
        if sv["mssv"] == mssv:
            print("❌ MSSV đã tồn tại!")
            return

    name = input("Nhập họ tên sinh viên: ").strip()

    try:
        age = int(input("Nhập tuổi: "))
        score = float(input("Nhập điểm trung bình: "))
    except ValueError:
        print("❌ Tuổi hoặc điểm không hợp lệ!")
        return

    student = {
        "mssv": mssv,
        "name": name,
        "age": age,
        "score": score
    }

    students.append(student)
    print("✅ Thêm sinh viên thành công!")

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

def load_students_from_file():
    global students
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                students = json.load(f)
        except json.JSONDecodeError:
            students = []
    else:
        students = []

def save_students_to_file():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

def load_students_from_file():
    global students
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                students = json.load(f)
                # Ép kiểu cho đúng
                for sv in students:
                    if 'age' in sv:
                        sv['age'] = int(sv['age'])
                    if 'score' in sv:
                        sv['score'] = float(sv['score'])
        except json.JSONDecodeError:
            students = []
    else:
        students = []


def save_students_to_file():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

def find_student_by_mssv(mssv):
    for sv in students:
        if sv.get("mssv") == mssv:
            return sv
    return None

def get_current_student():
    if not current_user:
        return None

    mssv = current_user["username"]  # username = MSSV
    return find_student_by_mssv(mssv)

def add_schedule_for_student():
    if not students:
        print("\nDanh sách sinh viên đang trống!")
        input("Nhấn Enter để quay lại menu...")
        return

    # 🔥 HIỆN BẢNG DANH SÁCH ĐỂ LỰA CHỌN
    show_students_table()
    
    print("\n0. Quay lại menu")
    choice = input("Chọn STT sinh viên cần thêm lịch học: ").strip()

    if choice == "0": return
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(students):
        print("❌ Lựa chọn không hợp lệ!")
        return

    # Lấy sinh viên dựa trên STT
    sv = students[int(choice) - 1]

    print(f"\n--- Đang nhập lịch học cho: {sv.get('name')} (MSSV: {sv.get('mssv')}) ---")

    day = input("Thứ (VD: Thứ 2): ").strip()
    subject = input("Môn học: ").strip()
    room = input("Phòng học: ").strip()
    time = input("Thời gian (VD: 7h30 - 9h30): ").strip()

    if not (day and subject and room and time):
        print("⚠️ Không được bỏ trống thông tin!")
        return

    sv["schedule"] = {
        "day": day,
        "subject": subject,
        "room": room,
        "time": time
    }
    save_students_to_file()

    print("✅ Đã cập nhật lịch học thành công!")
    input("\nNhấn Enter để quay lại menu...")


def add_exam_for_student():
    if not students:
        print("\nDanh sách sinh viên đang trống!")
        input("Nhấn Enter để quay lại menu...")
        return

    # 🔥 HIỆN BẢNG DANH SÁCH ĐỂ LỰA CHỌN
    show_students_table()
    
    print("\n0. Quay lại menu")
    choice = input("Chọn STT sinh viên cần thêm lịch thi: ").strip()

    if choice == "0": return
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(students):
        print("❌ Lựa chọn không hợp lệ!")
        return

    # Lấy sinh viên dựa trên STT
    sv = students[int(choice) - 1]

    print(f"\n--- Đang nhập lịch thi cho: {sv.get('name')} (MSSV: {sv.get('mssv')}) ---")

    day = input("Thứ (VD: Thứ 6): ").strip()
    subject = input("Môn thi: ").strip()
    room = input("Phòng thi: ").strip()
    time = input("Thời gian thi (VD: 13h30 - 15h30): ").strip()

    if not (day and subject and room and time):
        print("⚠️ Không được bỏ trống thông tin!")
        return

    sv["exam"] = {
        "day": day,
        "subject": subject,
        "room": room,
        "time": time
    }
    save_students_to_file() # Nhớ lưu lại file sau khi sửa

    print("✅ Đã cập nhật lịch thi thành công!")
    input("\nNhấn Enter để quay lại menu...")
def delete_student_by_mssv():
    if not students:
        print("\nDanh sách sinh viên đang trống!")
        input("Nhấn Enter để quay lại menu...")
        return

    # 1. Hiển thị bảng để người dùng dễ nhìn
    show_students_table()

    # 2. Cho phép chọn theo STT để tránh gõ sai MSSV dài
    choice = input("\nNhập STT sinh viên cần xóa (0 để hủy): ").strip()
    
    if choice == "0":
        return

    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(students):
        print("❌ STT không hợp lệ!")
        input("Nhấn Enter để tiếp tục...")
        return

    index = int(choice) - 1
    sv = students[index]

    # 3. Xác nhận trước khi xóa
    confirm = input(f"⚠️ Bạn có chắc muốn xóa vĩnh viễn sinh viên: {sv['name']} (MSSV: {sv['mssv']})? (y/n): ").strip().lower()
    
    if confirm == "y":
        # Xóa khỏi danh sách trong bộ nhớ RAM
        removed_name = sv['name']
        students.pop(index) 
        
        # 🔥 QUAN TRỌNG: Cập nhật ngay lập tức vào file JSON
        save_students_to_file()
        
        print(f"✅ Đã xóa vĩnh viễn sinh viên {removed_name} khỏi hệ thống và file dữ liệu!")
    else:
        print("❌ Đã hủy thao tác xóa.")
    
    input("Nhấn Enter để quay lại menu...")
def find_students_by_name():
    if not students:
        print("\nDanh sách sinh viên đang trống!")
        input("Nhấn Enter để quay lại menu...")
        return

    name_query = input("Nhập tên sinh viên cần tìm: ").strip().lower()
    if not name_query:
        print("⚠ Bạn chưa nhập tên sinh viên!")
        return

    # Tìm sinh viên có tên chứa từ khóa (không phân biệt hoa/thường)
    matched_students = [sv for sv in students if name_query in sv.get("name", "").lower()]

    if not matched_students:
        print("❌ Không tìm thấy sinh viên nào phù hợp!")
        input("Nhấn Enter để quay lại menu...")
        return

    # Hiển thị danh sách sinh viên tìm được
    print("\n--- DANH SÁCH SINH VIÊN TÌM THẤY ---")
    print(f"{'STT':<5} {'MSSV':<10} {'Họ tên':<20} {'Tuổi':<6} {'Điểm TB':<8}")
    print("-" * 55)

    for i, sv in enumerate(matched_students, 1):
        print(
            f"{i:<5} "
            f"{sv.get('mssv','N/A'):<10} "
            f"{sv.get('name','N/A'):<20} "
            f"{sv.get('age','-'):<6} "
            f"{sv.get('score','-'):<8}"
        )

    input("\nNhấn Enter để quay lại menu...")
