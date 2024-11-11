
students = {}
n = int(input("Enter the number of students: "))
for i in range(n):
    name = input("Enter student's name: ")
    age = int(input(f"Enter {name}'s age: "))
    grade = input(f"Enter {name}'s grade: ")
   
    students[name] = (age, grade)

print("\nStudent List:")
for student, details in students.items():
    age, grade = details
    print(f"Name: {student}, Age: {age}, Grade: {grade}")

