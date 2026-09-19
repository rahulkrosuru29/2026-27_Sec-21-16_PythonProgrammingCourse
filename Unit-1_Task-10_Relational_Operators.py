#Membership operators
#IN 
a = [10, 20, 30, 40, 50]
result = 30 in a
print("result of 30 in a is:",result)

b = {100, 200, 300, 400, 500}
result = 600 in b
print("result of 600 in b is:",result)

#NOT IN
c = ["Rahul", 500, "Diva", 700, 800]
result = "RahulNRI" not in c
print("result of 'RahulNRI' not in c is:",result)

d = {"Brand": "Toyota", "year": 2000, "model": 3000,}
result = "model" not in d
print("result of 'model' not in d is:",result) 
