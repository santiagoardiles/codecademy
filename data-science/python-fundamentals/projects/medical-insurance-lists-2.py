# Python lists 2: Medical insurance (yes, again, again).

names = [
    "Mohamed",
    "Sara",
    "Xia",
    "Paul",
    "Valentina",
    "Jide",
    "Aaron",
    "Emily",
    "Nikita",
    "Paul",
]

insurance_costs = [
    13262.0,
    4816.0,
    6839.0,
    5054.0,
    14724.0,
    5360.0,
    7640.0,
    6072.0,
    2750.0,
    12064.0,
]


# -------------------- Code for the project. -------------------- #


# ------- Iteration 1. ------- #
names.append("Priscilla")
insurance_costs.append(8320.0)


# ------- Iteration 2 and 3. ------- #
medical_records = list(zip(insurance_costs, names))
print(f"\n{medical_records}")


# ------- Iteration 4 and 5. ------- #
num_medical_records = len(medical_records)
print(f"\nThere are {num_medical_records} medical records.")


# ------- Iteration 6 and 7. ------- #
first_medical_record = medical_records[0]
print(f"\nHere is the first medical record: {first_medical_record}.")


# ------- Iteration 8. ------- #
medical_records.sort()
print(f"\nHere are the medical records sorted by insurance cost: {medical_records}")


# ------- Iteration 9 and 10. ------- #
cheapest_three = medical_records[0:3]
print(f"\nHere are the three cheapest medical records: {cheapest_three}.")


# ------- Iteration 11 and 12. ------- #
priciest_three = medical_records[-3:]
print(
    f"\nHere are the three most expensive insurance costs in our medical records: {priciest_three}"
)

# ------- Iteration 13. ------- #
occurrences_paul = names.count("Paul")
print(
    f"\nThere are {occurrences_paul} individuals with the name Paul in our medical records.\n"
)
