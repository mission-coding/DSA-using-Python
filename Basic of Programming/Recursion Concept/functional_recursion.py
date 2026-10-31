''' Question: find sum of n natural number using functional recursion'''

def sum_of_n(n):
    if n == 1:
        return 1
    return n + sum_of_n(n-1)

print(sum_of_n(5))

# Recursion tree
# 5 + sum_of_n(4)
# 5 + 4 + sum_of_n(3)
# 5 + 4 + 3 + sum_of_n(2)
# 5 + 4 + 3 + 2 + sum_of_n(1)
# 5 + 4 + 3 + 2 + 1 = 15
