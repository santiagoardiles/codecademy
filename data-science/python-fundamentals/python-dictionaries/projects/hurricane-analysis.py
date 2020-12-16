# ----- Codecademy ----- #

# Python Fundamentals
# Python Dictionaries
# Project: Hurricane Analysis


# Names of hurricanes.
names = [
    "Cuba I",
    "San Felipe II Okeechobee",
    "Bahamas",
    "Cuba II",
    "CubaBrownsville",
    "Tampico",
    "Labor Day",
    "New England",
    "Carol",
    "Janet",
    "Carla",
    "Hattie",
    "Beulah",
    "Camille",
    "Edith",
    "Anita",
    "David",
    "Allen",
    "Gilbert",
    "Hugo",
    "Andrew",
    "Mitch",
    "Isabel",
    "Ivan",
    "Emily",
    "Katrina",
    "Rita",
    "Wilma",
    "Dean",
    "Felix",
    "Matthew",
    "Irma",
    "Maria",
    "Michael",
]

# Months of hurricanes.
months = [
    "October",
    "September",
    "September",
    "November",
    "August",
    "September",
    "September",
    "September",
    "September",
    "September",
    "September",
    "October",
    "September",
    "August",
    "September",
    "September",
    "August",
    "August",
    "September",
    "September",
    "August",
    "October",
    "September",
    "September",
    "July",
    "August",
    "September",
    "October",
    "August",
    "September",
    "October",
    "September",
    "September",
    "October",
]

# Years of hurricanes.
years = [
    1924,
    1928,
    1932,
    1932,
    1933,
    1933,
    1935,
    1938,
    1953,
    1955,
    1961,
    1961,
    1967,
    1969,
    1971,
    1977,
    1979,
    1980,
    1988,
    1989,
    1992,
    1998,
    2003,
    2004,
    2005,
    2005,
    2005,
    2005,
    2007,
    2007,
    2016,
    2017,
    2017,
    2018,
]

# Maximum sustained winds (mph) of hurricanes.
max_sustained_winds = [
    165,
    160,
    160,
    175,
    160,
    160,
    185,
    160,
    160,
    175,
    175,
    160,
    160,
    175,
    160,
    175,
    175,
    190,
    185,
    160,
    175,
    180,
    165,
    165,
    160,
    175,
    180,
    185,
    175,
    175,
    165,
    180,
    175,
    160,
]

# Areas affected by each hurricane.
areas_affected = [
    ["Central America", "Mexico", "Cuba", "Florida", "The Bahamas"],
    ["Lesser Antilles", "The Bahamas", "United States East Coast", "Atlantic Canada"],
    ["The Bahamas", "Northeastern United States"],
    ["Lesser Antilles", "Jamaica", "Cayman Islands", "Cuba", "The Bahamas", "Bermuda"],
    ["The Bahamas", "Cuba", "Florida", "Texas", "Tamaulipas"],
    ["Jamaica", "Yucatn Peninsula"],
    ["The Bahamas", "Florida", "Georgia", "The Carolinas", "Virginia"],
    ["Southeastern United States", "Northeastern United States", "Southwestern Quebec"],
    ["Bermuda", "New England", "Atlantic Canada"],
    ["Lesser Antilles", "Central America"],
    ["Texas", "Louisiana", "Midwestern United States"],
    ["Central America"],
    ["The Caribbean", "Mexico", "Texas"],
    ["Cuba", "United States Gulf Coast"],
    ["The Caribbean", "Central America", "Mexico", "United States Gulf Coast"],
    ["Mexico"],
    ["The Caribbean", "United States East coast"],
    ["The Caribbean", "Yucatn Peninsula", "Mexico", "South Texas"],
    ["Jamaica", "Venezuela", "Central America", "Hispaniola", "Mexico"],
    ["The Caribbean", "United States East Coast"],
    ["The Bahamas", "Florida", "United States Gulf Coast"],
    ["Central America", "Yucatn Peninsula", "South Florida"],
    ["Greater Antilles", "Bahamas", "Eastern United States", "Ontario"],
    ["The Caribbean", "Venezuela", "United States Gulf Coast"],
    ["Windward Islands", "Jamaica", "Mexico", "Texas"],
    ["Bahamas", "United States Gulf Coast"],
    ["Cuba", "United States Gulf Coast"],
    ["Greater Antilles", "Central America", "Florida"],
    ["The Caribbean", "Central America"],
    ["Nicaragua", "Honduras"],
    [
        "Antilles",
        "Venezuela",
        "Colombia",
        "United States East Coast",
        "Atlantic Canada",
    ],
    [
        "Cape Verde",
        "The Caribbean",
        "British Virgin Islands",
        "U.S. Virgin Islands",
        "Cuba",
        "Florida",
    ],
    [
        "Lesser Antilles",
        "Virgin Islands",
        "Puerto Rico",
        "Dominican Republic",
        "Turks and Caicos Islands",
    ],
    ["Central America", "United States Gulf Coast (especially Florida Panhandle)"],
]

# Damages (USD($)) of hurricanes.
damages = [
    "Damages not recorded",
    "100M",
    "Damages not recorded",
    "40M",
    "27.9M",
    "5M",
    "Damages not recorded",
    "306M",
    "2M",
    "65.8M",
    "326M",
    "60.3M",
    "208M",
    "1.42B",
    "25.4M",
    "Damages not recorded",
    "1.54B",
    "1.24B",
    "7.1B",
    "10B",
    "26.5B",
    "6.2B",
    "5.37B",
    "23.3B",
    "1.01B",
    "125B",
    "12B",
    "29.4B",
    "1.76B",
    "720M",
    "15.1B",
    "64.8B",
    "91.6B",
    "25.1B",
]

# Deaths for each hurricane.
deaths = [
    90,
    4000,
    16,
    3103,
    179,
    184,
    408,
    682,
    5,
    1023,
    43,
    319,
    688,
    259,
    37,
    11,
    2068,
    269,
    318,
    107,
    65,
    19325,
    51,
    124,
    17,
    1836,
    125,
    87,
    45,
    133,
    603,
    138,
    3057,
    74,
]


# -------------------- Code for the project. -------------------- #


# ------- Iteration 1. ------- #
"""Just click."""


# ------- Iteration 2. ------- #
def update_damages(damages):
    updated_damages = []

    for damage in damages:
        if damage == "Damages not recorded":
            updated_damages.append(damage)
        elif damage[-1:] == "M":
            updated_damages.append(float(damage[: len(damage) - 1]) * 1000000)
        else:
            updated_damages.append(float(damage[: len(damage) - 1]) * 1000000000)

    return updated_damages


updated_damages = update_damages(damages)


# ------- Iteration 3. ------- #
def hurricanes_dictionary_maker(
    names, months, years, max_sustained_winds, areas_affected, damages, deaths
):
    hurricanes = {}

    for i in range(len(names)):
        hurricanes.update(
            {
                names[i]: {
                    "Name": names[i],
                    "Month": months[i],
                    "Year": years[i],
                    "Max Sustained Wind": max_sustained_winds[i],
                    "Areas Affected": areas_affected[i],
                    "Damages": damages[i],
                    "Deaths": deaths[i],
                }
            }
        )

    return hurricanes


hurricanes_dictionary = hurricanes_dictionary_maker(
    names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths
)


# ------- Iteration 4. ------- #
def hurricanes_by_year_maker(hurricanes_dictionary):
    hurricanes_by_year = {}

    for values in hurricanes_dictionary.values():
        current_year = values["Year"]

        if not current_year in hurricanes_by_year:
            hurricanes_by_year.update({current_year: [values]})
        else:
            hurricanes_by_year[current_year].append(values)

    return hurricanes_by_year


hurricanes_by_year = hurricanes_by_year_maker(hurricanes_dictionary)


# ------- Iteration 5. ------- #
def count_areas_affected(areas_affected):
    counted_areas_affected = {}

    for areas in areas_affected:
        for area in areas:
            if not area in counted_areas_affected:
                counted_areas_affected.update({area: 1})
            else:
                counted_areas_affected[area] += 1

    return counted_areas_affected


counted_areas_affected = count_areas_affected(areas_affected)


# ------- Iteration 6. ------- #
def find_most_affected_area(counted_areas_affected):
    max_area = ""
    max_count = 0

    for key, value in counted_areas_affected.items():
        if value > max_count:
            max_area = key
            max_count = value

    return {max_area: max_count}


most_affected_area = find_most_affected_area(counted_areas_affected)


# ------- Iteration 7. ------- #
def greatest_death_count(hurricanes):
    max_deaths_name = ""
    max_deaths = 0

    for values in hurricanes.values():
        if values["Deaths"] > max_deaths:
            max_deaths_name = values["Name"]
            max_deaths = values["Deaths"]

    return {max_deaths_name: max_deaths}


# ------- Iteration 8. ------- #
def calculate_mortality_scale(hurricanes):
    mortality_scale = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for values in hurricanes.values():
        deaths = values["Deaths"]
        name = values["Name"]

        if deaths <= 0:
            mortality_scale[0].append(name)

        elif deaths <= 100:
            mortality_scale[1].append(name)

        elif deaths <= 500:
            mortality_scale[2].append(name)

        elif deaths <= 1000:
            mortality_scale[3].append(name)

        elif deaths <= 5000:
            mortality_scale[4].append(name)

        elif deaths >= 10000:
            mortality_scale[5].append(name)

    return mortality_scale


# ------- Iteration 9. ------- #
def greatest_death_count(hurricanes):
    max_damage_name = ""
    max_damage = 0

    for values in hurricanes.values():
        if values["Damages"] == "Damages not recorded":
            continue
        elif values["Damages"] > max_damage:
            max_damage_name = values["Name"]
            max_damage = values["Damages"]

    return {max_damage_name: max_damage}


# ------- Iteration 10. ------- #
def calculate_damage_scale(hurricanes):
    damage_scale = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

    for values in hurricanes.values():
        damages = values["Damages"]
        name = values["Name"]

        if damages == "Damages not recorded":
            damage_scale[0].append(name)

        elif damages <= 100000000:
            damage_scale[1].append(name)

        elif damages <= 5000000000:
            damage_scale[2].append(name)

        elif damages <= 10000000000:
            damage_scale[3].append(name)

        elif damages <= 50000000000:
            damage_scale[4].append(name)

        elif damages >= 100000000000:
            damage_scale[5].append(name)

    return damage_scale
