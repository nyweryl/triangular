#!/usr/bin/env python3

import argparse
import sys

error_message_incorrect_arguments   = "Incorrect arguments. -h for help."
error_message_not_natural_number    = "Oops, that is not a natural number."

def sum(n):
    '''Returns the sum of all numbers [1-n]'''
    return int(n * (n + 1) / 2)

def is_natural_number(number):
    '''Returns whether a number is natural'''
    if (number > 0):
        return True
    else:
        return False

def user_input():
    '''Asks the user for a natural number'''
    natural_number_given = False
    
    while (natural_number_given == False):
        try:
            input_number = int(input("Enter a natural number: "))
            if (is_natural_number(input_number)):
                natural_number_given = True
            else:
                print(error_message_not_natural_number)
        except ValueError:
            print(error_message_not_natural_number)
            
    return input_number
    
def main(argv):
    '''Prints the sum of all numbers [1-n], where n is either a given argument or live input'''
    
    # Create a command line argument parser.
    parser = argparse.ArgumentParser(prog="triangular", description="Prints the sum of all numbers [1-n]")
    parser.add_argument("-n", dest="number_list", metavar="natural number", type=int, nargs=1, help="a natural number n to sum [1-n]")
    
    # Try to retrieve the number in the number list given in the command line argument.
    # If the number list exists, put it in integer n and check whether it is a natural number.
    if (vars(parser.parse_args())["number_list"]):
        try:
            n = int((vars(parser.parse_args())["number_list"]).pop())
        except:
            sys.exit(error_message_incorrect_arguments)
        if (not is_natural_number(n)):
            sys.exit(error_message_not_natural_number)
    # Otherwise, ask for user input.
    else:
        n = user_input()
    
    # Print the result.
    print("The sum of the numbers from 1 to", n, "is:", sum(n))
        
if __name__ == "__main__":
    main(sys.argv[1:])