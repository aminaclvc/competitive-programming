import re


def isPalindrome(s):
    return s == s[::-1]


word = input()
regex = re.compile("[^a-zA-Z]")
word = regex.sub("", word).lower()

lenght = len(word)
for i in range(lenght):
    for j in range(lenght):
        newWord = word[i : i + j + 2]
        if len(newWord) < 2:
            print("Anti-palindrome")
            exit()

        if isPalindrome(newWord):
            print("Palindrome")
            exit()
