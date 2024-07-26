# Import necessary modules
import random
import string

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left_half = merge_sort(lst[:mid])
    right_half = merge_sort(lst[mid:])

    # Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    res = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            res.append(left[left_index])
            left_index += 1
        else:
            res.append(right[right_index])
            right_index += 1

    # If we reach the end of either array, append the leftover elements from the other array
    if left:
        res.extend(left[left_index:])
    if right:
        res.extend(right[right_index:])

    return res

# Generate a list of 20 random alphanumeric characters.
random_alphanumeric = [random.choice(string.ascii_letters + string.digits) for _ in range(20)]

print("Original List of random alphanumeric characters:\n", random_alphanumeric)

# Apply merge sort
sorted_alphanumeric = merge_sort(random_alphanumeric)

print("\nSorted List of alphanumeric characters:\n", sorted_alphanumeric)