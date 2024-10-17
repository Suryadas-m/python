value=int(input("Enter the number:"))
num=2
count=0
print("First",value,"prime numbers are:")
while count < num:
    # define a flag variable
    prime_flag = True
     
    for i in range(2,value):
        if (n % i) == 0:
            prime_flag = False
            break
     
    # check if flag is True
    if prime_flag:
        print(n, end =" ")
        count = count + 1
    n = n + 1
     


