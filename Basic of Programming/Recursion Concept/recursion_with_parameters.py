''' Ques. print x, n times using recursion with parameter.'''

# def func(x, n):
#     if n == 0:
#         return

#     print(x)
#     func(x, n-1)

# func("Vivek", 4)


''' Ques. print 1 to n using  HEAD recursion with parameter.'''

# def func(n, i=1):
#     if i>n:
#         return
    
#     print(i)
#     func(n, i+1)

# func(10)

''' Ques. print n to 1 using HEAD recursion with parameter.'''

# def func(n):
#     if n == 0:
#         return 

#     print(n)
#     func(n-1)
# func(5)

''' Ques. print 1 to n using recursion TAIL with parameter.'''

def func(n):
    if n==0:
        return
    func(n-1)
    print(n, end=" ")

func(10)
