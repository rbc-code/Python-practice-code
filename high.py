x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
if(x==y==z):
    print(f"{x} All values are equal")
elif(x==y>z):
    print(f'{x} is greater and first-second value equal')    
elif(x==z>y):
    print(f'{x} is greater and first-third value equal')
elif(z==y>x):
    print(f'{z} is greater and second-third value equal')
elif(x==y<z):
    print(f'{z} is greater and first-second value equal')    
elif(x==z<y):
    print(f'{y} is greater and first-third value equal')
elif(z==y<x):
    print(f'{x} is greater and second-third value equal') 
elif(x>y and x>z):
    print(f'{x} is greater')
elif(y>x and y>z):
    print(f'{y} is greater')
elif(z>y and z>x):
    print(f'{z} is greater')    
else:
    print("Something Is Wrong...")    














# x=(input("Enter first number"))
# y=(input("Enter second number"))
# z=(input("Enter third number"))
# if(x>y and x>z):
#     print(f'{x}is Greater')
# else:
#     if(y>z and y>x):
#         print(f'{y}is Greater')
#     else:
#         print(f'{z}is Greater')    
# 
# x=(input("Enter first number"))
# y=(input("Enter second number"))
# z=(input("Enter third number"))
# if(x>y and x>z):
#     print(f'{x}is Greater')
# elif(y>z and y>x):
#     print(f'{y}is Greater')
# elif(z>x and z>y):
#     print(f'{z}is Greater')
# else:
#     print("wrong")

           




       