"""
# Concatenating strings.
    first_name = "Julie"
    last_name = "Blevins"


    def account_generator(first_name, last_name):
        return first_name[:3] + last_name[:3]


    new_account = account_generator(first_name, last_name)

"""


"""
# String slicing.
    first_name = "Reiko"
    last_name = "Matsuki"


    def password_generator(first_name, last_name):
        return first_name[len(first_name) - 3 :] + last_name[len(last_name) - 3 :]


    temp_password = password_generator(first_name, last_name)
"""


"""
# Negative indices.
    company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

    second_to_last = company_motto[-2]

    final_word = company_motto[-4:]
"""


"""
# Immutability of strings.
    first_name = "Bob"
    last_name = "Daily"

    fixed_first_name = "R" + first_name[1 : len(first_name)]
"""


"""
# Strings and conditionals.
    def contains(big_string, little_string):
        if little_string in big_string:
            return True
        else:
            return False


    def common_letters(string_one, string_two):
        commons = []

        for letter in string_one:
            if letter in string_two and not letter in commons:
                commons.append(letter)

        return commons

"""


"""
# Review.
    def username_generator(first_name, last_name):
        first = ""
        last = ""

        if len(first_name) > 3:
            first = first_name[:3]
        else:
            first = first_name

        if len(last_name) > 4:
            last = last_name[:4]
        else:
            last = last_name

        return first + last


    def password_generator(username):
        password = ""

        for i in range(len(username)):
            password += username[i - 1]

        return password
"""
