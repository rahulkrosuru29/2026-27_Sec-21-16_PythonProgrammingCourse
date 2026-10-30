# Fibonacci series upto N terms
n = int(input("Enter the number of terms: "))
a = 0 # first term
b = 1 # second term
for i in range(n):
    print(a)
    nxt = a + b # next term
    a = b
    b = nxt