"""You are in a room with a circle of 100 chairs. The chairs are 

numbered sequentially from 1 to 100.

At some point in time, the person in chair #1 will be asked to 

leave. The person in chair #2 will be skipped, and the person in 

chair #3 will be asked to leave. This pattern of skipping one 

person and asking the next to leave will keep going around the 

circle until there is one person left… the survivor.

Write a program to determine which chair the survivor is sitting in."""

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




