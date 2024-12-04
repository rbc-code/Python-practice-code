n=int(input("Enter Year :"))
if(n<=1000 and n>=9999 and n%4==0 and n%100!=0 and n%400==0):
    print(n,"=Is Leap Year")
else:
    print(n,"=Is Not Leap Year")    

