# #           0           1    
# lis =[["ajay","rb"],(67,99)]        #list.....
# #        0      1     0  1

# print(type(lis[1]))
# # lis[1][0]=99   #error (tuple)
# # lis.pop()
# # print(lis)

t = (56,857,[5,8,90])
print(t)
t[2][1]=888
print(t)

lis = [["raja","rb"],(56,90,[65,99])]
print(lis)

lis[1][2][1]=777
print(lis)

# len() , max(), min(), sum(), index(),count()

r = (5,6,8,9,2,1)

a=r.count(1)
print(a)

b = (5,6,8,9,2,1)

c=sorted(b)
print(a)

