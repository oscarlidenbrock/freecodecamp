# Daily challenge 2025-09-20: File Storage
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-20
#
# Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:
# 
# The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
# Return the number of whole files the drive can fit.
# Use the following conversions:
# 
# Unit , Equivalent
# 1 B  , 1 B
# 1 KB , 1000 B
# 1 MB , 1000 KB
# 1 GB , 1000 MB
#
# For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.

from typing import TypedDict


# Challenge
def number_of_files(file_size: int, file_unit: str, drive_size_gb: int) -> int:
    """
    Calculate the maximum number of files that can fit on a drive.

    :param file_size: Size of a single file (numeric value)
    :param file_unit: Unit of the file size ("B", "KB", "MB", "GB")
    :param drive_size_gb: Total drive capacity in gigabytes (GB)
    :return: Maximum number of whole files that can be stored
    """

    # Convert the file size to bytes based on the provided unit
    file_size_bytes = 0

    match file_unit:
        case "B":
            # Already in bytes
            file_size_bytes = file_size
        case "KB":
            # Convert kilobytes to bytes
            file_size_bytes = file_size * 1000
        case "MB":
            # Convert megabytes to bytes
            file_size_bytes = file_size * (1000 ** 2)
        case "GB":
            # Convert gigabytes to bytes
            file_size_bytes = file_size * (1000 ** 3)
        case _:
            file_size_bytes = 0

    # Convert drive capacity from GB to bytes
    drive_size_bytes = drive_size_gb * (1000 ** 3)

    debug("file size in bytes", file_size_bytes)
    debug("drive size in bytes", drive_size_bytes)

    # Divide total capacity by file size.
    result = int(drive_size_bytes / file_size_bytes)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [500, "KB", 1], "result": 2000},
        {"parameters": [50000, "B", 1], "result": 20000},
        {"parameters": [5, "MB", 1], "result": 200},
        {"parameters": [4096, "B", 1.5], "result": 366210},
        {"parameters": [220.5, "KB", 100], "result": 453514},
        {"parameters": [4.5, "MB", 750], "result": 166666},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = number_of_files(test['parameters'][0], test['parameters'][1], test['parameters'][2])
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