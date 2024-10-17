lowervalue=int(input("Enter the Lower value:"))
highervalue=int(input("Enter the Higher value:"))

for number in range(lowervalue,highervalue+1):
 if number>1:  
   for i in range (2,number):  
       if (number%i)==0:  
           break  
   else:  
        print(number)  

