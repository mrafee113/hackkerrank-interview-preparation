"""https://www.hackerrank.com/challenges/sock-merchant/"""


def sockMerchant(n, ar):
    pair_counter = 0
    for number in set(ar):
        count = ar.count(number)
        if count < 2:
            continue
        pair_counter += count // 2 if count % 2 == 0 else (count - 1) // 2

    return pair_counter
