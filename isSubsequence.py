def isSubsequence(s, t):
    
    # ---------------------------------------
    #   Time Complexity: O(s + t)
    #   Space Complexity: O(s + t)
    # ---------------------------------------
    
    # p1, p2 = 0, 0
    # sec,text = list(s), list(t)
    
    # while(p1 <= len(sec) - 1 and p2 <= len(text) - 1):
    #     if sec[p1] == text[p2]:
    #         p1 += 1
    #         p2 += 1
    #     else:
    #         p2 += 1
    
    # return p1 == len(sec)

    # ---------------------------------------
    #   Time Complexity: O(n)
    #   Time Complexity: O(1)
    # ---------------------------------------
    
    p1, p2 = 0, 0

    while p1 < len(s) and p2 < len(t):
        if s[p1] == t[p2]:
            p1 += 1
        p2 += 1

    return p1 >= len(s)

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t)) # True

s = "dg"
t = "ahbgdc"
print(isSubsequence(s,t)) # False