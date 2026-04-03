# Daily challenge 2025-09-21: Video Storage
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-21
#
# Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:
# 
# The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
# If not given one of the video units above, return "Invalid video unit".
# The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
# If not given one of the hard drive units above, return "Invalid drive unit".
# Return the number of whole videos the drive can fit.
# Use the following conversions:
# 
# Unit , Equivalent
# 1 B  , 1 B
# 1 KB , 1000 B
# 1 MB , 1000 KB
# 1 GB , 1000 MB
# 1 TB , 1000 GB
#
# For example, given 500, "MB", 100, and "GB" as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.

from typing import TypedDict


# Challenge
def number_of_videos(video_size: int, video_unit: str, drive_size: int, drive_unit: str) -> int | str:
    """
    Computes how many complete video files can fit into a storage device.

    :param video_size: Size of a single video (numeric value)
    :param video_unit: Unit of the video size ("B", "KB", "MB", "GB")
    :param drive_size: Total capacity of the drive (numeric value)
    :param drive_unit: Unit of the drive size ("GB", "TB")
    :return: Maximum number of whole videos that fit, or an error message if units are invalid
    """

    # Validate supported units for video size
    if video_unit not in ["B", "KB", "MB", "GB"]:
        return "Invalid video unit"

    # Validate supported units for drive capacity
    if drive_unit not in ["GB", "TB"]:
        return "Invalid drive unit"

    # Normalize both values to bytes to ensure consistent calculation
    video_size_bytes = convert_size_to_bytes(video_size, video_unit)
    drive_size_bytes = convert_size_to_bytes(drive_size, drive_unit)

    debug("video size in bytes", video_size_bytes)
    debug("drive size in bytes", drive_size_bytes)

    # Integer division: only full videos can be stored (no partial files)
    result = int(drive_size_bytes / video_size_bytes)

    return result


def convert_size_to_bytes(file_size: int, file_unit: str) -> int:
    """
    Converts a file size from a given unit to bytes.

    Uses decimal units (1 KB = 1000 bytes), not binary (1024).

    :param file_size: Numeric size value
    :param file_unit: Unit of size ("B", "KB", "MB", "GB", "TB")
    :return: Equivalent size in bytes
    """

    # Default to 0 for unsupported units (acts as a safeguard)
    file_size_bytes = 0

    match file_unit:
        case "B":
            # No conversion needed
            file_size_bytes = file_size
        case "KB":
            # Kilobytes → bytes
            file_size_bytes = file_size * 1000
        case "MB":
            # Megabytes → bytes
            file_size_bytes = file_size * (1000 ** 2)
        case "GB":
            # Gigabytes → bytes
            file_size_bytes = file_size * (1000 ** 3)
        case "TB":
            # Terabytes → bytes
            file_size_bytes = file_size * (1000 ** 4)
        case _:
            # Unsupported unit (should not occur if validated beforehand)
            file_size_bytes = 0

    return file_size_bytes
# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: int

    unitTest: list[UnitTest] = [
        {"parameters": [500, "MB", 100, "GB"], "result": 200},
        {"parameters": [1, "TB", 10, "TB"], "result": "Invalid video unit"},
        {"parameters": [2000, "MB", 100000, "MB"], "result": "Invalid drive unit"},
        {"parameters": [500000, "KB", 2, "TB"], "result": 4000},
        {"parameters": [1.5, "GB", 2.2, "TB"], "result": 1466},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = number_of_videos(test['parameters'][0], test['parameters'][1], test['parameters'][2], test['parameters'][3])
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