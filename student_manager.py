from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Thêm sinh viên mới ---")
        student_id = input("Nhập mã sinh viên: ")
        name = input("Nhập họ tên: ")
        age = input("Nhập tuổi: ")
        major = input("Nhập ngành học: ")

        student = Student(student_id, name, age, major)
        self.students.append(student)
        print("✔ Thêm sinh viên thành công!\n")

    def show_students(self):
        print("\n--- Danh sách sinh viên ---")
        if not self.students:
            print("Chưa có sinh viên nào!\n")
            return
        for sv in self.students:
            sv.display()

    def search_student(self):
        print("\n--- Tìm kiếm sinh viên ---")
        keyword = input("Nhập mã hoặc tên sinh viên: ")

        found = False
        for sv in self.students:
            if sv.student_id == keyword or sv.name.lower() == keyword.lower():
                sv.display()
                found = True
        
        if not found:
            print("❌ Không tìm thấy sinh viên!\n")

    def delete_student(self):
        print("\n--- Xóa sinh viên ---")
        student_id = input("Nhập mã sinh viên cần xóa: ")

        for sv in self.students:
            if sv.student_id == student_id:
                self.students.remove(sv)
                print("✔ Xóa sinh viên thành công!\n")
                return

        print("❌ Không tìm thấy sinh viên!\n")