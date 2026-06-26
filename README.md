# Laptop Price Prediction

This project is a Machine Learning-based web application that predicts the price of laptops based on their specifications. The model is trained on laptop datasets and provides an estimated price based on user inputs.

## Features

* Predicts laptop prices accurately.
* Simple and user-friendly web interface.
* Machine Learning model for price prediction.
* Supports different laptop brands and specifications.
* Instant price prediction.

## Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* Joblib
* HTML
* CSS

## Input Parameters

* Company
* Laptop Type
* RAM
* Weight
* IPS Display
* Screen Size
* Screen Resolution
* CPU
* Memory
* GPU
* Operating System

## Output

* Predicted price of the laptop.

## Project Structure

```
Laptop-Price-Prediction/
│── Data/
│   └── laptop_data.csv
│
│── Model/
│   └── RandomForestRegressor.lb
│
│── static/
│   ├── css/
│       └── style.css
│
│── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── project.html
│
│── app.py
│── requirements.txt
│── README.md
```

## How to Run

1. Clone the repository.
2. Install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:

   ```bash
   python app.py
   ```
4. Open your browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

## Author

**Krishan**
