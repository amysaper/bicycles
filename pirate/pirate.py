import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def question():
  """I ask the user what types of drinks he or she likes and return a dictionary of the     results"""
  recipe = {
    "strong": False,
    "salty": False,
    "bitter": False,
    "sweet": False,
    "fruity": False,
  }
  for descriptor in questions:
    print (descriptor)
    favorite = raw_input (questions[descriptor])
    if favorite == "y" or favorite == "yes":
     recipe[descriptor] = True
  print recipe
  return recipe

def drinkmaker(recipe):
  """Based on the drinker's favs, concocts his or her ideal drink."""
  drink= []
  for ingredient in recipe:
    if recipe[ingredient]:
      drink.append(random.choice(ingredients[ingredient]))
  print drink
  return drink

if __name__=='__main__':
  print ("running question function")
  recipe = question()
  drink = drinkmaker(recipe)
  print drink
              