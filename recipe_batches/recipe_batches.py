#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # create an empty list bc we dont know what will be in it yet
    batches = []

    # create a for loop of item in recipe
    for item in recipe:
      # if the item is not in the ingredients return 0
        if item not in ingredients:
            return 0

        
        # if the item in the ingredients divided by the item in the recipe is greater than or equal to 1,
        if ingredients[item] // recipe[item] >= 1:

        # then batches appends the item in the ingredients divided by the item in
        # the recipe to find the amount needed for the recipe
          batches.append(ingredients[item] // recipe[item])

        #else, if there's not enough ingredients return 0
        else:
            return 0

    #return the number of batches that can be made
    return min(batches)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 32, 'butter': 150, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))