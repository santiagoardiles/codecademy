# Python loops: Medical insurance (yes, again, again, again).


names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]


# -------------------- Code for the project. -------------------- #


# ------- Iteration 1. ------- #
total_cost = 0


# ------- Iteration 2. ------- #
for n in actual_insurance_costs:
    total_cost += n


# ------- Iteration 3 and 4. ------- #
average_cost = total_cost / len(actual_insurance_costs)
print(f"Average Insurance Cost: {average_cost} dollars.")


# ------- Iteration 5, 6, and 7. ------- #
for i in range(len(names)):
    name = names[i]
    insurance_cost = actual_insurance_costs[i]

    print(f"\nThe insurance cost for {name} is {insurance_cost} dollars.")

    # ------- Iteration 8 and 9. ------- #
    if insurance_cost > average_cost:
        print(f"The insurance cost for {name} is above average.")
    elif insurance_cost < average_cost:
        print(f"The insurance cost for {name} is below average.")
    else:
        print(f"The insurance cost for {name} is equal to the average.")


# ------- Iteration 10 and 11. ------- #
updated_estimated_costs = [cost * 11 / 10 for cost in estimated_insurance_costs]
print(f"\nThe updated estimated costs are: {updated_estimated_costs}.")
