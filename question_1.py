# Write a program that simulates rolling a six-sided dice a user defined number of times.
# The program keeps track of how many times each number was rolled and then outputs the results.

import random

def roll_of_dice():
    """
        Returns the stored outcome of simulating rolling a six-sided dice, user defined number of times

            Parameters:
             None.

            Returns:
                    history_of_rolls (List): Outcome of all user defined rolls
    """
    print("Let’s roll some dice!")
    while True:
        number_of_rolls = input("Please enter the number of rolls to make: ")
        try:
            val = int(number_of_rolls)
            if val > 0:  # if a positive return the positive int value
                break
            else:  # if not a positive int print message and ask for input again
                print("Negative number: Sorry, input must be a positive integer, try again")
                continue

        except:
            print("Exception Error: Sorry, input must be an integer number, try again")

    history_of_rolls = []
    print("Rolling...")
    # Looping for the above defined number of rolls
    for i in range(0, int(number_of_rolls)):
        #Having an array to store the outcome of rolls of dice simulated by randomly outputting integers between 1 and 6
        history_of_rolls.append(random.randint(1,6))

    # returning outcome of all user defined rolls
    return history_of_rolls


def analyze_roll_of_dice(history) -> None:
    """
        Analyzes the history of simulated dice rolls passed through the array

            Parameters:
                    history (List): History of all the simulated dice rolls

            Returns:
                    None. Prints analysis of simulated dice rolls and ends the program.
    """
    # intializing the list
    arr = history
    # initializing dict to store frequency of each element
    elements_count = {}
    # iterating over the elements for frequency
    for element in arr:
        # checking whether it is in the dict or not
        if element in elements_count:
            # incrementing the count by 1
            elements_count[element] += 1
        else:
            # setting the count to 1
            elements_count[element] = 1

    # Sorting this dictionary into ascending order of key
    sorted_elements_count = dict(sorted(elements_count.items()))

    # Output results of tracking how many times each number was rolled
    for key, value in sorted_elements_count.items():
        print(f"{key} was rolled {value} times")

def roll_snake_eyes() -> None:
    """
        Bonus: A function that tries to roll snake eyes (two 1s) and counts how many rolls it takes to get this result

            Parameters:
                    None

            Returns:
                    None. Prints how many rolls it takes to get this result and ends the program
    """
    print("Trying to roll double 1s...")
    # initializing a few variables to track certain parameters
    did_you_roll_double_1s = False
    history_of_rolls = []
    loop_counter = 0
    #looping until double 1s are rolled
    while did_you_roll_double_1s == False:
        # dice simulator with outcomes stored in history_of_rolls array
        history_of_rolls.append(random.randint(1, 6))
        # if loop to see if dice has been rolled atleast twice to get double 1s
        if loop_counter > 1:
            # if loop to check for double 1s in previous 2 rolls
            if history_of_rolls[loop_counter] == history_of_rolls[loop_counter-1] == 1:
                # output of result when we get double 1s
                print("omg it took ", loop_counter, " rolls to get snake eyes!")

                # changing status of variable to track if double 1s have been rolled to 'True' to exit loop
                did_you_roll_double_1s = True
        # counting up by 1 to track number of rolls
        loop_counter += 1



def main():
    #start of program
    # rolling of dice after asking user for number of rolls and returning the outcomes of all rolls
    history = roll_of_dice()
    # analyzing the above rolled dice outcomes and output how many times each number was rolled
    analyze_roll_of_dice(history)
    # deliberate break in program to mark bonus question
    input("Hit enter to proceed to bonus question. ")
    roll_snake_eyes()

#main entry point to the program
if __name__ == "__main__":
    main()




