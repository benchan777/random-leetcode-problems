def longestPalindrome(s):
  current_longest_palindrome = ''
  prev = []
  
  for letter in s:
    if len(current_longest_palindrome) == 0:
      current_longest_palindrome = letter
      prev.append(letter)
      continue

    curr = []
    while prev:
      temp_str = prev.pop(0)
      temp_str += letter
      if temp_str == temp_str[::-1]:
        if len(temp_str) > len(current_longest_palindrome):
          current_longest_palindrome = temp_str
      curr.append(temp_str)
    curr.append(letter)
    prev = curr
      
  return current_longest_palindrome

def longestPalindrome2(s):
  longest_length = 0
  left_index, right_index = 0, 0

  # initialize 2d array
  matrix = []
  for i in range(len(s)):
    row = []
    for j in range(len(s)):
      row.append(0)
    matrix.append(row)

  # populate 2d array with boolean value based on palindrome status with 1 letter
  for i in range(len(s)):
    matrix[i][i] = 1
    longest_length = 1
    left_index, right_index = i, i
  
  # populate 2d array with boolean value based on palindrome status with 2 letters
  # for i in range(len(s) - 1):
  #   if s[i] == s[i + 1]: # is palindrome
  #     matrix[i][i + 1] = 1
  #     longest_length = 2
  #     left_index = i
  #     right_index = i + 1
  #   else: # is not palindrome
  #     matrix[i][i + 1] = 0

  # populate 2d array with boolean value based on palindrome status with 3 or more letters
  for i in range(len(s) - 1, -1, -1):
    for j in range(i + 1, len(s)):
      if j - i > 1:
        if s[i] == s[j]: # if both ends of the string equal, check if the string in between both ends is also a palindrome
          if matrix[i + 1][j - 1] == 1: # if string in between both ends is a palindrome, then this is a valid palindrome
            matrix[i][j] = 1    
            if (j + 1) - i > longest_length:
              longest_length = (j + 1) - i
              left_index ,right_index = i, j
          else: # if string in between both ends isn't a palindrome, then this is not a valid palidnrome
            matrix[i][j] = 0
        else: # both ends do not equal. valid palindrome is impossible
          matrix[i][j] = 0
      if j - i == 1:
        if s[i] == s[j]:
          matrix[i][j] = 1
          longest_length = 2
          left_index, right_index = i, i + 1
        else: # is not palindrome
          matrix[i][j] = 0

  print(s[left_index:right_index + 1])
  return s[left_index:right_index + 1]

# this one works
def longestPalindrome3(s):
  length = len(s)
  maxDiff = 0
  maxLeft, maxRight = 0, 0

  for i in range(length):
    # expand outwards from middle point until invalid palindrome is found (odd palindrome)
    left, right = i, i
    while left >= 0 and right < length and s[left] == s[right]:
      left -= 1
      right += 1
    
    # restore left/right pointers to position where last palindrome was found
    left += 1
    right -= 1

    if right - left >= maxDiff: # if distance between current two pointers > prev largest, replace pointers with curr left/right
      maxDiff = right - left
      maxLeft, maxRight = left, right

    # expand outwards from middle point until invalid palindrome is found (even palindrome)
    left, right = i, i + 1
    while left >= 0 and right < length and s[left] == s[right]:
      left -= 1
      right += 1
    
    # restore left/right pointers to position where last palindrome was found
    left += 1
    right -= 1

    if right - left >= maxDiff: # if distance between current two pointers > prev largest, replace pointers with curr left/right
      maxDiff = right - left
      maxLeft, maxRight = left, right

  print(s[maxLeft:maxRight + 1])
  return(s[maxLeft:maxRight + 1])

longestPalindrome3('racecar')
longestPalindrome3('aaa')
longestPalindrome3('babad')
longestPalindrome3('aaabbaaa')
longestPalindrome3("aacabdkacaa")