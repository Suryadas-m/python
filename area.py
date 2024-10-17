a=int(input("enter the side a="))
b=int(input("enter the side b="))
c=int(input("enter the side c="))
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c)*0.5)
print("area of triangle=",a)
