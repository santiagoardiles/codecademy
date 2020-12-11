# ---------- Initial variables. ---------- #
age = 23
smoker = 0
sex = 1
bmi = 23.0
num_of_children = 0

# ---------- Insurance estimation formula. ---------- #
insurance_cost = (
    250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
)

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")

# ---------- Age Factor. ---------- #
age += 4

new_insurance_cost = (
    250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
)

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(
    "\nThe change in cost of insurance after increasing the age by 4 years is "
    + str(change_in_insurance_cost)
    + " dollars."
)

# ---------- BMI Factor. ---------- #
age -= 4
bmi += 3.1

new_insurance_cost = (
    250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
)

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(
    "\nThe change in cost of insurance after increasing BMI by 3.1 years is "
    + str(change_in_insurance_cost)
    + " dollars."
)

# ---------- Male vs. Female Factor ---------- #
bmi -= 3.1
sex = 0

new_insurance_cost = (
    250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
)

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(
    "\nThe change in cost for being female instead of male is "
    + str(change_in_insurance_cost)
    + " dollars."
)
