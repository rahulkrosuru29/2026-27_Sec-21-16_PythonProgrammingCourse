# python logical operators exe
#AND operator
a = 5
result = a > 2 and a < 10
print("Result of,", a, "> 2  and", a, "< 10:", result) 
a = 20
result = a > 2 and a < 10
print("Result of,", a, "> 2  and", a, "< 10:", result) 
#OR operator
a = 5
result = a > 2 or a < 10
print("Result of,", a, "> 2  or", a, "< 10:", result)
a = 20  
result = a > 122 or a < 5
print("Result of,", a, "> 2  or", a, "< 225:", result)
#Not operator
a = 25
result = not(a > 2 and a < 10)
print("Result of not(", a, "> 2  and", a, "< 10):", result)
a = 20
result = not(a > 10 and a < 40)
print("Result of not(", a, "> 10  and", a, "< 40):", result)
