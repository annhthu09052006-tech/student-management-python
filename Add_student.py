import json
import os
from auth import current_user


students = []

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
# =========================
# SINH VIÊN - XEM THÔNG TIN
# =========================
def view_student_info(mssv):
    sv = find_student_by_mssv(mssv)

    if not sv:
        print("❌ Không tìm thấy thông tin sinh viên!")
        input("\nNhấn Enter để quay lại menu...")
        return

    print("\n====== THÔNG TIN CÁ NHÂN ======")
    print("-" * 40)
    print(f"MSSV     : {sv.get('mssv', 'N/A')}")
    print(f"Họ tên   : {sv.get('name', 'N/A')}")
    print(f"Tuổi     : {sv.get('age', 'N/A')}")
    print("-" * 40)

    input("\nNhấn Enter để quay lại menu...")

def view_student_score(mssv):
    sv = find_student_by_mssv(mssv)

    if not sv:
        print("❌ Không tìm thấy sinh viên!")
        input("\nNhấn Enter để quay lại menu...")
        return

    print("\n====== ĐIỂM TRUNG BÌNH ======")
    print("-" * 40)
    print(f"{'MSSV':<10} {'Họ tên':<20} {'Điểm TB':<8}")
    print("-" * 40)
    print(
        f"{sv.get('mssv','N/A'):<10} "
        f"{sv.get('name','N/A'):<20} "
        f"{sv.get('score','-'):<8}"
    )

    input("\nNhấn Enter để quay lại menu...")

def view_student_schedule(mssv):
    sv = find_student_by_mssv(mssv)

    if not sv or "schedule" not in sv:
        print("\n❌ Chưa có lịch học!")
        input("\nNhấn Enter để quay lại menu...")
        return

    s = sv["schedule"]

    print("\n====== LỊCH HỌC ======")
    print("-" * 60)
    print(f"{'Thứ':<10} {'Môn học':<20} {'Phòng':<10} {'Thời gian':<15}")
    print("-" * 60)
    print(
        f"{s.get('day','-'):<10} "
        f"{s.get('subject','-'):<20} "
        f"{s.get('room','-'):<10} "
        f"{s.get('time','-'):<15}"
    )

    input("\nNhấn Enter để quay lại menu...")

def view_student_exam(mssv):
    sv = find_student_by_mssv(mssv)

    if not sv or "exam" not in sv:
        print("\n❌ Chưa có lịch thi!")
        input("\nNhấn Enter để quay lại menu...")
        return

    e = sv["exam"]

    print("\n====== LỊCH THI ======")
    print("-" * 60)
    print(f"{'Thứ':<10} {'Môn thi':<20} {'Phòng':<10} {'Thời gian':<15}")
    print("-" * 60)
    print(
        f"{e.get('day','-'):<10} "
        f"{e.get('subject','-'):<20} "
        f"{e.get('room','-'):<10} "
        f"{e.get('time','-'):<15}"
    )

    input("\nNhấn Enter để quay lại menu...")



