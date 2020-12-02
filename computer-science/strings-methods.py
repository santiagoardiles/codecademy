"""
# Formatting methods.
    poem_title = "spring storm"
    poem_author = "William Carlos Williams"

    poem_title_fixed = poem_title.title()
    print(poem_title_fixed)

    poem_author_fixed = poem_author.upper()
    print(poem_author_fixed)
"""

"""
# Splitting strings.
    line_one = "The sky has given over"
    line_one_words = line_one.split()
"""

"""
# Splitting strings 2.
    authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
    author_names = authors.split(",")

    def get_last_names(full_names):
        last_names = []

        for name in full_names:
            split_name = name.split()
            last_names.append(split_name[1])

        return last_names

    author_last_names = get_last_names(author_names)
"""