#Determining a prime number
Number = int(input("Enter a number: "))
if Number > 1:
    for i in range(2, int(Number**0.5) + 1):
        if Number % i == 0:
            print(f"{Number} is a composite number (not a prime number).")
            break
    else:
        print(f"{Number} is a prime number.") 