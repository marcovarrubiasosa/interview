def romanToInt(s: str) -> int:
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res = 0

    for i in range(len(s)):
        val = roman[s[i]]
        if i + 1 < len(s) and val < roman[s[i+1]]:
            res -= val
        else:
            res += val

    return res

assert romanToInt('III') == 3
assert romanToInt('LVIII') == 58
assert romanToInt('MCMXCIV') == 1994
