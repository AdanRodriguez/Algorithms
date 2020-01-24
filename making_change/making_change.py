#!/usr/bin/python

import sys

def making_change(amount, denominations, cache = 0):
  ways = [0 for i in range(amount + 1)]

  #base case
  ways[0] = 1

  #for loop -> for value in denominations, return amount of ways
  for value in denominations:
    # for a given coin, loop through all of the higher amounts between our coin and
    # the amount (i.e., `for higher_amount in range(coin, amount + 1)`)
    # for loop2 -> for the higher_amount in range(1, amount + 1)
    for higher_amount in range(1, amount + 1):
       # if the denom is less than or equal to the current amount
        if value <= higher_amount:
            # Take the difference between the higher amount and the value of coin
            # start building up the values in cache.
            # then increment at the amount's position in ways
            ways[higher_amount] += ways[higher_amount - value]

  return ways[amount]




if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")