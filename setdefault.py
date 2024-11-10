# setdefalut()
# 1) key available -- return existing value
# 2) ket not available -- key value pair add,
# return added value

data={'1':454, '2':654, '3':234}  #value return krta hai..

data.setdefault('11',999)
print(data)

value=data.setdefault('1',9890)
print(data)
print(value)