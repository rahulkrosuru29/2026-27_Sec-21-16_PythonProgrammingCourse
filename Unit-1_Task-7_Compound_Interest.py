# compound interest
p = int(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))   
n = float(input("Enter the number of times interest is compounded per year: "))
ci = p*(1 + r/n)**(n*t)
print(ci)
