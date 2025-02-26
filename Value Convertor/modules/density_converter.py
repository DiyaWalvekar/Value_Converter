def convert_density(value, from_unit, to_unit):
    # Density conversion factors (relative to kg/m³)
    density_units = {
        "kg/m³": 1,
        "g/cm³": 1000,
        "lb/ft³": 16.0185,
        "lb/in³": 27679.9,
        "oz/in³": 1729.99,
        "g/L": 1,
        "mg/m³": 0.001,
        "g/m³": 1,
        "kg/L": 1000
    }

    if from_unit not in density_units or to_unit not in density_units:
        return "Invalid unit!"

    # Convert input value to kg/m³
    value_in_kgm3 = value / density_units[from_unit]

    # Convert to target unit
    converted_value = value_in_kgm3 * density_units[to_unit]

    return round(converted_value, 6)
