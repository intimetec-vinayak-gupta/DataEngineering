str = input('Enter a string: ')

setOfStr = set(str)

repeatedCharacters = [char for char in setOfStr if str.count(char)>1 and char != ' ']
print(repeatedCharacters)


str = "babad"
longestPalindrome = ""
maxLength = 0
multiplePalindromes = []

for i in range(len(str)):
    for j in range(i, len(str)):
        substring = str[i : j+1]
        if substring == substring[::-1]:
            if len(substring) > maxLength:
                maxLength = len(substring)
                longestPalindrome = substring
                multiplePalindromes = [substring]
            elif len(substring) == maxLength:
                multiplePalindromes.append(substring)

print(longestPalindrome)
