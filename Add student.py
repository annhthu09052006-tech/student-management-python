import json
import os

FILE_NAME = "students.json"

def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

def is_id_exists(students, student_id):
    return any(student["id"] == student_id for student in students)
def them_mot_sinh_vien():
    print("\n=== THÊM SINH VIÊN MỚI ===\n")
    
    students = load_students()
    
    while True:
        try:
            ten = input("Nhập họ và tên: ").strip()
            if not ten:
                print("❌ Lỗi: Tên không được để trống!\n")
                continue
            
            tuoi_str = input("Nhập tuổi: ").strip()
            tuoi = int(tuoi_str)
            if tuoi <= 0:
                print("❌ Lỗi: Tuổi phải lớn hơn 0!\n")
                continue
            
            ma_sv = input("Nhập ID sinh viên: ").strip()
            if not ma_sv:
                print("❌ Lỗi: ID không được để trống!\n")
                continue
            if is_id_exists(students, ma_sv):
                print("❌ Lỗi: ID sinh viên đã tồn tại!\n")
                continue
            
            diem_str = input("Nhập điểm trung bình (0 - 10): ").strip()
            diem = float(diem_str)
            if diem < 0 or diem > 10:
                print("❌ Lỗi: Điểm phải từ 0 đến 10!\n")
                continue
            
            sinh_vien_moi = {
                "id": ma_sv,
                "name": ten,
                "age": tuoi,
                "score": diem
            }
            
            students.append(sinh_vien_moi)
            save_students(students)
            
            print("\n✅ Thêm sinh viên thành công!")
            print(f"   → {ten} (ID: {ma_sv}, Tuổi: {tuoi}, Điểm: {diem})\n")
            break
            
        except ValueError:
            print("❌ Lỗi: Tuổi và điểm phải là số hợp lệ!\n")
        
    if __name__ == "__main__":
     print("🌟 CHƯƠNG TRÌNH THÊM SINH VIÊN 🌟\n")
    
    while True:
        them_mot_sinh_vien()
        
        while True:
            tiep_tuc = input("Bạn có muốn thêm sinh viên khác không? (y/n): ").strip().lower()
            if tiep_tuc in ["y", "yes", "có", "co"]:
                print("-" * 40)
                break
            elif tiep_tuc in ["n", "no", "không", "khong"]:
                print("\nCảm ơn bạn đã sử dụng chương trình. Tạm biệt! 👋\n")
                exit()
            else:
                print('Vui lòng nhập "y" (có) hoặc "n" (không).')
def xem_danh_sach_sinh_vien():
    print("\n=== DANH SÁCH SINH VIÊN ===\n")
    students = load_students()
    
    if not students:
        print("Hiện tại chưa có sinh viên nào.")
        return
    
    for sv in students:
        print(f"ID: {sv['id']} | Tên: {sv['name']} | Tuổi: {sv['age']} | Điểm: {sv['score']}")
    print()