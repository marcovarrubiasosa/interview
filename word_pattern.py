def wordPattern(pattern, s):
    words = s.split()

    if len(pattern) != len(words):
        return False

    return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))

assert wordPattern("abba", "dog cat cat dog") ==  True

assert wordPattern("abba", "dog cat cat fish") ==  False
