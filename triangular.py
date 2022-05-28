#!/usr/bin/env python3

import argparse
import sys

message_error_incorrect_arguments   = "Incorrect arguments. -h for help."
message_error_not_natural_number    = "Oops, that is not a natural number."
message_input                       = "Enter a natural number (or enter 0 to quit): "
message_goodbye                     = "Goodbye."

def sum(n):
    '''Returns the sum of all numbers [1-n]'''
    return int(n * (n + 1) / 2)

def print_sum(n):
    '''Prints a sum message'''
    print("The sum of the numbers from 1 to", n, "is:", sum(n))

def is_natural_number(number):
    '''Returns whether a number is natural'''
    if (number > 0):
        return True
    else:
        return False

def user_input():
    '''Asks the user for natural numbers and prints them'''
    natural_number_given = False
    
    while (natural_number_given == False):
        try:
            input_number = int(input(message_input))
            if (input_number == 0):
                sys.exit(message_goodbye)
            elif (not(is_natural_number(input_number))):
                print(message_error_not_natural_number)
            else:
                print_sum(input_number)
        except ValueError:
            print(message_error_not_natural_number)
    
def main(argv):
    '''If a number n is given as argument, prints the sum of all numbers [1-n].
    If no argument is given, user input is asked.'''
    
    # Create a command line argument parser.
    parser = argparse.ArgumentParser(prog="triangular", description="Prints the sum of all numbers [1-n]")
    parser.add_argument("-n", dest="number_list", metavar="natural number", type=int, nargs=1, help="a natural number n to sum [1-n]")
    
    # Try to retrieve the number in the number list given in the command line argument.
    # If the number list exists, put it in integer n and check whether it is a natural number.
    if (vars(parser.parse_args())["number_list"]):
        try:
            arg_number = int((vars(parser.parse_args())["number_list"]).pop())
        except:
            sys.exit(message_error_incorrect_arguments)
        if (not is_natural_number(arg_number)):
            sys.exit(message_error_not_natural_number)
        # Print the result.
        print_sum(arg_number)  
            
    # Otherwise, ask for user input.
    else:
        user_input()
        
if __name__ == "__main__":
    main(sys.argv[1:])