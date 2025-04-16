def wordPattern(pattern, s):
    
    #--------------------------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    #--------------------------------------------------
    
    i = 0
    sList = s.split()
    values = {}
    keys = {}
    
    if len(sList) != len(pattern):
        return False
    
    for n in pattern:
        if n not in keys and sList[i] not in values:
            keys[n] = sList[i]
            values[sList[i]] = True
        else:
            if keys.get(n) != sList[i]:
                return False
        i += 1
    return True
    


print(wordPattern("abba", "dog cat cat dog"))