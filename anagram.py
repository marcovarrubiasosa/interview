def isAnagram(s, t):
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))  # True
print(isAnagram("rat", "car"))          # False

def isAnagram2(s, t):
    if len(s) != len(t):
        return False

    counts = {}

    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False

    return True

print(isAnagram2("anagram", "nagaram"))  # True
print(isAnagram2("rat", "car"))          # False
