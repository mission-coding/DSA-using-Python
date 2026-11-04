'''Question: Sort the list using selection sort'''

nums = [4, 1, 3, 9, 7]

min_index = 0

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[min_index] > nums[j]:
            min_index = j
    
    nums[min_index], nums[i] = nums[i], nums[min_index]

print(nums)

