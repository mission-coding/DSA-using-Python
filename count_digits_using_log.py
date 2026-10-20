from math import log
n = 342174

# Number of Digits = int(log(n) + 1)

digits = int(log(n,10) + 1)

print("Number of digits in", n, ":", digits)