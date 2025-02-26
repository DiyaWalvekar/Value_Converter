def convert_calorie(amount, from_unit, to_unit):
    conversion_factors = {
        "calories": 1,
        "kilojoules": 4.184,
        "kilocalories": 0.001,
        "joules": 4.184 * 1000
    }

    if from_unit in conversion_factors and to_unit in conversion_factors:
        return round(amount * (conversion_factors[to_unit] / conversion_factors[from_unit]), 4)
    else:
        return "Invalid conversion"
