# Operator Precedence and Associativity
a = int(input("Enter the value of (a) :"))
b = int(input("Enter the value of (b) :"))
c = int(input("Enter the value of (c) :"))

# Precedence
result1 = a + b * c
print("a + b * c =", result1)

# Associativity
result2 = a - b - c
print("a - b - c =", result2)

# Using brackets
result3 = (a + b) * c
print("(a + b) * c =", result3)
