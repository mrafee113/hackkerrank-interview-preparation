"""https://www.hackerrank.com/challenges/sherlock-and-anagrams/"""

from itertools import combinations, groupby
from collections import Counter


def sherlockAndAnagrams(s):
    # distinct chars are not valid
    if len(set(s)) == len(s):
        return 0

    anagram_counter = 0
    substrings = [s[start:end] for start, end in
                  combinations(range(len(s) + 1), 2)]
    substrings.sort(key=lambda x: len(x))
    for length, v in groupby(substrings, lambda x: len(x)):
        if length == len(s):
            break

        group = list(v)
        for pair in combinations(group, 2):
            if Counter(pair[0]) == Counter(pair[1]):
                anagram_counter += 1
                print(pair[0], pair[1])

    return anagram_counter
