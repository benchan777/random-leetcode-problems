def filter_vowels(s):
    vowels = 'aeiou'
    consonants = ''

    for i in s:
        if i not in vowels:
            consonants += i

    return consonants

def filter_consonants(s):
    vowels = 'aeiou'
    only_vowels = ''

    for i in s:
        if i in vowels:
            only_vowels += i

    return only_vowels

print(filter_vowels('hackerrank'))
print(filter_consonants('hackerrank'))