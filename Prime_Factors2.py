n = int(input("Enter a number: "))
prime_factors = []
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        prime_factors.append(i)
        if i != n//i:
            prime_factors.append(n//i)
prime_factors.sort()

print(f"Prime Factors of {n} are {prime_factors}")

# eg n = 36
# root n = 6
# 
# we need to check only to 1 to 6
# 
# 1 ---- 36/1 = 36 
# 2 ---- 36/2 = 18
# 3 ---- 36/3 = 12
# 4 ---- 36/4 = 9
# 6 ---- 36/6 = 6 (exclude)