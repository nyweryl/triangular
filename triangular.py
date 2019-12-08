#!/usr/bin/env python3

n = int(input("Enter a natural number: "))

if n < 1:
    print("That isn't a natural number.")
else:
    result = int(n * (n + 1) / 2)
    print("The sum of the numbers from 1 to ", n, "is:", result)