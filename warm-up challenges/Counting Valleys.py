"""https://www.hackerrank.com/challenges/counting-valleys/"""


def countingValleys(steps, path):
    valley_counter = 0
    altitude = 0
    processing_valley = False
    for step in path:
        if altitude == 0 and processing_valley:
            valley_counter += 1
            processing_valley = False

        if altitude == 0 and step == "D":
            processing_valley = True

        if step == "U":
            altitude += 1
        elif step == "D":
            altitude -= 1

    # for final valley
    if altitude == 0 and processing_valley:
        valley_counter += 1

    return valley_counter
