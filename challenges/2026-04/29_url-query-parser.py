# Daily challenge 2026-04-29: URL Query Parser
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-04-29
#
# Given a URL that contains a query string, parse the query string into an object (or dictionary) of key-value pairs.
# 
# The query string begins after the "?",
# each parameter is separated by "&#x26;",
# each key/value pair is separated by "="
# 
# For example, given "https://example.com/search?name=Alice&#x26;age=30", return:
# {
#   "name": "Alice",
#   "age": "30"
# }
# 
# All values should be returned as strings.

from typing import TypedDict


# Challenge
def parse_url_query(url: str) -> dict:
    """
    Get the query string from a URL and parse it into a dictionary.

    :param url: The URL containing the query string.
    :return: The parsed query string as a dictionary.
    """

    result = {}
    query = url.split("?")[1]
    params = query.split("&")

    for param in params:
        key, value = param.split("=")
        result[key] = value

    return result


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: dict

    unitTest: list[UnitTest] = [
        {"parameters": ["https://example.com/search?name=Alice&age=30"], "result": {"name": "Alice", "age": "30"}},
        {"parameters": ["https://freecodecamp.org/learn?skill=programming&language=python"], "result": {"skill": "programming", "language": "python"}},
        {"parameters": ["https://freecodecamp.org/items?category=books&sort=asc&page=2"], "result": {"category": "books", "sort": "asc", "page": "2"}},
        {"parameters": ["https://example.com?redirect=freecodecamp.org/learn&when=now"], "result": {"redirect": "freecodecamp.org/learn", "when": "now"}},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = parse_url_query(test['parameters'][0])
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