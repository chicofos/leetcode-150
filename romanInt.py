def romanInt(s):
        
    # ---------------------------------
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ---------------------------------
        
    # count = 0
    # i = 0
    # length = len(s) - 1
    
    # while i <= length:
        
    #     if s[i] == 'M':
    #        count += 1000
    #     if s[i] == 'D':
    #         count += 500
    #     if s[i] == 'L':
    #         count += 50
    #     if s[i] == 'V':
    #         count += 5
        
    #     if s[i] == 'C':
    #         if i+1 <= length and (s[i+1] == 'M' or s[i+1] == 'D'):
    #             if s[i+1] == 'M':
    #                 count += 900
    #             if s[i+1] == 'D':
    #                 count += 400

    #             i += 1
    #         else:
    #             count += 100

    #     if s[i] == 'X':
    #         if i+1 <= length and (s[i+1] == 'L' or s[i+1] == 'C'):
    #             if s[i+1] == 'L':
    #                 count += 40
    #             if s[i+1] == 'C':
    #                 count += 90
    #             i += 1
    #         else:
    #             count += 10
            
    #     if s[i] == 'I':
    #         if i+1 <= length and (s[i+1] == 'V' or s[i+1] == 'X'):
    #             if s[i+1] == 'V':
    #                 count += 4
    #             if s[i+1] == 'X':
    #                 count += 9
    #             i += 1
    #         else:
    #             count += 1
                
    #     i+= 1
    
    # return count
        
    # ---------------------------------
    # Simplified and Improved version
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # ---------------------------------
        
    roman_values = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total
    
    
print(romanInt("MCMXCIV")) # 1994
print(romanInt("III")) # 3
print(romanInt("MCMLVIIIXCIV")) # 58