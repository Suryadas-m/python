def fibonacci(n):
	if n==0 or n==1:
		return n;
	else:
		return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter an integer:"))
for i in range(n):
	print(fibonacci(i))
result=fibonacci(n-1)
print(f"The {n}th fibonacci number is: {result}")
