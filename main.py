# Danh sách lưu trữ sinh viên (mỗi sinh viên là một dict)
students = []

def show_menu():
    print("\n" + "="*40)
    print("     MENU QUẢN LÝ SINH VIÊN")
    print("="*40)
    print("1. Thêm sinh viên")
    print("2. Xem danh sách sinh viên")
    print("3. Sửa thông tin sinh viên")
    print("4. Xóa sinh viên")
    print("5. Tìm sinh viên theo tên")
    print("6. Sắp xếp sinh viên theo tên")
    print("7. Lưu danh sách sinh viên vào file")
    print("8. Tải danh sách sinh viên từ file")
    print("9. Cập nhật thông tin sinh viên")  # có thể gộp với 3
    print("0. Thoát")
    print("="*40)

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

# 2. Xem danh sách
def view_students():
    if not students:
        print("\nDanh sách sinh viên đang trống!")
        return
    
    print("\n--- Danh sách sinh viên ---")
    print(f"{'STT':<5} {'Họ tên':<20} {'Tuổi':<10} {'Điểm TB':<10}")
    print("-"*50)
    for i, sv in enumerate(students, 1):
        print(f"{i:<5} {sv['name']:<20} {sv['age']:<10} {sv['score']:<10}")

# Chương trình chính
def main():
    while True:
        show_menu()  # Hiển thị toàn bộ menu mỗi lần lặp
        
        choice = input("Nhập lựa chọn của bạn (0-9): ").strip()
        
        if choice == "1":
            add_student()
            
        elif choice == "2":
            view_students()
            
        elif choice == "0":
            print("\nCảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
            
        else:
            print("\nLựa chọn không hợp lệ! Vui lòng nhập số từ 0 đến 9.")

# Chạy chương trình
if __name__ == "__main__":
    main()
    


    