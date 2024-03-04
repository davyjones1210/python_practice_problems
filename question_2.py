# Write a program that generates a random number between 1 and 15, and prompts the user to guess the number.
# If the user guesses low, the program should say “You’re a little low” and
# if they guess high the program should say “You’re a little high”.
# The program exits with “Good guess!” when the user guesses correctly,
# or with “Thanks for playing!” when -1 is entered to quit.
# The program should only allow for a maximum of 3 guesses, and
# if the user runs out of turns, the program wins saying “You ran out of guesses, the number was: X”.

import random
def generate_random_number():

    # Generating a random number and saving it in a variable
    pick_random_number = random.randint(1, 15)

    # Prompting user
    print("A random number between 1 and 15 has been picked. You have 3 guesses!")


    return pick_random_number
    #print(pick_random_number)


def get_user_inputs(pick_random_number):

    # Initializing some variables for tracking user guesses and if they are true
    user_guess = []
    guess_is_correct = False
    i = 0
    exit_game = -1

    # Keeping looping till no correct guesses have been entered
    while guess_is_correct == False:

    # For loop to indicate start of 3 guesses
        for i in range(0,3):
            # User's guesses are saved in above initialized list

            while True:
                try:
                    user_guess.append(int(input("Please guess the number: ")))
                    break
                except:
                    print("Exception Error: Sorry, input must be an integer number, try again")


            # Checking to see if user's guess matches with the random number picked earlier
            # If the guess is correct, indicate correct guess, change guess_is_correct to 'True' to end the while loop
            # and then break out of the for loop
            if user_guess[i] == pick_random_number:
                guess_is_correct = True
                print("Good guess!")
                #print(i)
                break
            # Else if the user's entry is '-1' then indicate end of game, change guess_is_correct to 'True' to end the while loop
            # and then break out of the for loop
            elif user_guess[i] == exit_game:
                guess_is_correct = True
                print("Thanks for playing!")
                break
            # Else if the user's guess is lower than the randomly picked number, indicate guess is low
            elif user_guess[i] < pick_random_number:
                print("You’re a little low")

            # Else if the user's guess is higher than the randomly picked number, indicate guess is high
            elif user_guess[i] > pick_random_number:
                print("You’re a little high")



        # If 3 guesses have been used up and still no correct number has been guesssed, print out of guesses,
        # print the randomly generated number, change guess_is_correct to 'True' to end the while loop
        # and then break out of the while loop.
        if i > 1 and guess_is_correct == False:

            print("You ran out of guesses, the number was: ", pick_random_number)
            #print(i)
            guess_is_correct = True
            break

def main():
    #start of program
    # rolling of dice after asking user for number of rolls and returning the outcomes of all rolls
    random_number = generate_random_number()
    # analyzing the above rolled dice outcomes and output how many times each number was rolled
    get_user_inputs(random_number)


#main entry point to the program
if __name__ == "__main__":
    main()




