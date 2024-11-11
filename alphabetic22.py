name=[]
n=int(input("Enter the no of string:"))
for i in range(1,n+1):
	print("Enter name:",i)
	item=str(input())
	name.append(item)
	name.sort()
	print("alphabetical order:",name)
