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


"""
# Joining strings.
    reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
    reapers_line_one = " ".join(reapers_line_one_words)
"""


"""
# Joining strings 2.
    winter_trees_lines = [
        "All the complicated details",
        "of the attiring and",
        "the disattiring are completed!",
        "A liquid moon",
        "moves gently among",
        "the long branches.",
        "Thus having prepared their buds",
        "against a sure winter",
        "the wise trees",
        "stand sleeping in the cold.",
    ]

    winter_trees_full = "\n".join(winter_trees_lines)
"""


"""
# Stripping.
    love_maybe_lines = [
        "Always    ",
        "     in the middle of our bloodiest battles  ",
        "you lay down your arms",
        "           like flowering mines    ",
        "\n",
        "   to conquer me home.    ",
    ]

    love_maybe_lines_stripped = []

    for line in love_maybe_lines:
        love_maybe_lines_stripped.append(line.strip())

    love_maybe_full = "\n".join(love_maybe_lines_stripped)

    print(love_maybe_full)
"""


"""
# Replacing.
    toomer_bio = "Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands."

    toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
"""


"""
# Finding.
    god_wills_it_line_one = "The very earth will disown you"

    disown_placement = god_wills_it_line_one.find("disown")
"""

"""
# Formatting.
    def poem_title_card(title, poet):
        return 'The poem "{}" is written by {}.'.format(title, poet)

    poem_title_card("I Hear America Singing", "Walt Whitman")
"""

"""
# Formatting 2.
    def poem_description(publishing_date, author, title, original_work):
        poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
            publishing_date=publishing_date,
            author=author,
            title=title,
            original_work=original_work,
        )
        return poem_desc


    my_beard_description = poem_description(
        "1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends"
    )
"""
