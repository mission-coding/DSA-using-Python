'''Question: Check if a string is a Palindrome'''

'''Using Loop (otimal)'''
def check_palindrome(s):
    i = 0
    while i <= len(s)//2:
        if s[i] != s[len(s)-1-i]:
            return False
        else:
            i += 1
    return True

'''Using Recursion'''
# def check_palindrome(s, i=0):
#     if i>=len(s)//2:
#         return True
#     if s[i] != s[len(s)-1-i]:
#         return False
#     return check_palindrome(s,i+1)

s = input("Enter a string: ")

if check_palindrome(s):
    print(f"{s} is a Palindrome")
else:
    print(f"{s} is not a Palindrome")






