from collections import defaultdict, Counter
import re
from loguru import logger
import sys


def parse_input(filename):
    for line in open(filename, 'r'):
        m = re.match('^(.*) \(contains (.*)\)$', line.strip())
        yield m.group(1).split(' '), m.group(2).split(', ')


ingredient_count = Counter()
allergens_ = defaultdict(list)
ingredients_allergens = defaultdict(set)
foods = []
for ingredients, allergens in parse_input(sys.argv[1]):
    foods.append((ingredients, set(allergens)))
    for ingredient in ingredients:
        ingredients_allergens[ingredient] |= set(allergens)
    for allergen in allergens:
        allergens_[allergen].append(set(ingredients))

for ingredients, allergens in foods:
    for ingredient in ingredients:
        ingredient_count[ingredient] += 1
        for allergen in allergens:
            if not all([ingredient in ingredients for ingredients in allergens_[allergen]]):
                logger.info(f'Ingredient {ingredient} cannot contain allergen {allergen}')
                if allergen in ingredients_allergens[ingredient]:
                    ingredients_allergens[ingredient].remove(allergen)

ingredients_without_allergen = [ingredient for ingredient, allergens in ingredients_allergens.items() if not allergens]

print(sum([ingredient_count[ingredient] for ingredient in ingredients_without_allergen]))

ingredients = {ingredient: allergens for ingredient, allergens in ingredients_allergens.items() if allergens}
print(ingredients)

allergens__ = {}
# while ingredients:
#     print(ingredients)
#     for ingredient, allergens in ingredients.copy().items():
#         if len(allergens) == 1:
#             allergens__[list(allergens)[0]] = ingredient
#             logger.info(f'Removing {ingredient}')
#             del ingredients[ingredient]

# {'nlph': {'soy'}, 'jbbsjh': {'soy', 'dairy', 'wheat', 'sesame', 'nuts',
# 'peanuts', 'eggs'}, 'tdmqcl': {'sesame'}, 'cpttmnv': {'shellfish', 'nuts'},
# 'vnjxjg': {'shellfish', 'soy', 'wheat', 'sesame'}, 'ccrbr': {'peanuts'},
# 'mzqjxq': {'soy', 'wheat'}, 'fbtqkzc': {'dairy', 'wheat', 'peanuts'}}

while ingredients:
    for ingredient, allergens in ingredients.copy().items():
        logger.info(f'Looking for ingredient {ingredient}')
        for allergen in allergens:
            logger.info(f'Considering {allergen}')
            if allergen not in {a for i, al in ingredients.items() for a in al if i != ingredient}:
                allergens__[allergen] = ingredient
                logger.info(f'Removing {ingredient}')
                del ingredients[ingredient]

print(allergens__)

for a in sorted(allergens__):
    print(allergens__[a], end=',')
print()

# 'jbbsjh': {'soy', 'eggs', 'nuts', 'wheat', 'sesame', 'dairy', 'peanuts'}
# 'cpttmnv': {'nuts', 'shellfish'}
# 'vnjxjg': {'soy', 'wheat', 'sesame', 'shellfish'}
# 'mzqjxq': {'soy', 'wheat'}
# 'fbtqkzc': {'wheat', 'dairy', 'peanuts'}}

