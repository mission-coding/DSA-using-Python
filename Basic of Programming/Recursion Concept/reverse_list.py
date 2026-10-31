'''Question: Reverse a list using recursion'''

l = [5,7,3,2,6,1,5,9,0]

# using loop
# for i in range(len(l)//2):
#     l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]
# print(l)

def reverse(l, i = 0):
    if i>len(l)//2:
        return l
    
    l[i], l[len(l)-1-i] = l[len(l)-1-i], l[i]
    return reverse(l, i+1)

print(reverse(l))