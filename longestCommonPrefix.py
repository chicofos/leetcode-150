def longestCommonPrefix(strs):
    
    # ---------------------------------------
    #   Time Complexity: O(m * n)
    #   Space Complexity: O(n)
    #   this is not the best solution when strings are bigger
    # ---------------------------------------
    
    longestPrefix = ''
    i = 0
    match = True
    
    while (i < len(strs[0]) and match):
        letter = strs[0][i]
        for n in strs[1:]:
            if len(n) > i:
                if n[i] != letter:
                    match = False
            else:
                match = False
        if match == True:
            longestPrefix += letter
        i += 1
    
    return longestPrefix

    # ---------------------------------------
    #   ChatGPT Solution
    #   Time Complexity: O(n log n + m)
    #   Space Complexity: O(n)
    # ---------------------------------------
    
    # if not strs:
    #     return ""
    
    # strs.sort()  # Ordena lexicográficamente
    # first = strs[0]
    # last = strs[-1]
    
    # min_len = min(len(first), len(last))
    # prefix = []
    
    # for i in range(min_len):
    #     if first[i] == last[i]:
    #         prefix.append(first[i])
    #     else:
    #         break
    
    # return "".join(prefix)
    
    
print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["ab","a"]))