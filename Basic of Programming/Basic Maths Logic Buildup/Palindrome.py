n = int(input("Enter a Number: "))
num = n
reversed_n = 0

while num > 0:
    last_digit = num % 10
    reversed_n = (reversed_n*10)+last_digit
    num //= 10

if n == reversed_n:
    print("The Number is Palindrome")
else:
    print("The Number is not Palindrome")
