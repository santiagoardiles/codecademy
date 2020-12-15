# ----- Codecademy ----- #

# Python Fundamentals
# Python Dictionaries
# Project: Medical Insurance


# -------------------- Code for the project. -------------------- #


# ------- Iteration 1, 2, 3, and 4. ------- #
medical_costs = {}

medical_costs.update({"Marina": 6607.0, "Vinay": 3225.0})
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})

print(medical_costs)


# ------- Iteration 5. ------- #
medical_costs["Vinay"] = 3325.0
print(medical_costs)


# ------- Iteration 6 and 7. ------- #
total_cost = 0

for value in medical_costs.values():
    total_cost += value

average_cost = total_cost / len(medical_costs)
print(f"Average Insurance Cost: {average_cost}")


# ------- Iteration 8 and 9. ------- #
names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)

# ------- Iteration 10. ------- #
names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)


# ------- Iteration 11. ------- #
marina_age = names_to_ages.get("Marina", None)
print(f"Marina's age is {marina_age}")


# ------- Iteration 12, 13, 14, and 15. ------- #
medical_records = {}

medical_records.update(
    {
        "Marina": {
            "Age": 27,
            "Sex": "Female",
            "BMI": 31.1,
            "Children": 2,
            "Smoker": "Non-smoker",
            "Insurance_cost": 6607.0,
        }
    }
)

medical_records.update(
    {
        "Vinay": {
            "Age": 24,
            "Sex": "Male",
            "BMI": 26.9,
            "Children": 0,
            "Smoker": "Non-smoker",
            "Insurance_cost": 3225.0,
        }
    }
)

medical_records.update(
    {
        "Connie": {
            "Age": 43,
            "Sex": "Female",
            "BMI": 25.3,
            "Children": 3,
            "Smoker": "Non-smoker",
            "Insurance_cost": 8886.0,
        }
    }
)

medical_records.update(
    {
        "Isaac": {
            "Age": 35,
            "Sex": "Male",
            "BMI": 20.6,
            "Children": 4,
            "Smoker": "Smoker",
            "Insurance_cost": 16444.0,
        }
    }
)

medical_records.update(
    {
        "Valentina": {
            "Age": 52,
            "Sex": "Female",
            "BMI": 18.7,
            "Children": 1,
            "Smoker": "Non-smoker",
            "Insurance_cost": 6420.0,
        }
    }
)

print(medical_records)


# ------- Iteration 16. ------- #
print(
    "Connie's insurance cost is "
    + str(medical_records["Connie"]["Insurance_cost"])
    + " dollars."
)


# ------- Iteration 17. ------- #
medical_records.pop("Vinay")


# ------- Iteration 18. ------- #
for patient, record in medical_records.items():
    name = patient
    age = record["Age"]
    sex = record["Sex"]
    smoker = record["Smoker"]
    bmi = record["BMI"]
    insurance_cost = record["Insurance_cost"]

    print(
        f"\n{name} is a {age} year old {sex} {smoker} with a BMI of {bmi} and insurance cost of {insurance_cost}"
    )
