a=int(input("enter the number to check"))
sum=0
for i in range(1,a):
   if a%i==0:
     sum=sum+i
  
if sum==a:
 
    print("number is perfect")
      
else:
          
      print("not perfect")
