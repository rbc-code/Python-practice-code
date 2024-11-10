# tuple
#0) it is a container , which store multiple data objects.
#1) it is a sequence date type .(order data type)
#2) it is a imnutable data type. 
#3) (a) representation ()
#   (b) comma seperated
#4) it is faster the list,
#5) single element represntation.
#6) generallu whenever data is fetched from database it is stored in the form of tuple or dictionary.
 

fruit =("Apple",20,100)

print(type(fruit))
# fruit[2]=200 # tuple imnutable
print(id(fruit))
print(id(fruit[0]),id(fruit[1]),id(fruit[2]))

fruit = ("Apple",20,100) + ("Mango",50)
print(fruit)

number = (34,45) + (64,89)
number = number + (56,98)

print(number)

# Note--> 
