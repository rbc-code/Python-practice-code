'''
conditional statement(decision making)(if-else)
control flow statement(looping)
'''
'''
age = int(input("Enter Age"))

if age>=18:
    print("Eligible")
else:
    print("Your are not eligible")    
'''

# print("main script") #simple
# if False: # complex
#     print("if body1")
#     print("if body2")
#     print("if body3")
#     print("if body4")
# else:
#     print("else 1") 
#     print("else 1")    

'''
1.
ch = input("Enter any character :")                  

if ch =='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("vowel")
else:
    {
        print("not")
    }
 '''

ch = input("Enter any character :")  
v="AEIOUaeiou"                

if ch[0] in v:               # if in v 
    print("vowel")
else:
    {
        print("not")
    }

