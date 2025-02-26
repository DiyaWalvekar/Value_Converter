def convert_angle(value, from_unit, to_unit):
    conversion_factors = {
        "Degree": {"Degree": 1, "Radian": 0.0174533, "Gradian": 1.11111},
        "Radian": {"Degree": 57.2958, "Radian": 1, "Gradian": 63.66198},
        "Gradian": {"Degree": 0.9, "Radian": 0.0157079, "Gradian": 1}
    }
    return round(value * conversion_factors[from_unit][to_unit], 4)
