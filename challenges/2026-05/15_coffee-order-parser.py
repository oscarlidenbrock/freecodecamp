# Daily challenge 2026-05-15: Coffee Order Parser
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-15
#
# Given a string for a coffee order, identify any menu items and return a formatted order.
# Use the following menu items and prices:
#
# Item              , Price
# "cold brew"       , $4.50
# "oat latte"       , $5.00
# "cappuccino"      , $4.75
# "espresso"        , $3.00
# "vanilla syrup"   , $0.75
# "caramel drizzle" , $0.60
# "extra shot"      , $0.50
# "oat milk"        , $0.75
# "cream"           , $0.75
#
# Return a string with the matched items joined by " + ", followed by a colon and space (": "), and the total price.
# For example, given "I'd like an oat latte with vanilla syrup and an extra shot please.", return "oat latte + vanilla syrup + extra shot: $6.25"
# Items should appear in the order they appear in the menu and the total price should always have two decimal places.
#

from typing import TypedDict


# Challenge
def format_coffee_order(order: str) -> str:
    """
    Return a formatted order.

    :param order: The order.
    :return: Returns a formatted order.
    """

    # Price list
    prices = {
        "cold brew": 4.50,
        "oat latte": 5.00,
        "cappuccino": 4.75,
        "espresso": 3.00,
        "vanilla syrup": 0.75,
        "caramel drizzle": 0.60,
        "extra shot": 0.50,
        "oat milk": 0.75,
        "cream": 0.75,
    }

    # Get a list with the items in the order
    items = []

    for price in prices:
        if price in order:
            items.append(price)

    # Return the formatted order
    return f"{' + '.join(items)}: ${format(sum([prices[item] for item in items]), '.2f')}"


# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: str

    unitTest: list[UnitTest] = [
        {"parameters": ["I'd like an oat latte with vanilla syrup and an extra shot please."], "result": "oat latte + vanilla syrup + extra shot: $6.25"},
        {"parameters": ["Give me a cappuccino with caramel drizzle, vanilla syrup, and some oat milk."], "result": "cappuccino + vanilla syrup + caramel drizzle + oat milk: $6.85"},
        {"parameters": ["Can I get a cold brew with some cream and an extra shot."], "result": "cold brew + extra shot + cream: $5.75"},
        {"parameters": ["Just an espresso please."], "result": "espresso: $3.00"},
        {"parameters": ["I'll take an oat latte with cream and an extra shot, and some vanilla syrup and caramel drizzle."], "result": "oat latte + vanilla syrup + caramel drizzle + extra shot + cream: $7.60"},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = format_coffee_order(test['parameters'][0])
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