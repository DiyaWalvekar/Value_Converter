def convert_volume(value, from_unit, to_unit):
    volume_units = {
        "liter": 1,
        "milliliter": 1000,
        "cubic meter": 0.001,
        "cubic inch": 61.0237,
        "cubic foot": 0.0353147
    }
    
    return value * (volume_units[to_unit] / volume_units[from_unit])
