# Daily challenge 2026-03-07: Element Size
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-07
#
# Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.
# 
# 
# The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.
# 
# 
# "vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.
# 
# 
# "vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.
# 
# 

from typing import TypedDict
import re

# Challenge
def get_element_size(window_size: str, element_vw: str, element_vh: str) -> str:
    """
    Returns the size of the elements in a window
    :param window_size: Window resolution
    :param element_vw: viewport width
    :param element_vh: viewport height
    :return: object size
    """
    result = ""
    window_width = 0
    window_height = 0
    viewport_width = 0
    viewport_height = 0

    # Get the window size values
    match = re.search(r'(\d+)\s*x\s*(\d+)', window_size)

    if match:
        window_width = int(match.group(1))
        window_height = int(match.group(2))

    debug("window width", window_width)
    debug("window height", window_height)

    # Get the viewport width value
    match = re.search(r'(\d+)vw', element_vw)

    if match:
        viewport_width = int(match.group(1))

    debug("viewport_width", viewport_width)

    # Get the viewport height value
    match = re.search(r'(\d+)vh', element_vh)

    if match:
        viewport_height = int(match.group(1))

    debug("viewport_height", viewport_height)

    # Calculate size using the viewports
    width = int(window_width * viewport_width / 100)
    height = int(window_height * viewport_height / 100)

    result = str(width) + " x " + str(height)
    debug("result", result)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["1200 x 800", "50vw", "50vh"], "result": "600 x 400"},
        {"parameters": ["320 x 480", "25vw", "50vh"], "result": "80 x 240"},
        {"parameters": ["1000 x 500", "7vw", "3vh"], "result": "70 x 15"},
        {"parameters": ["1920 x 1080", "95vw", "100vh"], "result": "1824 x 1080"},
        {"parameters": ["1200 x 800", "0vw", "0vh"], "result": "0 x 0"},
        {"parameters": ["1440 x 900", "100vw", "114vh"], "result": "1440 x 1026"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_element_size(test['parameters'][0], test['parameters'][1], test['parameters'][2])
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