# Question
# Find frequency of elements of list b in list a
# 0 < a[i] < 10

a = [5,3,2,2,1,5,5,7,5,10]
b = [10,11,1,9,5,67,2]

# Method 1
# freq = {}
# for i in b:
#     if i not in freq:
#         freq[i] = a.count(i)
# print(freq)

# Method 2

hashList = [0]*11
freq = {}
for i in a:
    hashList[i] += 1

for i in b:
    if i>10:
        freq[i] = 0
    else:
        freq[i] = hashList[i]

print(freq)

