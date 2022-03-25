def isAnagram(s: str, t: str) -> bool:
    original = {}
    
    for i in range(len(s)):
        if s[i] in original:
            original[s[i]] += 1
        else:  
            original[s[i]] = 1
        
    for i in range(len(t)):
        if t[i] in original:
            original[t[i]] -= 1
        else:
            return False

    for key, value in original.items():
        if value != 0:
            return False

    return True

print(isAnagram('anagram', 'ccac'))