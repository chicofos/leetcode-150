def isAnagram(s, t): 
    
    #--------------------------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    #--------------------------------------------------
    
    if len(s) != len(t):
        return False
    
    words = {}
    
    for n in s:
       words[n] = words.get(n, 0) + 1
    
    for x in t:
        if x in words and words[x] > 0:
            words[x] -= 1
        else: 
            return False
        
    return True
            
print(isAnagram('anagram','nagaram')) # True
print(isAnagram('aacc','ccac')) # False
print(isAnagram('aacc','ccac')) # False