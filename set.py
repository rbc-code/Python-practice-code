#set
'''
    set is a container in which we contain multiple data, but duplication is not allowd,
    and it an unorderd data type,

    where our main concern is data , but not any orderd related to it , then we use set .


'''

a={1,3,9,9,7,2,5}
b={2,3,99,11,99,5}
c={2,33,7,"a","b"}

#r=a.union(b,c)
r=a|b|c
print(r)

#r=b.intersection(b)
r= a & b & c 
print(r)

#s=a.difference(b)
s=a-b
print(s)

#s1=a.difference(b,c)
s1=a-b-c
print(s1)


a1={3,4,7,6,4,11,18,5}
b1={44,23,65}

a1.update(b1)
print(a1)
a1.update((2,90,98))
print(a1)
a1.update([23,43,888888])
print(a1)
a1.update(("abcd"))
print(a1)


a1.add(999)       # list, tuple sabhi add ho sakte hai....
print(a1)
a1.add((756,))
print(a1)
a1.add(("abcf"))
print(a1)