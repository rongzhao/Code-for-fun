"""This is the python code for solving the quiz asked by POPSUGAR."""

"""To run this code, you should have python and numpy library installed in your computer"""

import numpy as np

# Use a loop to keep removing one person from the circle and stop when only one person is left
def skip_one(total_number):
    circle = np.arange(1, total_number + 1)
    people_left = total_number
    index = -total_number
    while people_left > 1:
        circle = np.delete(circle, index)
        people_left = people_left - 1
        index = index + 2
        if index >= 0:
            index = index - people_left
    return circle

def main():
    result = skip_one(100)
    print result

if __name__ == '__main__':
    main()




