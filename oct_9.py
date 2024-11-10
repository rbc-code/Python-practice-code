#Note: dot(period) opreator (methods)

# functions without using any dot opreator



#index() return index value of element passed, we can give maximim of 
# 3 parameter in index() in first parameter, u have to pass the element
# itself,
# and second and thrid are optionl parameter,
# second--> start
# third--> end(excluded)
#if element is not found it throws an .........


num =[56,857,76,45,00,70,45,54,2,1,45,768]     # 0, 1, 2, 3, 4, 5, 6, 7, 8

# a=num.index(56,5,9) #error             #5...start   9.....end
# print(a)



a =num.index(45,0)
print(a)
b=num.index(00,a+1)
print(b)
c=num.index(45,b+1)
print(c)
d=num.index(45,c+1)
print(d)
e=num.index(768,d+1)
print(e)


# count() --> return frequency.........
         

num1 =[56,857,76,45,00,70,45,54,2,1,45,768]
o=num1.count(45)
print(o)          


# sort()...... None return,, inplace function,,, no need of extra list(object).......

num2 =[56,857,76,45,00,70,45,54,2,1,45,768]
num2.sort()
print(num2)

num3 =[56,857,76,45,00,70,45,54,2,1,45,768]
num3.sort(reverse=True)
print(num3)


