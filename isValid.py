def isValid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or stack.pop() != pairs[c]:
                return False

    return len(stack) == 0

assert True == isValid("()[]{}")
assert False == isValid("(]")
assert True == isValid("([])")
