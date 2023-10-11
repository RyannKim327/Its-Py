from code_challenge1_external import *
import getpass

students= []
librarians = []
books = []

def start():
	choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	_a_ = ["1", "2", "3"]

	while not choice in _a_:
		choice = input("Login as:\n[1] Student\n[2] Librarian\n[3] Exit\nEnter your choice: ")
	
	match choice:
		case "1":
			id = len(students) + 1
			name = input("Enter your name: ")
			student = Student({
				"ID": id,
				"studentName": name
			})

			print(f"Welcome to Library Mr/Ms. {student.getStudentName()}")
			if len(books) <= 0:
				print("There's no books yet.")
				return
			another_choice = input("Enter a book you want to borrow: ")

			students.append(student)

		case "2":
			id = len(librarians) + 1
			name = input("Enter your name: ")
			password = getpass.getpass("Enter your password: ")
			password1 = getpass.getpass("Verify your password: ")
			while password == password1:
				password = getpass.getpass("Enter your password: ")
				password1 = getpass.getpass("Verify your password: ")

			librarian = Librarian({
				"ID": id,
				"name": name,
				"password": password
			})

			librarians.append(librarian)

		case _:
			print("Thank you...")
			break

if __name__ == "__main__":
	start()