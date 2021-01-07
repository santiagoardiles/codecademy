# --------------- Codecademy. --------------- #
#                                             #
#    PATH: Machine Learning.                  #
#    TRACK: Supervised Learning: Regression.  #
#    LESSON: Distance Formula.                #
#                                             #
# --------------- Codecademy. --------------- #


# --------------------
# Euclidean distance.
# --------------------
def euclidean_distance(pt1, pt2):
    distance = 0

    for i in range(len(pt1)):
        distance += (pt1[i] - pt2[i]) ** 2

    return distance ** 0.5


print("\nEuclidean distance:")
print(euclidean_distance([1, 2], [4, 0]))
print(euclidean_distance([5, 4, 3], [1, 7, 9]))


# --------------------
# Manhattan distance.
# --------------------
def manhattan_distance(pt1, pt2):
    distance = 0

    for i in range(len(pt1)):
        distance += abs(pt1[i] - pt2[i])

    return distance


print("\nManhattan distance:")
print(manhattan_distance([1, 2], [4, 0]))
print(manhattan_distance([5, 4, 3], [1, 7, 9]))


# --------------------
# Hamming distance.
# --------------------
def hamming_distance(pt1, pt2):
    distance = 0

    for i in range(len(pt1)):
        if pt1[i] != pt2[i]:
            distance += 1

    return distance


print("\nHamming distance:")
print(hamming_distance([1, 2], [1, 100]))
print(hamming_distance([5, 4, 9], [1, 7, 9]))
print("")
