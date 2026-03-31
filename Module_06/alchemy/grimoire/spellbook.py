from .validator import validate_ingredients


def record_spell(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)

    tmp = result.split("-")[1].strip()
    if tmp == "VALID":
        return f"Spell recorded: {spell_name} ({result})"
    else:
        return f"Spell rejected: {spell_name} ({result})"
