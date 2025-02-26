def convert_speed(value, from_unit, to_unit):
    conversion_factors = {
        "km/h": 1,
        "m/s": 0.277778,
        "mph": 0.621371,
        "knot": 0.539957
    }

    if from_unit in conversion_factors and to_unit in conversion_factors:
        result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        return round(result, 4)
    else:
        return "Invalid Conversion"
