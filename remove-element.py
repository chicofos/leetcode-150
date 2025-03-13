# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

def removeElement(nums, val):
    p1 = 0
    p2 = len(nums) -1 
    k = 0
    
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    while(len(nums) > 0 and p1 <= p2):
        if nums[p1] is val:
            if nums[p2] is val:
                p2 -= 1
            else:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                k += 1
                p1 += 1
        else:
            p1 += 1
            k+= 1
    return k
  
print(removeElement([2], 3))