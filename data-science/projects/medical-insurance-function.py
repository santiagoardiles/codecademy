# Calculates insurance cost.
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    insurance_cost = (
        250 * age
        - 128 * sex
        + 370 * bmi
        + 425 * num_of_children
        + 24000 * smoker
        - 12500
    )

    print(
        "The estimated insurance cost for "
        + name
        + " is "
        + str(insurance_cost)
        + " dollars.\n"
    )

    return insurance_cost


# Calculating...
maria_insurance_cost = calculate_insurance_cost("Maria", 28, 0, 26.2, 3, 0)
omar_insurance_cost = calculate_insurance_cost("Omar", 35, 1, 22.2, 0, 1)
