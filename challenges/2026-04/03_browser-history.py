# Daily challenge 2026-04-03: Browser History
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-03
#
# Given an array of browser commands, return an array with two values: the history as an array of URLs, and the index of the current page.
# Valid commands are:
# 
# "URL" - Where URL is a web address ("freecodecamp.org" for example). Navigates to the given URL, adds it to the history at the next position, and discards any forward history.
# "Back" - moves to the previous page in history, or stays on the current page if there isn't one.
# "Forward" - moves to the next page in history, or stays on the current page if there isn't one.
# 
# For example, given ["freecodecamp.org", "freecodecamp.org/learn", "Back"], return [["freecodecamp.org", "freecodecamp.org/learn"], 0].

from typing import TypedDict


# Challenge
def get_browser_history(commands: list) -> list:
    """
    Simulates browser navigation history.

    :param commands: List of navigation commands or URLs.
                     Commands can be:
                     - "Back": move one step back in history
                     - "Forward": move one step forward in history
                     - any other string: treated as a new URL visit
    :return: A list containing:
             - the history list
             - the current position index
    """
    result = [[], -1]  # [history_list, current_index]

    for command in commands:
        match command:
            case "Back":
                # Move back if not already at the beginning
                if result[1] > 0:
                    result[1] -= 1

            case "Forward":
                # Move forward if not already at the latest entry
                if result[1] < len(result[0]) - 1:
                    result[1] += 1

            case _:
                if result[1] != len(result[0]) - 1:
                    # Visiting a new URL after going back, overwrite forward history from current position
                    result[1] += 1
                    result[0][result[1]] = command
                else:
                    # Normal navigation: append new URL to history
                    result[0].append(command)
                    result[1] += 1

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [["freecodecamp.org", "freecodecamp.org/learn", "Back"]], "result": [["freecodecamp.org", "freecodecamp.org/learn"], 0]},
        {"parameters": [["example.com", "example.com/about", "example.com/contact", "example.com/blog"]], "result": [["example.com", "example.com/about", "example.com/contact", "example.com/blog"], 3]},
        {"parameters": [["example.com", "example.com/about", "Back", "example.com/contact", "example.com/blog", "Back", "Back", "Forward"]], "result": [["example.com", "example.com/contact", "example.com/blog"], 1]},
        {"parameters": [["example.com", "example.com/about", "example.com/contact", "example.com/blog", "Back", "Back", "Forward", "freecodecamp.org"]], "result": [["example.com", "example.com/about", "example.com/contact", "freecodecamp.org"], 3]},
        {"parameters": [["example.com", "example.com/about", "Back", "Back"]], "result": [["example.com", "example.com/about"], 0]},
        {"parameters": [["example.com", "example.com/about", "Forward"]], "result": [["example.com", "example.com/about"], 1]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_browser_history(test['parameters'][0])
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