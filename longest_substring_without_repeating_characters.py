def lengthOfLongestSubstring(s):
  left = 0
  right = 0
  length = 0
  dict = {}

  while right < len(s):
    if s[right] not in dict:
      dict[s[right]] = 0
      right += 1
      length = max(length, right - left)
    
    elif s[right] in dict:
      dict.pop(s[left], None)
      left += 1

  return length

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring(''))
