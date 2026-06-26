def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ''
    for chars in zip(*strs):
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix
        

assert longestCommonPrefix(['flower','flow','flight']) == 'fl'
assert longestCommonPrefix(['dog', 'racecar', 'car']) == ''
