lis=["Rb","chauhan","Python","Java"]
print(lis)

a=lis.append("xyz")
print(a)  

deleted_v=lis.pop(2)       #pop........ index value deni hai....
print(lis)
 
print(deleted_v)

# a=lis.append("xyz")
# print(a)            #None

lis.remove("Rb")             #remove...........  ek time m ek data hi remove hota hai(data value dena hai...)
print(lis)



lis.clear()
print(lis)                       #clear........... sara data delet krne ke liye.......



lis1=["Rb","chauhan","Python","Java"]

print(lis1)
del lis1                   #del.............. refrence ke satha sara data delet kr deta hai..
print(lis1)