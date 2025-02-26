import requests

def convert_currency(amount, from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    data = response.json()
    
    if to_currency in data["rates"]:
        return round(amount * data["rates"][to_currency], 2)
    return "Invalid currency"
