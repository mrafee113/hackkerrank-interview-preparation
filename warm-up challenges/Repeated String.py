"""https://www.hackerrank.com/challenges/repeated-string/"""


def repeatedString(s, n):
    # part 1: biggest multiple of len(s) < n
    # abcac, 11
    bm = n // len(s)
    count = s.count('a') * bm

    # part 2: trimming s for remainder of n
    if n == bm:
        return count

    count += s[:n - bm * len(s)].count('a')
    return count
