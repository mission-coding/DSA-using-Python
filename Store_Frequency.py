nums = [1,2,3,4,5,6,7,5,2,3,4,4,6,7,7,7,9,1,2,1,2]
freq = {}

for i in nums:
    if i not in freq:
        freq[i] = nums.count(i)

print(freq)