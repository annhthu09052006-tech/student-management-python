# search_student.py

# Danh sách sinh viên mẫu
students = [
    {"id": 1, "name": "Nguyễn Văn An", "class": "CNTT1"},
    {"id": 2, "name": "Trần Thị Bình", "class": "CNTT2"},
    {"id": 3, "name": "Lê Văn Cường", "class": "KTPM1"},
    {"id": 4, "name": "Phạm Thị Dung", "class": "CNTT1"},
    {"id": 5, "name": "Hoàng Văn Em", "class": "HTTT"},
    {"id": 6, "name": "nguyễn thị hoa", "class": "CNTT3"},  # chữ thường để test sau
]

print("=== TÌM KIẾM SINH VIÊN THEO TÊN ===")
search_name = input("Nhập tên sinh viên cần tìm: ")


print("\nDanh sách tất cả sinh viên:")
for student in students:
    print(f"{student['id']}. {student['name']} - Lớp: {student['class']}")


matching_students = []
for student in students:
    if search_name in student['name']:
        matching_students.append(student)

print("\nKết quả tìm kiếm:")
for student in matching_students:
    print(f"{student['id']}. {student['name']} - Lớp: {student['class']}")