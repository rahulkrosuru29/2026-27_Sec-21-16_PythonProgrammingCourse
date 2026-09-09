#Simple interest calculator
principle = int(input("Enter the principle amount: "))
time = float(input("Enter the time in years: "))
rate = float(input("Enter the rate of interest: "))
ptr = (principle*time*rate) / 100
print("The simple interest: ", ptr)