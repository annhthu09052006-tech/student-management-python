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
def sua_thong_tin_sinh_vien():
    print("\n=== SỬA THÔNG TIN SINH VIÊN ===\n")
    students = load_students()
    
    if not students:
        print("📭 Danh sách sinh viên trống! Không có ai để sửa.\n")
        return
    
    ma_sv = input("Nhập ID sinh viên cần sửa: ").strip()
    
    # Tìm sinh viên theo ID
    sinh_vien_tim_thay = None
    for sv in students:
        if sv["id"] == ma_sv:
            sinh_vien_tim_thay = sv
            break
    
    if not sinh_vien_tim_thay:
        print(f"❌ Không tìm thấy sinh viên với ID: {ma_sv}\n")
        return
    
    # Hiển thị thông tin hiện tại (chỉ in 1 lần, sạch sẽ)
    print(f"Thông tin hiện tại:")
    print(f"   Tên : {sinh_vien_tim_thay['name']}")
    print(f"   Tuổi: {sinh_vien_tim_thay['age']}")
    print(f"   Điểm: {sinh_vien_tim_thay['score']}\n")
    
    # Nhập thông tin mới (Enter để giữ nguyên)
    try:
        ten_moi = input(f"Tên mới (Enter để giữ '{sinh_vien_tim_thay['name']}'): ").strip()
        if ten_moi:
            sinh_vien_tim_thay["name"] = ten_moi
        
        tuoi_input = input(f"Tuổi mới (Enter để giữ {sinh_vien_tim_thay['age']}): ").strip()
        if tuoi_input:
            tuoi_moi = int(tuoi_input)
            if tuoi_moi <= 0:
                print("❌ Lỗi: Tuổi phải lớn hơn 0! Giữ nguyên tuổi cũ.")
            else:
                sinh_vien_tim_thay["age"] = tuoi_moi
        
        diem_input = input(f"Điểm mới (Enter để giữ {sinh_vien_tim_thay['score']}): ").strip()
        if diem_input:
            diem_moi = float(diem_input)
            if diem_moi < 0 or diem_moi > 10:
                print("❌ Lỗi: Điểm phải từ 0 đến 10! Giữ nguyên điểm cũ.")
            else:
                sinh_vien_tim_thay["score"] = diem_moi
        
        # Lưu lại vào file JSON
        save_students(students)
        
        # Thông báo thành công
        print("\n✅ Cập nhật thông tin sinh viên thành công!")
        print(f"   ID: {ma_sv}")
        print(f"   Tên : {sinh_vien_tim_thay['name']}")
        print(f"   Tuổi: {sinh_vien_tim_thay['age']}")
        print(f"   Điểm: {sinh_vien_tim_thay['score']}\n")
        
    except ValueError:
        print("❌ Lỗi: Dữ liệu nhập không hợp lệ (tuổi và điểm phải là số)! Không thay đổi gì.\n")

    def xoa_sinh_vien():
     print("\n=== XÓA SINH VIÊN ===\n")
    students = load_students()
    
    if not students:
        print("📭 Danh sách sinh viên trống! Không có ai để xóa.\n")
        return
    
    ma_sv = input("Nhập ID sinh viên cần xóa: ").strip()
    
    # Tìm sinh viên theo ID
    sinh_vien_tim_thay = None
    vi_tri = -1
    for i, sv in enumerate(students):
        if sv["id"] == ma_sv:
            sinh_vien_tim_thay = sv
            vi_tri = i
            break
    
    if sinh_vien_tim_thay is None:
        print(f"❌ Không tìm thấy sinh viên với ID: {ma_sv}\n")
        return
    
    # Hiển thị thông tin sinh viên sắp xóa
    print(f"Tìm thấy sinh viên:")
    print(f"   ID  : {sinh_vien_tim_thay['id']}")
    print(f"   Tên : {sinh_vien_tim_thay['name']}")
    print(f"   Tuổi: {sinh_vien_tim_thay['age']}")
    print(f"   Điểm: {sinh_vien_tim_thay['score']}\n")