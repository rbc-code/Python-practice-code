x=int(input("enter number"))
y=x%10
y1=y%10
y2=y1%10
a=y*y*y
b=y1*y1*y1
c=y2*y2*y2
sum=a+b+c
if x==sum:
    print("Arm")
else:
    print("NOT Arm")
        

