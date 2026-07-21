def isIsomorphic(s, t):
    for i in range(len(s)):
        if s.find(s[i]) != t.find(t[i]):
            return False
    return True


print(isIsomorphic("egg", "add"))      # True
print(isIsomorphic("foo", "bar"))      # False
print(isIsomorphic("paper", "title"))  # True
