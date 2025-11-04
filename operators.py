# Operators
# Arithmetic Operations in Python
print("Arithmetic Operators:")
a = 10
b = 20
add = a + b 
sub = b - a 
mul = a * b
div = b / a
mod = b % a
exp = a ** 2
print (add , sub , mul , div , mod , exp)
# Another way to do the same
a = 10
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**2)




#relations and comparision operators
print("Relational and Comparison Operators:")
a = 10
b = 20
print("equal to: " , a==b)  #false (equal to)
print("not equal to: " , a!=b)  #true  (not equal to)
print("greater than:" , a>b)   #false (greater than)
print("less than:" , a<b)   #true (less than)
print("greater than equal to:" , a>=b)  #false (greater than equal to)
print("less than equal to:" , a<=b)  #true (less than equal to)




#assignment operators
print("Assignment Operators:")
num = 20
num = num + 10
num += 10  #same as num = num + 10
print("num : " , num)

num = num - 10
num -= 10  #same as num = num - 10
print("num : " , num)

num = num * 2
num *= 2  #same as num = num * 2
print("num : " , num)

num = num / 2
num /= 2  #same as num = num / 2
print("num : " , num)

num = num % 3
num %= 3  #same as num = num % 3
print("num : " , num)




#logical operators
print("Logical Operators:")
print ("Val for NOT:" , not True)  #false
print ("Val for NOT:",not False) #true

a = 20
b = 10
print("Op NOT:",not (a > b))  #false
print("Op NOT:",not (a < b))  #true

val1 = True 
val2 = True
print ("Op AND:",val1 and val2)  #true
print ("Op OR:",val1 or val2)   #true

val1 = True 
val2 = False
print ("Op AND:",val1 and val2)  #false
print ("Op OR:", (a==b) or (a>b)) #true (using expressions)
