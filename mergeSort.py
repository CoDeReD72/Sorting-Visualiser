import random
import matplotlib.pyplot as plt
import numpy as np

amount = 100

numbers = [random.randint(0, 1000) for _ in range(amount)]


def animate():
    plt.pause(0.01)  # Refresh of Animation
    plt.clf()  # Clear Figure


def merge_sort(numList, left, right):
    if left >= right:  # Recursive Base Case
        return

    midpoint = (left + right) // 2

    plt.bar(list(range(amount)), numList)
    animate()

    # Recursively split into halves
    merge_sort(numList, left, midpoint)
    merge_sort(numList, midpoint + 1, right)

    # Merge the two results
    merge(numList, left, right, midpoint)

    plt.bar(list(range(amount)), numList)
    animate()


def merge(numList, left, right, midpoint):

    left_cpy = numList[left: midpoint + 1]
    right_cpy = numList[midpoint + 1: right + 1]

    l_counter, r_counter = 0, 0
    sorted_counter = left

    while l_counter < len(left_cpy) and r_counter < len(right_cpy):
        if left_cpy[l_counter] <= right_cpy[r_counter]:
            numList[sorted_counter] = left_cpy[l_counter]
            l_counter += 1

        else:
            numList[sorted_counter] = right_cpy[r_counter]
            r_counter += 1

        sorted_counter += 1

    while l_counter < len(left_cpy):
        numList[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
        sorted_counter += 1

    while r_counter < len(right_cpy):
        numList[sorted_counter] = right_cpy[r_counter]
        r_counter += 1
        sorted_counter += 1


print(numbers)
merge_sort(numbers, 0, len(numbers) - 1)
print(numbers)
plt.bar(list(range(amount)), numbers)
plt.show()
