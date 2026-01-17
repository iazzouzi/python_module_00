def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    seed_type = seed_type.capitalize()
    if (unit == "packets"):
        print(seed_type, "seeds:", quantity, unit, "available")
    elif (unit == "grams"):
        print(seed_type, "seeds:", quantity, unit, "total")
    elif (unit == "area"):
        print(seed_type, "seeds:", "covers", quantity, "square meters")
    else:
        print("Unknown unit type")
