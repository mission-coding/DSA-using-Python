n = int(input('Enter a number: '))

prime_factors = []

for i in range(1, n//2 + 1):
    if n % i == 0:
        prime_factors.append(i)

prime_factors.append(n)
print("The Prime Factors of", n,"are")

for i in prime_factors:
    print(i, end = " ")
