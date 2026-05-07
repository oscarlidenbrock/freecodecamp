# Daily challenge 2025-11-04: Image Search
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-04
#
# On November 4th, 2001, Google launched its image search, allowing people to find images using search terms. In this challenge, you will imitate the image search.
# Given an array of image names and a search term, return an array of image names containing the search term.
# 
# Ignore the case when matching the search terms.
# Return the images in the same order they appear in the input array.
# 

from typing import TypedDict


# Challenge
def image_search(images: list, term: str) -> list:
    """
    Return the images containing the search term.

    :param images: A list of image names.
    :param term: The search term.
    :return: Returns a list of image names containing the search term.
    """

    result = []

    for image in images:
        if term.lower() in image.lower():
            result.append(image)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [["dog.png", "cat.jpg", "parrot.jpeg"], "dog"], "result": ["dog.png"]},
        {"parameters": [["Sunset.jpg", "Beach.png", "sunflower.jpeg"], "sun"], "result": ["Sunset.jpg", "sunflower.jpeg"]},
        {"parameters": [["Moon.png", "sun.jpeg", "stars.png"], "PNG"], "result": ["Moon.png", "stars.png"]},
        {"parameters": [["cat.jpg", "dogToy.jpeg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"], "Cat"], "result": ["cat.jpg", "kitty-cat.png", "catNip.jpeg", "franken_cat.gif"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = image_search(test['parameters'][0], test['parameters'][1])
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