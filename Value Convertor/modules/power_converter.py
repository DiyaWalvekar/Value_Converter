def convert_power(value, from_unit, to_unit):
    conversion_factors = {
        "Watt": {"Watt": 1, "Kilowatt": 0.001, "Horsepower": 0.00134102},
        "Kilowatt": {"Watt": 1000, "Kilowatt": 1, "Horsepower": 1.34102},
        "Horsepower": {"Watt": 745.7, "Kilowatt": 0.7457, "Horsepower": 1}
    }
    return round(value * conversion_factors[from_unit][to_unit], 4)
