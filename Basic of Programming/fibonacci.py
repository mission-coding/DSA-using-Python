def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n-1) + fibo(n-2)

n = int(input("Enter a number: "))
print(f"The {n}th term of Fibonacci series is  {fibo(n)}")