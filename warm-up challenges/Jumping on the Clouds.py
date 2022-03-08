"""https://www.hackerrank.com/challenges/jumping-on-the-clouds/"""


def jumpingOnClouds(c: list):
    step_counter = 0
    index = 0
    path_length = len(c)
    while index < path_length - 1:
        if index == path_length - 2:
            step_counter += 1
            break

        index += 2 if c[index + 2] != 1 else 1
        step_counter += 1

    return step_counter
