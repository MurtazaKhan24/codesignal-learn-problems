def insert_position(nums, target):
    left, right = 0, len(nums) - 1
    if nums[left] > target:
        return 0
    if nums[right] < target:
        return right + 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else: 
            return mid
    return left
        

print(insert_position([1, 2, 3, 3, 5], 3))  # Expected output: 2
print(insert_position([1, 2, 3, 3, 5], 4))  # Expected output: 4
print(insert_position([1, 3, 5, 7, 9], 10)) # Expected output: 5