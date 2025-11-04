# Taking input from user

name = input("Enter your name: ") # by default string input
print("Welcome " , name)

# If we want integer input
age = int(input("enter your age : ")) # converting string input to integer
print("Your Age is:" , age)

# If we want float input
marks = float(input("enter your marks : ")) # converting string input to float
print("marks is:" , marks)

# If we want boolean input
old = input("Are you old? (True/False): ")
old = old == 'True'  # converting string input to boolean
print("Old Status is:" , old)
