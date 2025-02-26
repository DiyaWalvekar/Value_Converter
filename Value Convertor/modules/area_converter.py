def convert_area(value, from_unit, to_unit):
    area_units = {
        "square meter": 1,
        "square kilometer": 1e-6,
        "square mile": 3.861e-7,
        "square yard": 1.19599,
        "square foot": 10.7639
    }
    
    return value * (area_units[to_unit] / area_units[from_unit])
