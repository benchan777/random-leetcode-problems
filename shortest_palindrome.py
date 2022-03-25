def shortestPalindrome(s):
    # bccd -> dccbccd
    # babad -> dababad
    
    longestPalindrome = 0
    longestLeft = 0
    longestRight = 0
    
    for i in range(len(s)):
      left, right = i, i
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
      
      left += 1
      right -= 1
      
      if right - left + 1 >= longestPalindrome and left == 0:
        longestPalindrome = right - left + 1
        longestLeft = left
        longestRight = right

      left, right = i, i + 1
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
      
      left += 1
      right -= 1
      
      if right - left + 1 >= longestPalindrome and left == 0:
        longestPalindrome = right - left + 1
        longestLeft = left
        longestRight = right
    
    # charToAdd = s[longestRight + 1:len(s)][::-1]
    # newPalindrome = charToAdd + s

    char = ''
    for i in range(len(s) - 1, 0, -1):
      char += s[i]


    return char + s


print(shortestPalindrome('abcd'))