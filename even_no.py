# n=int(input("Enter No."))
# i=1
# while i<=n:
#     if n%2==0:
#         if i%2==0:
#            if i<=(n-2):
#                print(i,end=',')
#            else:
#                print(i)   
#     else:
#         if i%2!=0:
#             if i<=(n-2):
#                 print(i,end=',')
#             else:
#                 print(i)               

#     i=i+1         
#===============================================================

# n=int(input("Enter No."))
# i=1
# while i<=n:
#     if i%2==0:
#         if i<=(n-2):
#             print(i,end=",")
#         else:
#             print(i)
#     i=i+1            

#=====================================================================

# n=int(input("Enter No."))
# i=1
# while i<=n:
#     if i!=2:
#         if i<=(n-2):
#             print(i,end=",")
#         else:
#             print(i)
#     i=i+1   

#============================================================================

# n=int(input("Enter No."))
# i=1
# sum=0
# while i<=n:
#     if i!=2:
#         sum=sum+i
#         if i<=(n-2):
#             print(i,end="+")
#         else:
#             print(i,end='=')
#     i=i+1 
# print(sum)

#===============================================================================

n=int(input("Enter No."))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
        if i<=(n-2):
            print(i,end=" + ")
        else:
            print(i,end='=')
    i=i+1  
print(sum)    