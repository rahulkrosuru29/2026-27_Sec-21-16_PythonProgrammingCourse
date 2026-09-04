#Identity Operators EXE
#IS OPERATOR
a = [10, 20, 30]
b=a
result = b is a
print("result of ",b,"is",a,"is:",result) 

c = [100, 200, 300]
d = [100, 200, 300]
result = c is d 
print("result of ",c,"is",d,"is:",result)

#IS NOT OPERATOR
e = [400, 500, 600]
f = [400, 500, 600]
result = e is not f
print("result of ",e,"is not",f,"is:",result)

g = [700, 800, 900]
h = g
result = g is not h
print("result of ",g,"is not",h,"is:",result)