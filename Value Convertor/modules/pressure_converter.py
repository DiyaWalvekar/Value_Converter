def convert_pressure(value, from_unit, to_unit):
    conversion_factors = {
        "Pascal": {"Pascal": 1, "Bar": 1e-5, "Atmosphere": 9.8692e-6},
        "Bar": {"Pascal": 100000, "Bar": 1, "Atmosphere": 0.986923},
        "Atmosphere": {"Pascal": 101325, "Bar": 1.01325, "Atmosphere": 1}
    }
    return round(value * conversion_factors[from_unit][to_unit], 4)
