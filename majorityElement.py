def majorityElement(nums):
    #--------------------------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    #--------------------------------------------------
    
    # elements = {}
    # for i in nums:
    #     if i in elements:
    #         elements[i] += 1
    #     else:
    #         elements[i] = 1
            
    # return max(elements, key=elements.get)
    
    #--------------------------------------------------
    # Boyer-Moore Voting Algorithm
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    #--------------------------------------------------
    
    count = 0
    candidate = None
    
    for i in nums:
        if count == 0:
            candidate = i
       
        if candidate == i:
            count += 1
        else:
            count -= 1
                
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None
    

print(majorityElement([1,3,2,3,3]))