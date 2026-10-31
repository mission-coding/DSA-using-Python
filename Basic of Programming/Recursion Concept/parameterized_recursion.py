''' Question: find sum of n natural number using parammeterized recursion'''

def sum_of_n(n, i=1, sum=0):
    if i > n:
        print(sum)
        return
    sum_of_n(n, i+1, sum+i)

sum_of_n(5)

# Recursion tree
# sum_of_n(5,1,0)
# sum_of_n(5,2,1)
# sum_of_n(5,3,3)
# sum_of_n(5,4,6)
# sum_of_n(5,5,10)
# sum_of_n(5,6,15)
