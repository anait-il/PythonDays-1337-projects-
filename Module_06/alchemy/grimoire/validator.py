
def validate_ingredients(ingredients: str) -> str:
    ings = ingredients.split()
    ing_list = ["fire", "water", "earth","air"]
    for ingredient in  ings:
        if ingredient not in ing_list:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
