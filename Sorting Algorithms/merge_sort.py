'''Merge Sort - divide and merge'''

def merge_array(left,right):
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left_half = arr[:mid]
    right_half = arr[mid:]

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge_array(left,right)

arr = [3,1,5,4,8,7,9]
print(merge_sort(arr))

# Time Complexitiy - O(n log n)
# Space Comlexity - O(n)

# Recursive function that divides the array into halves until it reaches a base case of a single element, then merges the sorted halves back together.
