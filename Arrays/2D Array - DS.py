"""https://www.hackerrank.com/challenges/2d-array/"""


def hourglassSum(arr):
    maximum = float('-inf')
    for i in range(0, 3 + 1):
        for j in range(0, 3 + 1):
            hsum = sum(arr[i][j:j + 3])
            hsum += arr[i + 1][j + 1]
            hsum += sum(arr[i + 2][j:j + 3])
            maximum = max(hsum, maximum)

    return maximum
