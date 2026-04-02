# Daily challenge 2025-09-19: Photo Storage
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-19
#
# Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), return the number of photos the hard drive can store using the following constraints:
# 
# 1 gigabyte equals 1000 megabytes.
# Return the number of whole photos the drive can store.
# 

from typing import TypedDict


# Challenge
def number_of_photos(photo_size_mb: int, drive_size_gb: int) -> int:
    """
    Calculate how many photos can be stored on a drive.
    Assumes 1 GB = 1000 MB (decimal units, not binary).

    :param photo_size_mb: Size of a single photo in megabytes (MB)
    :param drive_size_gb: Total storage capacity in gigabytes (GB)
    :return: Maximum number of whole photos that can fit in the drive
    """

    # Convert drive capacity from GB to MB and divide by photo size.
    result = int(drive_size_gb * 1000 / photo_size_mb)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [1, 1], "result": 1000},
        {"parameters": [2, 1], "result": 500},
        {"parameters": [4, 256], "result": 64000},
        {"parameters": [3.5, 750], "result": 214285},
        {"parameters": [3.5, 5.5], "result": 1571},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = number_of_photos(test['parameters'][0], test['parameters'][1])
        if result == test['result']:
            print("OK\r")

            print(f"INPUT: ", test['parameters'])
            print(f"RETURN: ", result)
            print("======================\r")
        else:
            print("ERROR\r")

            print(f"INPUT: ", test['parameters'])
            print(f"RETURN: ", result)
            print(f"EXPECTED: ", test['result'])
            print("======================\r")

            if len(debug_messages) > 0:
                print("DEBUG:")
                for msg in debug_messages:
                    print(f"", msg[0], ": ", msg[1])

            print("")
            answer = input("Continue with the next test? [y/n] ")
            print("")

            if not (answer == "y" or answer == ""): return

debug_messages = []


def debug(type, message):
    debug_messages.append([type, message])

test()