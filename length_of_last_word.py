def lengthOfLastWord(s: str) -> int:
    i = len(s) - 1
    while s[i] == ' ':
        i -= 1

    length = 0
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length

def lengthOfLastWord2(s: str) -> int:
    return len(s.split()[-1])

assert lengthOfLastWord('Hello World') == 5
assert lengthOfLastWord('   fly  me   to the   moon   ') == 4
assert lengthOfLastWord('luffy is still joyboy') == 6
assert lengthOfLastWord2('Hello World') == 5
assert lengthOfLastWord2('   fly  me   to the   moon   ') == 4
assert lengthOfLastWord2('luffy is still joyboy') == 6

