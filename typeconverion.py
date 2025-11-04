#type conversion in python
a = 10
b = 20.5
print("Value of sum: " , a + b)  #here a is converted to float type(to superior) which is by default



#type casting (here we forcefully convert one type to another type)
a = int("10") #here a is converted str to integer type
b = 20.5
print("Value of sum: " , a + b) 

a = float(10) #here a is converted int to float type
b = 20.5
print("Value of sum: " , a + b)

a = str(10) #here a is converted int to string type
print("Type of a: " , type(a))

