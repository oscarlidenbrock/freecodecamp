import random
import re
def main():
    print("\n===========\n  HANGMAN\n===========\n")

    # Leer el diccionario
    with open("dictionary.txt", "r", encoding="utf-8") as f:
        dictionary = f.read()

    # Preguntar por una palabra
    secret_word = input("Do you want to enter the word to guess? (leave empty to get a random word from the dictionary): ")

    # Si no se ha introducido, obtener una palabra random del diccionario
    if secret_word == "":
        secret_word = random.choice(re.findall(r"[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ]+", dictionary))
        secret_word = re.split(r'[^a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+', secret_word)[0]

    # Crear el patrón de la palabra secreta
    pattern_word = "_" * len(secret_word)

    print("Word to find: " + secret_word)
    print("")

    # Intentar encontrar la palabra en x intentos
    attempt = 0
    blacklist = []
    whitelist = []

    while attempt < 10:
        attempt += 1
        search_word_result = search_word_by_pattern(pattern_word, whitelist, blacklist, dictionary)
        next_attempt = search_word_result[0]

        # Rellena el pattern con la letra, si existe
        next_pattern_word = ""

        for i in range(len(secret_word)):
            if secret_word[i] == next_attempt:
                next_pattern_word += next_attempt
            else:
                next_pattern_word += pattern_word[i]

        # Actuliza el patter y añade el intento al whitelist o al blacklist
        if pattern_word != next_pattern_word:
            whitelist.append(next_attempt)
        else:
            blacklist.append(next_attempt)

        pattern_word = next_pattern_word

        print("Attempt #", str(attempt), ":")
        print("  letter: ", next_attempt, "(" + str(search_word_result[1]) + "%)")
        print("    word: ", pattern_word)

        # Comprueba si has ganado
        if pattern_word == secret_word:
            print("\nYOU WIN!!\n")
            quit()

    # Después de 10 intentos, si no se ha encontrado la palabra, has perdido
    print("\nYOU LOOSE!!\n")

def search_word_by_pattern(pattern: str, whitelist: list, blacklist: list, dictionary: str) -> list:
    # Busca todas las palabras en el diccionario que coincidan con el pattern
    if len(blacklist) > 0:
        regex = "(?!.*[" + "".join(blacklist) + "])" + pattern.replace("_", "\\w")
    else:
        regex = pattern.replace("_", "\\w")

    valid_words = re.findall(regex, dictionary)

    # Cuenta cuantas letras contienen las palabras
    letters = {}

    for word in valid_words:
        word = word.lower()

        for letter in word:
            if not letter in blacklist and not letter in whitelist:
                letters[letter] = letters.get(letter, 0) + 1

    # Obtén cual es la letra con más coincidencias
    max_key = max(letters, key=letters.get)

    # Obtén el % de probabilidad
    total = sum(letters.values())
    percent = round(letters[max_key] / total * 100)

    return [max_key, percent]

main()