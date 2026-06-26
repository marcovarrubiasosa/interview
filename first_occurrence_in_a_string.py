def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


def strStr2(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1

assert strStr("sadbutsad", "sad") == 0
assert strStr("leetcode", "leeto") == -1

assert strStr2("sadbutsad", "sad") == 0
assert strStr2("leetcode", "leeto") == -1
