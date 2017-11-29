def vowel_check(c):
    if c in ['a','e','i','o','u']:
        return True
    else:
        return False

c=input('Enter character: ')
print(vowel_check(c))