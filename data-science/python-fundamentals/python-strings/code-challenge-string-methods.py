# ----- Codecademy ----- #

# Python Fundamentals
# Python Strings
# Code Challenge: String methods


# --------------- Challenge 1 --------------- #
def unique_english_letters(word):
    uniques = []

    for letter in word:
        if not letter in uniques:
            uniques.append(letter)

    return len(uniques)


# Testing...
print(unique_english_letters("mississippi"))
print(unique_english_letters("Apple"))


# --------------- Challenge 2 --------------- #
def count_char_x(word, x):
    count = 0

    for letter in word:
        if letter == x:
            count += 1

    return count


# Testing...
print(count_char_x("mississippi", "s"))
print(count_char_x("mississippi", "m"))


# --------------- Challenge 3 --------------- #
def count_multi_char_x(word, x):
    return len(word.split(x)) - 1


# Testing...
print(count_multi_char_x("mississippi", "iss"))
print(count_multi_char_x("apple", "pp"))
print(count_multi_char_x("apppple", "pp"))


# --------------- Challenge 4 --------------- #
def substring_between_letters(word, start, end):
    start_idx = word.find(start)
    end_idx = word.find(end)

    if start_idx == -1 or end_idx == -1:
        return word
    else:
        return word[start_idx + 1 : end_idx]


# Testing...
print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))


# --------------- Challenge 5 --------------- #
def x_length_words(sentence, x):
    words = sentence.split()

    for word in words:
        if not len(word) >= x:
            return False

    return True


# Testing...
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))


# --------------- Challenge 6 --------------- #
def check_for_name(sentence, name):
    words = sentence.split()

    for word in words:
        if word.lower() == name.lower():
            return True

    return False


# Testing...
print(check_for_name("My name is Jamie", "Jamie"))
print(check_for_name("My name is jamie", "Jamie"))
print(check_for_name("My name is Samantha", "Jamie"))


# --------------- Challenge 7 --------------- #
def every_other_letter(word):
    letters = ""

    for i in range(0, len(word), 2):
        letters += word[i]

    return letters


# Testing...
print(every_other_letter("Codecademy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))


# --------------- Challenge 8 --------------- #
def reverse_string(word):
    reversed = ""

    for i in range(len(word) - 1, -1, -1):
        reversed += word[i]

    return reversed


# Testing...
print(reverse_string("Codecademy"))
print(reverse_string("Hello world!"))
print(reverse_string(""))


# --------------- Challenge 9 --------------- #
def make_spoonerism(word1, word2):
    temp = word2
    word2 = word1[0] + word2[1:]
    word1 = temp[0] + word1[1:]

    return f"{word1} {word2}"


# Testing...
print(make_spoonerism("Codecademy", "Learn"))
print(make_spoonerism("Hello", "world!"))
print(make_spoonerism("a", "b"))


# --------------- Challenge 10 --------------- #
def add_exclamation(word):
    if len(word) >= 20:
        return word
    else:
        for i in range(len(word), 20):
            word += "!"

        return word


# Testing...
print(add_exclamation("Codecademy"))
print(add_exclamation("Codecademy is the best place to learn"))
