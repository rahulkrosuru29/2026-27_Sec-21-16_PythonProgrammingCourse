# count digits in a number
num = int(input("Enter a number: "))
orig_num = num
count = 0
while num > 0:
    num = num // 10
    count = count + 1
print(f"Number of digits in {orig_num} is: {count}")