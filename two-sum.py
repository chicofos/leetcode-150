def twoSum(nums, target):
    
    #--------------------------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    #--------------------------------------------------
    
    indexes = {}

    for i, num in enumerate(nums):
        x = target - num
        if x in indexes:
            return [indexes[x], i]
        else:
            indexes[num] = i

    return None


print(twoSum([3,1,5,7,2], 5)) # [0,1]
print(twoSum([3,2,4], 6)) # [1,2]
print(twoSum([3,3], 6)) # [0,1]