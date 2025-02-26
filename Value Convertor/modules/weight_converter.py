# modules/weight_converter.py

def convert_weight(amount, from_unit, to_unit):
    # Conversion factors (relative to kg)
    conversion_factors = {
        "Kilogram": 1,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Metric Ton": 1000,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }

    # Check if conversion is valid
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        return "Invalid Conversion"

    # Convert from source unit to kg
    amount_in_kg = amount * conversion_factors[from_unit]

    # Convert from kg to target unit
    converted_amount = amount_in_kg / conversion_factors[to_unit]

    return round(converted_amount, 5)
