from functools import reduce
# x= lambda a,b,c,d,e,f: a+b/c-d*e+f
# print(x(33,2,77,1,8,44))

# #.....................................................................

# a= lambda r: r**2
# print(a(4))

# #.....................................................................

# my_list=[10,34,67,33,98,40,50,88,39]

# x= list(filter(lambda x: x%2==0, my_list))
# print("Even no=",x)

# #.....................................................................

# # Rb_list=[10,34,67,33,98,40,50,88,39]

# y=reduce(lambda x,y: x+y, x)
# print(y)

# #.....................................................................
# Rb_list=[10,34,67,33,98,40,50,88,39]
# even_data=filter(lambda x: x%2==0, Rb_list)
# squer_even=list(map(lambda x: x**2,even_data))
# squer_sum= reduce(lambda x,y: x+y, squer_even)

# print(even_data)
# print(squer_even)
# print(squer_sum)

#.......................................................................

Rbc_list=[10,34,67,33,98,40,50,88]
even_data=filter(lambda x: x%2==0, Rbc_list)
squer_sum= reduce(lambda x,y: x+y, even_data)
# squer_even=lambda x: x**2,squer_sum
squer_even = squer_sum**2

print(even_data)
print(squer_even)
print(squer_sum)