# Value Converter

## Overview

This is a **Flask-based Value Converter** that allows users to convert various units including currency, temperature, length, weight, speed, time, area, volume, data storage, calories, frequency, angle, power, pressure, and density.

## Features

- **Currency Conversion** (Uses real-time exchange rates)
- **Temperature Conversion**
- **Length Conversion**
- **Weight Conversion**
- **Speed Conversion**
- **Time Conversion**
- **Area Conversion**
- **Volume Conversion**
- **Data Storage Conversion**
- **Calorie Conversion**
- **Frequency Conversion**
- **Angle Conversion**
- **Power Conversion**
- **Pressure Conversion**
- **Density Conversion**
- **Simple & Responsive UI**

## Tech Stack

- **Frontend**: HTML, CSS
- **Backend**: Flask (Python)
- **API for Currency Conversion**: External API for real-time exchange rates
- **Database**: Not required (as conversions are formula-based)

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/DiyaWalvekar/Value_Converter.git
cd value-converter
```

### 2. Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Run the Flask App

```sh
python app.py
```

The application will run locally at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**.

## Deployment

To deploy the application on platforms like **Render, Railway, or Heroku**, follow these steps:

### **Render Deployment** (Recommended)

1. Push your code to **GitHub**.
2. Go to [Render](https://render.com/) and create a **New Web Service**.
3. Connect your GitHub repository.
4. Set up the **Build Command**:
   ```sh
   pip install -r requirements.txt
   ```
5. Set up the **Start Command**:
   ```sh
   gunicorn app:app
   ```
6. Click **Deploy**.

### **Heroku Deployment** (Alternative)

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. Run the following commands:
   ```sh
   heroku login
   heroku create your-app-name
   git push heroku main
   ```
3. Open the app with:
   ```sh
   heroku open
   ```

## File Structure

```
/value-converter
│── /static                # CSS, JS, Images
│── /templates             # HTML files
│── /modules               # Conversion modules (Python)
│── app.py                 # Main Flask app
│── requirements.txt       # Dependencies
│── Procfile               # For Heroku deployment
│── runtime.txt            # Python version (for Heroku)
│── README.md              # Documentation
```

## Future Improvements

- Add **Dark Mode**
- Integrate **Speech-to-Text Conversion**
- Implement **Real-Time Language Translation**
- Add more unit conversion categories

## License

This project is open-source under the **MIT License**.

---

**Author**: Diya Walvekar
**Contact**: diyawalvekar4321@gmail.com

