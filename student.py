class Student:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def display(self):
        print(f"Mã SV: {self.student_id}")
        print(f"Họ tên: {self.name}")
        print(f"Tuổi: {self.age}")
        print(f"Ngành: {self.major}")
        print("-------------------------")