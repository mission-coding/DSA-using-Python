n = int(input("Enter a number: "))
num = n

count = 0
while num > 0:
    last_digit = num % 10
    num = num // 10
    count += 1
num = n

sum = 0
while num > 0:
    last_digit = num % 10
    sum += last_digit**count
    num = num // 10

if sum == n:
    print("The Number is an Armstrong Number")
else:
    print("The Number is not an Armstrong Number")