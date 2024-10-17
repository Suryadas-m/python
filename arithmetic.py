a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("Which arithmetic operation want to perform")
print("1.Division\n2.Multiplication\n3.addition\n4.substraction\n5.floordivision\n6.moduls")
x=int(input("choose the operation:"))
if x==1:
        r=b/a
        print("div=",r)
elif x==2:
         r=a*b
         print("mul=",r)
elif x==3:
          r=a+b
          print("add=",r)
elif x==4:
          r=b-a
          print("sub=",r) 
elif x==5:
         r=a//b
         print("floor div=",r)    
elif x==6:
         r=a%b
         print("rem=",r)   
else: 
       print("Invalid input")                                   
          


