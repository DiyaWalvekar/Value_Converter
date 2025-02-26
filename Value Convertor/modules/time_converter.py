def convert_time(value, from_unit, to_unit):
    conversion_factors = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 86400
    }

    if from_unit in conversion_factors and to_unit in conversion_factors:
        result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        return round(result, 4)
    else:
        return "Invalid Conversion"
