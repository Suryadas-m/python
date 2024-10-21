def factorial(n):
     if n == 0 or n == 1:
         return 1
     result = factorial(n - 1)
     return n * result

number = int(input("Enter a number to find its factorial: "))
print("The factorial of", number, "is:", factorial(number))  
