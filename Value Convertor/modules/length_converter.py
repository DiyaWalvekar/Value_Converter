def convert_length(value, from_unit, to_unit):
    conversion_rates = {
        "meters": 1,  # Base unit
        "kilometers": 0.001,
        "miles": 0.000621371,
        "centimeters": 100
    }

    # Convert input to lowercase for consistency
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value  # No conversion needed

    if from_unit in conversion_rates and to_unit in conversion_rates:
        value_in_meters = value / conversion_rates[from_unit]  # Convert to meters first
        converted_value = value_in_meters * conversion_rates[to_unit]  # Convert to target unit
        return round(converted_value, 6)  # Round to 6 decimal places

    return "Invalid Conversion"
