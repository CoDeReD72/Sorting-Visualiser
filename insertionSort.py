import random
import matplotlib.pyplot as plt
import numpy as np

amount = 50  # Sample Size

numbers = [random.randint(0, 1000) for _ in range(amount)]


def animate():
    plt.pause(0.01)
    plt.clf()


def insertionSort(numList):
    # Traverse through 1 to len(numList)
    for i in range(1, len(numList)):
        key = numList[i]

        # Move elements of numList[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < numList[j]:
            numList[j+1] = numList[j]
            j -= 1
        numList[j+1] = key

        plt.bar(list(range(amount)), numList)
        animate()


insertionSort(numbers)
