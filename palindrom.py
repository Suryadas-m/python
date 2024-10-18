def is_paliandrome(n):
	n_str=str(n)
	n_rev=n_str[::-1]
	if n_str==n_rev:
		return True
	else:
		return False
n=input("Enter a value\n")
result=is_paliandrome(n);
if result==True:
	print("The value is paliandrome")
else:
	print("The value is not paliandrome")
