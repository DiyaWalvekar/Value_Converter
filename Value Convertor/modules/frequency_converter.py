def convert_frequency(amount, from_unit, to_unit):
    conversion_factors = {
        "hertz": 1,
        "kilohertz": 0.001,
        "megahertz": 0.000001,
        "gigahertz": 0.000000001
    }

    if from_unit in conversion_factors and to_unit in conversion_factors:
        return round(amount * (conversion_factors[to_unit] / conversion_factors[from_unit]), 6)
    else:
        return "Invalid conversion"
