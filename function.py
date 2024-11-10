'''
#replace()  (old_value, new value,opt to chang value fill num)


s="we are here to learn c++, it is a high level lang"
print(s)
s1=s.replace("c++","Python")
print(s1)
s2=s.replace("high","low")
print(s2)
s3=s.replace(s,"new")
print(s3)

#split() --> return list ,  


r="we are here to learn c++, it is a to high level lang"

a=r.split()
print(a)
b=r.split('i')
print(b)
c=r.split('to',2)
print(c)


#join() -->return string

lis =["apple","banan","mango","orange"]   #sari value string honi chahiye... ,8987..error
lis2=["fruits","group"]
tup=("hii","hlw")
r1="".join(lis)
print(r1)

r2=" ".join(lis)
print(r2)

r3=",".join(lis)
print(r3)

r4="|".join(lis)+" "+" ".join(lis2)
print(r4)

r5=" ".join(tup)+" "+" ".join(tup)
print(r5)

'''


s="its now or never"

s=s.split()
print(s)
a=s[0][::-1]
b=s[1][::-1]
c=s[2][::-1]
d=s[3][::-1]

s=[a,b,c,d]
print(s)

