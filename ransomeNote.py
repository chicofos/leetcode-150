def canConstruct(ransomNote, magazine):
    
    # ---------------------------------------
    #   Time Complexity: O(m + n)
    #   Time Complexity: O(m)
    # ---------------------------------------
    
    mTable = {}
    
    for m in magazine:
        if m in mTable:
            mTable[m] = mTable[m] + 1
        else:
            mTable[m] = 1
    
    for n in ransomNote:
        if n in mTable and mTable[n] > 0:
            mTable[n] = mTable[n] - 1
        else:
            return False
    return True
    

print(canConstruct('a','b')) # False
print(canConstruct('aa','ab')) # False
print(canConstruct('aa','aab')) # True