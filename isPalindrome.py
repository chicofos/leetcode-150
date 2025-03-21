def isPalindrome(s):
    # ---------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # ---------------------------------
        
    text = ''.join(c for c in s if c.isalnum()).lower()
    text_list = list(text)
    p1 = 0
    p2 = len(text_list) -1
    
    while p1 < p2:
        if text_list[p1] != text_list[p2]:
            return False
        p1 += 1
        p2 -= 1
        
    return True
       
print(isPalindrome('A man, a plan, a canal: Panama'))