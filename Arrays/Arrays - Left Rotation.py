"""https://www.hackerrank.com/challenges/ctci-array-left-rotation/"""


def rotLeft(a: list, d: int):
    d = d % len(a)
    queue = a[:d]
    for index in range(d, len(a)):
        a[index - d] = a[index]
    a[len(a) - d:] = queue

    return a
