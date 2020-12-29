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


# Challenge 3.
def delete_starting_evens(lst):
    for item in lst:
        if item % 2 == 0:
            lst = lst[1:]
        else:
            break

    return lst


# Challenge 4.
def odd_indices(lst):
    new_lst = []

    for idx in range(1, len(lst), 2):
        new_lst.append(lst[idx])

    return new_lst


# Challenge 5.
def exponents(bases, powers):
    answer = []

    for base in bases:
        for power in powers:
            answer.append(base ** power)

    return answer


# Challenge 6.
def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0

    for num in lst1:
        sum1 += num

    for num in lst2:
        sum2 += num

    if sum1 >= sum2:
        return lst1
    else:
        return lst2


# Challenge 7.
def over_nine_thousand(lst):
    count = 0

    for num in lst:
        if count > 9000:
            break
        else:
            count += num

    return count


# Challenge 8.
def max_num(nums):
    greatest = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > greatest:
            greatest = nums[i]

    return greatest


# Challenge 9.
def same_values(lst1, lst2):
    duplicates = []

    for idx1 in range(len(lst1)):
        for idx2 in range(len(lst2)):
            if lst2[idx2] == lst1[idx1] and idx2 == idx1:
                duplicates.append(idx2)

    return duplicates


# Challenge 10.
def reversed_list(lst1, lst2):
    j = len(lst2) - 1

    for i in range(len(lst1)):
        if lst2[j] != lst1[i]:
            return False
        else:
            j -= 1

    return True


# Testing.
print(add_greetings(["Owen", "Max", "Sophie"]))

print(divisible_by_ten([20, 25, 30, 35, 40]))

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

print(odd_indices([4, 3, 7, 10, 11, -2]))

print(exponents([2, 3, 4], [1, 2, 3]))

print(larger_sum([1, 9, 5], [2, 3, 7]))

print(over_nine_thousand([8000, 900, 120, 5000]))

print(max_num([50, -10, 0, 75, 20]))

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
