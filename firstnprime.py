
from math import sqrt
num = int(input("Enter a number: "))
count = 0
n = 2
 
print("First", num, "prime numbers are: ")
     while count < num:
     
    # define a flag variable
       prime_flag = True
   
     
    for i in range(2, int(sqrt(n)) + 1):
        if (n % i) == 0:
            prime_flag = False
            break
     
    # check if flag is True
    if prime_flag:
        print(n, end =" ")
        count = count + 1
    n = n + 1
