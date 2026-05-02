# Daily challenge 2025-10-28: Navigator
# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-28
#
# On October 28, 1994, Netscape Navigator was released, helping millions explore the early web.
# Given an array of browser commands you executed on Netscape Navigator, return the current page you are on after executing all the commands using the following rules:
# 
# You always start on the "Home" page, which will not be included in the commands array.
# Valid commands are:
# 
# "Visit Page": Where "Page" is the name of the page you are visiting. For example, "Visit About" takes you to the "About" page. When you visit a new page, make sure to discard any forward history you have.
# "Back": Takes you to the previous page in your history or stays on the current page if there isn't one.
# "Forward": Takes you forward in the history to the page you came from or stays on the current page if there isn't one.
#
# For example, given ["Visit About Us", "Back", "Forward"], return "About Us".

from typing import TypedDict


# Challenge
def navigate(commands: list[str]) -> str:
    """
    Simulate Netscape Navigator page history.

    :param commands: Browser commands to execute from the Home page.
    :return: The page that is currently open after all commands run.
    """
    history = ["Home"]
    current_index = 0

    for command in commands:
        if command == "Back":
            # Move to the previous history entry when one exists.
            if current_index > 0:
                current_index -= 1
            continue

        if command == "Forward":
            # Move to the next history entry when forward history exists.
            if current_index < len(history) - 1:
                current_index += 1
            continue

        # A Visit command stores everything after "Visit " as the page name.
        page = command.removeprefix("Visit ")

        # Visiting a new page from the middle discards all forward history.
        history = history[:current_index + 1]
        history.append(page)
        current_index += 1

    # The current index always points to the active page.
    return history[current_index]

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": [["Visit About Us", "Back", "Forward"]], "result": "About Us"},
        {"parameters": [["Forward"]], "result": "Home"},
        {"parameters": [["Back"]], "result": "Home"},
        {"parameters": [["Visit About Us", "Visit Gallery"]], "result": "Gallery"},
        {"parameters": [["Visit About Us", "Visit Gallery", "Back", "Back"]], "result": "Home"},
        {"parameters": [["Visit About", "Visit Gallery", "Back", "Visit Contact", "Forward"]], "result": "Contact"},
        {"parameters": [["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]], "result": "Visit Us"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = navigate(test['parameters'][0])
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
