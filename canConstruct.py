def canConstruct(ransomNote, magazine):
    for ch in ransomNote:
        if ch not in magazine:
            return False
        magazine = magazine.replace(ch, "", 1)  # Remove one occurrence

    return True

print(canConstruct("aa", "aab"))  # True
print(canConstruct("aa", "ab"))   # False
print(canConstruct("abc", "ab"))  # False
