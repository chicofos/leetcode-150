def isHappy(num):
    
    #--------------------------------------------------
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    #--------------------------------------------------
    
    table = {}
    
    while(num != 1 and num not in table):
        table[num] = True
        num = sum(int(digit) ** 2 for digit in str(num))
        
    return num == 1
    
print(isHappy(19))   # True
print(isHappy(2)) # False