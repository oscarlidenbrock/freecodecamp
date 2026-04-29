# Daily challenge 2025-10-23: Favorite Songs
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-23
#
# Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.
# Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played songs, with the most played song first.
# 
# Each object will have a "title" property (string), and a "plays" property (integer).
# 

from typing import TypedDict


# Challenge
def favorite_songs(playlist: list[dict]) -> list[str]:

    return playlist

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]], "result": ["Sync or Swim", "Earbud Blues"]},
        {"parameters": [[{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]], "result": ["Clickwheel Love", "99 Downloads"]},
        {"parameters": [[{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]], "result": ["Song B", "Song C"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = favorite_songs(test['parameters'][0])
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