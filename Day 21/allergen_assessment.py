import re

PATTERN = re.compile("(?P<ingredients>.*) \(contains (?P<allergens>.*)\)")


# Parse input
def parse_input(input):
    ingredient_translations = {}
    all_ingredients_count = {}

    for line in input:
        match = re.match(PATTERN, line)
        if match is not None:
            ingredients = match.group("ingredients")
            allergens = match.group("allergens")

            for ingredient in ingredients.split(" "):
                if ingredient in all_ingredients_count:
                    all_ingredients_count[ingredient] += 1
                else:
                    all_ingredients_count[ingredient] = 1

            for allergen in allergens.split(", "):
                if allergen in ingredient_translations:
                    ingredient_translations[allergen].append(ingredients)
                else:
                    ingredient_translations[allergen] = [ingredients]
    return ingredient_translations, all_ingredients_count


def can_contain_allergen(ingredient):
    for allergen in ingredient_translations:
        if all(ingredient in ingredient_list for ingredient_list in ingredient_translations[allergen]):
            return True
    return False


def find_ingredients_without_allergens(all_ingredients_count):
    ingredients_without_allergens = []
    for ingredient in all_ingredients_count:
        if not can_contain_allergen(ingredient):
            ingredients_without_allergens.append(ingredient)
    return ingredients_without_allergens


def get_count(ingredients_without_allergens, all_ingredients_count):
    num_without_allergens = 0
    for ingredient in ingredients_without_allergens:
        num_without_allergens += all_ingredients_count[ingredient]
    return num_without_allergens


with open("Day 21/input.txt") as f:
    input = f.read().splitlines()

# Ingredients have 0 or 1 allergen
# Allergens are in exaclty one ingredient
# Allergens aren't always marked but ingredients are
ingredient_translations, all_ingredients_count = parse_input(input)
ingredients_without_allergens = find_ingredients_without_allergens(all_ingredients_count)
num_without_allergens = get_count(ingredients_without_allergens, all_ingredients_count)
print("Answer to Part 1:")
print(num_without_allergens)


# Part 2
def remove_ingredients(ingredient_translations, list_to_remove):
    for allergen in ingredient_translations:
        ingredient_translations[allergen] = [[x for x in ingredient_list if x not in list_to_remove] for ingredient_list in ingredient_translations[allergen]]
    return ingredient_translations


def map_allergens(ingredient_translations):
    num_allergens = len(ingredient_translations)
    found = {}
    while len(found) < num_allergens:
        for allergen in ingredient_translations:

            curr_possibilities = []
            for ingredient in allergen_ingredients:
                if all(ingredient in ingredient_list for ingredient_list in ingredient_translations[allergen]):
                    curr_possibilities.append(ingredient)

            if len(curr_possibilities) == 1:
                ingredient = curr_possibilities[0]
                found[allergen] = ingredient

                # Remove found allergen from other ingredient lists
                ingredient_translations.pop(allergen)
                ingredient_translations = remove_ingredients(ingredient_translations, [ingredient])
                break
    return found


def get_canonical_dangerous_ingredient_list(allergens_to_ingredients):
    dangerous_list = ""
    for allergen in sorted(allergens_to_ingredients):
        dangerous_list += allergens_to_ingredients[allergen] + ","

    return dangerous_list[:-1]


# Remove ingredients that do not contain allergens
allergen_ingredients = [ingredient for ingredient in all_ingredients_count if ingredient not in ingredients_without_allergens]
for allergen in ingredient_translations:
    ingredient_translations[allergen] = [[x for x in ingredient_list.split(" ")] for ingredient_list in ingredient_translations[allergen]]
ingredient_translations = remove_ingredients(ingredient_translations, ingredients_without_allergens)

# Compose list of dangerous ingredients
allergens_to_ingredients = map_allergens(ingredient_translations)
dangerous_list = get_canonical_dangerous_ingredient_list(allergens_to_ingredients)
print("\nAnswer to Part 2:")
print(dangerous_list)
