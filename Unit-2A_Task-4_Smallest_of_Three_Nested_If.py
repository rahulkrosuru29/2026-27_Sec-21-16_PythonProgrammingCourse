#Finding the smallest of three numbers using nested if statements   
x = int(input("Enter the first number : "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number : "))
if x <= y:
    if x <= z:
        smallest = x
    else:
        smallest = z
else:
    if y <= z:
        smallest = y
    else:
        smallest = z
print(f"The smallest number is {smallest} among {x}, {y}, and {z}.")