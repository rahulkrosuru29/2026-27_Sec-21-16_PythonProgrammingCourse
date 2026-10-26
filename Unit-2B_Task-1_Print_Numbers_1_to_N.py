#printing numbers from 1 to N using for loop
limit = int(input("Enter the value of N: "))
for current_number in range(1, limit + 1):
    print(current_number)

#printing numbers from 1 to N using while loop
limit = int(input("Enter the value of N: "))    
current_number = 1
while current_number <= limit:
    print(current_number)
    current_number += 1