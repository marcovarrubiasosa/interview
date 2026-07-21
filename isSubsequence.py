def isSubsequence(s: str, t: str) -> bool:
    i = 0
    for c in t:
        if i < len(s) and c == s[i]:
            i += 1

    return i == len(s)

assert isSubsequence("abc", "ahbgdc") == True
assert isSubsequence("axc", "ahbgdc") == False
