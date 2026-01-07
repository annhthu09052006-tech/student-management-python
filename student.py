import json
import os
from auth import current_user
FILE_NAME = "students.json"

from teacher import students, find_student_by_mssv

def save_students_to_file():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)



def get_current_student():
    if not current_user:
        return None

    mssv = current_user["username"]  # username = MSSV
    return find_student_by_mssv(mssv)
# =========================
# SINH VIÊN - XEM THÔNG TIN
# =========================
def view_student_info(student):
    print("\n" + "="*30)
    print("      THÔNG TIN SINH VIÊN      ")
    print("="*30)
    print(f"MSSV   : {student.get('mssv', 'N/A')}")
    print(f"Họ tên : {student.get('name', 'N/A')}")
    print(f"Tuổi   : {student.get('age', '-')}")
    print("-" * 30)
    print("💡 Lưu ý: Để xem điểm, vui lòng chọn mục 'Xem điểm' ở menu chính.")
    input("\nNhấn Enter để quay lại menu...")
    
def view_student_score(mssv):
    from teacher import find_student_by_mssv
    sv = find_student_by_mssv(mssv)
    if not sv:
        print("❌ Không tìm thấy sinh viên!")
        return
    print("\n====== ĐIỂM TRUNG BÌNH ======")
    print(f"{'MSSV':<10} {'Họ tên':<20} {'Điểm TB':<8}")
    print(f"{sv['mssv']:<10} {sv['name']:<20} {sv['score']:<8}")
    input("\nNhấn Enter để quay lại menu...")


def view_student_schedule(mssv):
    from teacher import find_student_by_mssv
    sv = find_student_by_mssv(mssv)
    if not sv or "schedule" not in sv:
        print("❌ Sinh viên chưa có lịch học!")
        return
    s = sv["schedule"]
    print("\n====== LỊCH HỌC ======")
    print(f"Thứ: {s['day']}")
    print(f"Môn học: {s['subject']}")
    print(f"Phòng: {s['room']}")
    print(f"Thời gian: {s['time']}")
    input("\nNhấn Enter để quay lại menu...")


def view_student_exam(mssv):
    from teacher import find_student_by_mssv
    sv = find_student_by_mssv(mssv)
    if not sv or "exam" not in sv:
        print("❌ Sinh viên chưa có lịch thi!")
        return
    e = sv["exam"]
    print("\n====== LỊCH THI ======")
    print(f"Thứ: {e['day']}")
    print(f"Môn thi: {e['subject']}")
    print(f"Phòng: {e['room']}")
    print(f"Thời gian: {e['time']}")
    input("\nNhấn Enter để quay lại menu...")





