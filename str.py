'''
string :
1   sequence (ordered)
2   immutable
'''



mes = "string is a immutable Data-type"

# mes[3]="y" ....  error
print(mes[22:26])

a=mes.capitalize()
print(a)

b=mes.upper()
print(b)

c=mes.lower()
print(c)

msg = "apple is"

d=msg.isupper()
print(d)

e=msg.islower()
print(e)

f=msg.isalpha()
print(f)           #appleis....true

g=msg.isdigit()
print(g)           #7565658.....true

# str2=[1,2,3,4,5,6,7,8,9,10]

# print(str2[1:11:1])
y=range(1,11,1)
print(tuple(y))

str3=[2,4,6,8,10]

x=range(2,11,2)
print(list(x))

x=range(10)
print(x)

# range(4,8,9,7,5,7,9,3)

x=range(10,5,-1)
print(list(x))