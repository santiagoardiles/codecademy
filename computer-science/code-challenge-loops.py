# Challenge 1.
def divisible_by_ten(nums):
    count = 0

    for n in nums:
        if n % 10 == 0:
            count += 1

    return count


# Challenge 2.
def add_greetings(names):
    greetings = []

    for name in names:
        greetings.append("Hello, " + name)

    return greetings


# Testing.
print(add_greetings(["Owen", "Max", "Sophie"]))
print(divisible_by_ten([20, 25, 30, 35, 40]))
