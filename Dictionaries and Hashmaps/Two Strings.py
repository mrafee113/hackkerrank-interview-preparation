"""https://www.hackerrank.com/challenges/two-strings/"""


def twoStrings(s1: str, s2: str):
    if set(s1).intersection(set(s2)):
        return "YES"
    else:
        return "NO"
