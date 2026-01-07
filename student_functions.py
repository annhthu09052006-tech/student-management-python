import json
import os


# Helper functions to load and save data from JSON files
def load_students():
    file_path = 'students.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def load_accounts():
    file_path = 'accounts.json'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_accounts(accounts):
    file_path = 'accounts.json'
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(accounts, f, indent=4)


# Function to view personal information (only own data)
def view_personal_info(student_id):
    students = load_students()
    for student in students:
        if student.get('id') == student_id:
            print("\nPersonal Information:")
            print(f"ID: {student.get('id', 'N/A')}")
            print(f"Name: {student.get('name', 'N/A')}")
            print(f"Age: {student.get('age', 'N/A')}")
            # Add more fields if available in students.json
            return
    print("Student information not found.")


# Function to view average score (only own data)
def view_average_score(student_id):
    students = load_students()
    for student in students:
        if student.get('id') == student_id:
            scores = student.get('scores', [])
            if scores:
                average = sum(scores) / len(scores)
                print(f"\nAverage Score: {average:.2f}")
            else:
                print("\nNo scores available.")
            return
    print("Student information not found.")


# Function to change password (only own account)
def change_password(username, new_password):
    accounts = load_accounts()
    for account in accounts:
        if account.get('username') == username:
            account['password'] = new_password  # Note: In production, hash the password
            save_accounts(accounts)
            print("\nPassword changed successfully.")
            return
    print("Account not found.")


# Student menu after login
def student_menu(username, student_id):
    while True:
        print("\nStudent Portal Menu:")
        print("1. View Personal Information")
        print("2. View Average Score")
        print("3. Change Password")
        print("4. Logout")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            view_personal_info(student_id)
        elif choice == '2':
            view_average_score(student_id)
        elif choice == '3':
            new_password = input("Enter new password: ").strip()
            change_password(username, new_password)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")


# Main entry point for testing (can be integrated into main.py by calling student_menu after login)
if __name__ == "__main__":
    # Simple login for demonstration (in real integration, use auth.py for login)
    print("Student Login")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    accounts = load_accounts()
    logged_in = False
    student_id = None
    for account in accounts:
        if (account.get('username') == username and
                account.get('password') == password and
                account.get('role') == 'student'):
            student_id = account.get('student_id')
            logged_in = True
            break

    if logged_in and student_id:
        student_menu(username, student_id)
    else:
        print("Invalid login credentials or not a student account.")
