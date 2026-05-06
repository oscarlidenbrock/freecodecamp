# Daily challenge 2026-05-06: Allergen Friendly Meals
# https://www.freecodecamp.org/learn/daily-coding-challenge/2026-05-06
#
# Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.
# 
# Each meal is in the format [meal, allergens], where meal is the name of the meal, and allergens is an array of the allergens the meal contains. For example, ["pasta", ["wheat", "milk"]].
# Allergens to avoid will be an array of strings.
# 
# Return safe meal names in the same order given. If no meal is safe, return an empty array.

from typing import TypedDict


# Challenge
def get_allergen_friendly_meals(meals: list, allergens: list) -> list:
    """
    Return all meals that contain none of the given allergens.

    :param meals: Array of meals and allergens.
    :param allergens: Array of allergens to avoid.
    :return: Returns an array of safe meals.
    """

    # Store the names of meals that do not contain any avoided allergens.
    result = []

    for meal in meals:
        # Split each meal entry into its allergen list and display name.
        ingredients = meal[1]
        meal = meal[0]

        # Track whether this meal contains at least one allergen to avoid.
        found = False
        for ingredient in ingredients:
            if ingredient in allergens:
                found = True
                break

        # Keep only meals where no avoided allergen was found.
        if not found:
            result.append(meal)

    return result

# Test
def test():
    class UnitTest(TypedDict):
        parameters: list
        result: list

    unitTest: list[UnitTest] = [
        {"parameters": [[["pasta", ["wheat", "milk"]], ["salad", ["nuts"]]], ["milk"]], "result": ["salad"]},
        {"parameters": [[["steak", ["soy"]], ["fried rice", []], ["fish tacos", ["fish", "wheat"]], ["chicken parmesan", ["wheat", "milk"]]], ["soy", "fish"]], "result": ["fried rice", "chicken parmesan"]},
        {"parameters": [[["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["eggs", "milk"]], "result": ["oatmeal", "granola", "toast"]},
        {"parameters": [[["oatmeal", ["nuts"]], ["pancakes", ["wheat", "milk"]], ["granola", []], ["yogurt", ["milk"]], ["eggs", ["eggs", "milk"]], ["toast", ["wheat"]]], ["wheat", "nuts"]], "result": ["granola", "yogurt", "eggs"]},
    ]

    n = 0

    for test in unitTest:
        n += 1
        debug_messages.clear()
        print("======================")
        print(f"Test #{n} => ", end="")

        result = get_allergen_friendly_meals(test['parameters'][0], test['parameters'][1])
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
