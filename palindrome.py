def isPalindrome(s: str) -> bool:
    cleaned = ""
    for c in s:
        if c.isalnum():
            cleaned += c.lower()

    return cleaned == cleaned[::-1]

def isPalindrome1(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

assert isPalindrome1("A man, a plan, a canal: Panama") == True
assert isPalindrome1("race a car") == False
assert isPalindrome("") == True
        
