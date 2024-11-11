
"""Student={}
n=int(input("enter the number of students:"))

for i in range(n):
	name=input("NAME:")
	age=int(input("AGE:"))
	grade=input("GRADE:")
	Student[name]=age,grade
print (Student)

l=list(Student.items())
l.sort()
print("sorted items in ascending order",l)
l.sort(reverse=True)
print("sorted items in ascending order",l)
dict=dict(l)"""

Student = {}
n = int(input("Enter the number of students:"))

for i in range(n):
    name = input("NAME: ")
    age = int(input("AGE: "))
    grade = input("GRADE: ")
    Student[name] = (age, grade)

print("Original Student Dictionary:", Student)


sorted_by_keys_asc = dict(sorted(Student.items()))  
print("sorted by name(ascending, by name):",sorted_by_keys_asc)
sorted_by_keys_desc = dict(sorted(Student.items(), reverse=True))  
print("sorted by name(descending, by name):",sorted_by_keys_desc)


sorted_by_values_asc = dict(sorted(Student.items(), key=lambda item: item[1][0])) 
print("Sorted by values (ascending, by age):", sorted_by_values_asc)
sorted_by_values_desc = dict(sorted(Student.items(), key=lambda item: item[1][0], reverse=True))  
print("Sorted by values (descending, by age):", sorted_by_values_desc)

