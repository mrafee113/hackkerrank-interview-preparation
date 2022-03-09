"""https://www.hackerrank.com/challenges/ctci-ransom-note/"""
from collections import Counter


def checkMagazine(magazine: list, note: list):
    # magazine: attack at dawn
    # note: Attack at dawn
    magazine_hashmap = Counter(magazine)
    note_hashmap = Counter(note)
    for word, word_count in note_hashmap.items():
        if word not in magazine_hashmap or magazine_hashmap[word] < word_count:
            print("No")
            break
    else:
        print("Yes")
