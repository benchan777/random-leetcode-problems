def lengthOfLongestSubstring(s: str) -> int:
    unique = {}
    pointer_1 = 0
    pointer_2 = 0
    max_length = 0

    while pointer_2 < len(s):
        if s[pointer_2] not in unique:
            unique[s[pointer_2]] = pointer_2
            pointer_2 += 1
            max_length = max(max_length, len(unique))
        else:
            unique.pop(s[pointer_1])
            pointer_1 += 1
            
    return max_length

def lengthOfLongestSubstring2(s: str) -> int:
    temp = ''
    max_length = 0

    for i in range(len(s)):
        temp = ''
        temp += s[i]
        max_length = max(max_length, len(temp))
        counter = 1

        while i + counter < len(s):
            if s[i + counter] in temp:
                break
            else:
                temp += s[i + counter]
                max_length = max(max_length, len(temp))
                counter += 1

    return max_length

def longestUniqueSubsttr(string):
    last_idx = {}
    max_len = 0
    start_idx = 0
 
    for i in range(0, len(string)):
        if string[i] in last_idx:
            start_idx = max(start_idx, last_idx[string[i]] + 1)
 
        max_len = max(max_len, i-start_idx + 1)
        last_idx[string[i]] = i
 
    return max_len

def findsubstring(x):
    lst=[]
    longest=0

    if len(x) == 1:
        return 1

    for i in range(len(x)): # might get a out of bounds error here
        if x.find(x[i],i+1,len(x))!= -1:
            if len(x[i:x.find(x[i],i+1,len(x))]) > longest:
                longest=len(x[i:x.find(x[i],i+1,len(x))])

    return longest

# print(lengthOfLongestSubstring('pwwkew'))
# print(lengthOfLongestSubstring2('bbbb'))
# print(longestUniqueSubsttr('abcabcbb'))
print(findsubstring('au'))
# print(findsubstring('pwwkew'))