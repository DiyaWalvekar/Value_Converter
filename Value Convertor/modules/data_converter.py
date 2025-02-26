def convert_data(value, from_unit, to_unit):
    data_units = {
        "byte": 1,
        "kilobyte": 1e-3,
        "megabyte": 1e-6,
        "gigabyte": 1e-9,
        "terabyte": 1e-12
    }
    
    return value * (data_units[to_unit] / data_units[from_unit])
