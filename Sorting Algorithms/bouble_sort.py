# Bouble sort --> Adjecent swiping
nums = [5,8,1,6,9,2,4]

# Average Method:
# for i in range(0, len(nums)):
#     for j in range(0, len(nums)-1-i):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
#     # print(nums)
# print(nums)

# Time Complexity:
    # Average or Worst Case: O(n(n+1)/2) ~ O(n^2)
    # Best Case (already sorted): O(n(n+1)/2) ~ O(n^2)
# Space Complexity = O(1)

# Best Method:
for i in range(0, len(nums)):
    is_swap = False
    for j in range(0, len(nums)-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            is_swap = True
    if is_swap == False:
        break
print(nums)

# Time Complexity:
    # Average or Worst Case: O(n(n+1)/2) ~ O(n^2)
    # Best Case (already sorted): O(n)

# Space Complexity = O(1)