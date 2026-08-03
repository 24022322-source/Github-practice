def validPalindrome(s):
    n = len(s)
    
    left = 0
    right = n - 1
    
    count = 0
    while(left <= right):
        if(s[left] == s[right]):
            left += 1
            right -= 1
        elif(s[left] != s[right]):
            count += 1
            right -= 1
    
    if(count >= 2):
        count = 0
        left = 0
        right = n - 1
        while(left <= right):
            if(s[left] == s[right]):
                left += 1
                right -= 1
            elif(s[left] != s[right]):
                count += 1
                left += 1
        
        if(count >= 2):
            return False
        else:
            return True
    else:
        return True
    
s = "abkkiba"
print(validPalindrome(s))