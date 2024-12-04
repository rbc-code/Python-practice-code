x=10  #global
def show():
    # global y, x #................
    y=20 
    x=40     #local
    print(x)
    print(y)
    print(globals()['x'])
show()
print(x) 
print(y)  
print(x) 