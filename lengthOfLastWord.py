def lengthOfLastWord(s):
    
    # ---------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ---------------------------------
        
    count = 0
    found = False
    i = len(s) - 1
    
    while not found and i >= 0:
        if s[i] != " ":
            count += 1
        else:
            if count > 0:
                found = True
        i -= 1
    
    return count
    
    
print(lengthOfLastWord("Hello World")) # 5    
print(lengthOfLastWord("a")) # 1
print(lengthOfLastWord("   fly me   to   the moon  ")) # 4