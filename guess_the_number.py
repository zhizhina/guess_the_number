"""Guess-the-Number Game
Computer randomly chooses a number and guesses it.
"""

import numpy as np


def guess_number(number: int = 1) -> int:
    """Guesses a provided number with binary search algorithm.

    Args:
        number (int, optional): provided number to guess. Defaults to 1.

    Returns:
        int: Attempts count.
    """
    count = 0
    borders = {"min": 0, "max": 100}
    guessed_number = int((borders["min"] + borders["max"]) / 2)

    while True:
        count += 1

        if guessed_number > number:
            borders["max"] = guessed_number - 1
            guessed_number = (borders["max"] + borders["min"]) // 2
        elif guessed_number < number:
            borders["min"] = guessed_number + 1
            guessed_number = (borders["max"] + borders["min"]) // 2
        else:
            break

    return count


def score_game(guess_number) -> int:
    """ Checks how efficient the algorithm is. Finds the average number of attempts in a random list of 100000 numbers from 0 to 100.

    Args:
        guess_number (function): Guessing function.

    Returns:
        int: Average number of attempts.
    """
    count_ls = []

    # setting the random seed for reproducibility
    np.random.seed(1)

    # generating the list of 100000 numbers from 0 to 100
    random_array = np.random.randint(
        1, 101, size=(100000))

    for number in random_array:
        count_ls.append(guess_number(number))

    score = np.mean(count_ls)
    print(f"In average your algorithm guesses a number in {score} attempts")
    return score


score_game(guess_number)
