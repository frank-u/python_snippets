"""
Created on 01.05.2012

@author: Oleksandr Poliatykin
"""
# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


def longest_subpalindrome_slice(text):
    """Return (i, j) such that text[i:j] is the longest palindrome in text."""
    # Your code here
    text = text.upper()
    longest = (0, 0, 0)
    pals = []
    if len(text) <= 1: return (0, len(text))
    if len(text) == 2:
        if text[0] == text[1]:
            return (0, 2)
        else:
            return (0, 0)
    # here if 3 or more
    # print text[1:len(text)-1]
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            pals.append((2, i, i + 2))
            if longest[0] < 2:
                longest = (2, i, i + 2)
    for i in range(1, len(text) - 1):
        if text[i - 1] == text[i + 1]:
            pals.append((3, i - 1, i + 2))
            if longest[0] < 3:
                longest = (3, i - 1, i + 2)
    while pals:
        pal = pals.pop()
        if (pal[1] > 0) and (pal[2] < len(text)):
            start = pal[1] - 1
            end = pal[2] + 1
            #print text[start:end],"s",text[start],"e",text[end-1]

            if text[start] == text[end - 1]:
                pallen = pal[0] + 2
                newpal = (pallen, start, end)
                pals.append(newpal)
                if longest[0] < pallen:
                    longest = newpal

    return (longest[1], longest[2])


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print(test())
print(longest_subpalindrome_slice(
    "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"))
# print longest_subpalindrome_slice("axa")
#print longest_subpalindrome_slice("this is xx a racecar thing")
