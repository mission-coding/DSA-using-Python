def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

n = int(input("Enter the value of n: "))
print("The factorial of", n, "is", factorial(n))

# Recursion tree
# 5 * sum_of_n(4)
# 5 * 4 * sum_of_n(3)
# 5 * 4 * 3 + sum_of_n(2)
# 5 * 4 * 3 * 2 * sum_of_n(1)
# 5 * 4 * 3 * 2 * 1 = 15