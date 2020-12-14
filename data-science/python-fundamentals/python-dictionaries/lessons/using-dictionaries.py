# ----- Codecademy ----- #

# Python Fundamentals
# Python Dictionaries
# Lesson: Using Dictionaries


# --------------- Get All Keys --------------- #
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384,
}

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18,
}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


# --------------- Get All Values --------------- #
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18,
}

total_exercises = 0

for value in num_exercises.values():
    total_exercises += value

print(total_exercises)


# --------------- Get All Items --------------- #
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9,
}

for key, value in pct_women_in_occupation.items():
    print(f"Women make up {value} percent of {key}s.")


# --------------- Review --------------- #
tarot = {
    1: "The Magician",
    2: "The High Priestess",
    3: "The Empress",
    4: "The Emperor",
    5: "The Hierophant",
    6: "The Lovers",
    7: "The Chariot",
    8: "Strength",
    9: "The Hermit",
    10: "Wheel of Fortune",
    11: "Justice",
    12: "The Hanged Man",
    13: "Death",
    14: "Temperance",
    15: "The Devil",
    16: "The Tower",
    17: "The Star",
    18: "The Moon",
    19: "The Sun",
    20: "Judgement",
    21: "The World",
    22: "The Fool",
}

spread = {}

spread.update({"past": tarot.pop(13)})
spread.update({"present": tarot.pop(22)})
spread.update({"future": tarot.pop(10)})

for key, value in spread.items():
    print(f"Your {key} is the {value} card.")
