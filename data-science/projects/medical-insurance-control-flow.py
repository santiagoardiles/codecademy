import os

# Checks for smoker status.
def analyse_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")


# Checks for obesity status.
def analyse_bmi(bmi_value):
    if bmi_value > 30:
        print(
            "Your BMI is in the obese range. To lower your cost, you should significantly lower your BMI."
        )
    elif bmi_value >= 25 and bmi_value <= 30:
        print(
            "Your BMI is in the overweight range. To lower your cost, you should lower your BMI."
        )
    elif bmi_value >= 18.5 and bmi_value < 25:
        print("Your BMI is in a healthy range.")
    else:
        print(
            "Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health."
        )


# Calculates insurance cost.
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = (
        250 * age
        - 128 * sex
        + 370 * bmi
        + 425 * num_of_children
        + 24000 * smoker
        - 12500
    )

    # Clears the terminal.
    os.system("clear")

    print(
        "\n"
        + name
        + "'s Estimated Insurance Cost: "
        + str(estimated_cost)
        + " dollars.\n"
    )

    analyse_smoker(smoker)
    print("")

    analyse_bmi(bmi)
    print("")

    return estimated_cost


# Estimates Keanu's insurance cost.
keanu_insurance_cost = estimate_insurance_cost(
    name="Keanu", age=29, sex=1, bmi=26.2, num_of_children=3, smoker=1
)
