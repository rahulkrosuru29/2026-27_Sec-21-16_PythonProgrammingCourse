#Swapping of two numbers
#input
a = int(input("Enter the first number (a) :"))
b = int(input("Enter the second number (b) :"))
#process
a = a + b
b = a - b
a = a - b
#output
print(f"Before swapping a and b : {a} and {b}")
print(f"After swapping a and b : {a} and {b}")
