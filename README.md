# 🚗 Car Price Prediction Web App

This project is a Flask-based web application that predicts the **price of a car** based on various attributes like brand, model year, fuel type, transmission, mileage, engine capacity, and more. The project uses a machine learning model trained on cleaned car and bike data to provide fast, reliable predictions through a clean, user-friendly interface.

---

## 👩‍💻 Project Author
**GitHub Username**: [Isha452006](https://github.com/Isha452006)

---

## 🎯 Project Objective

The goal of this project is to:

- ✅ Predict the price of a used car based on user input
- ✅ Create a web interface using Flask + HTML/CSS
- ✅ Use cleaned data to train a robust ML model
- ✅ Help users, dealers, and buyers estimate resale car values

---

## 🧠 Key Features

- 🚘 Accurate car price prediction using ML
- 📊 Trained on cleaned car & bike dataset
- 🧠 Model: Saved as `car_price_model.pkl`
- 🖥️ HTML + Flask-based front-end interface
- 📄 Dataset: `cleaned_car_bike_data.csv`
- 📈 Data analysis scripts included

---

## 🧱 Project Structure

car-price-prediction/ ├── app.py # Main Flask web server
├── car_anal.py # Data visualization & analysis script 
├── car_bike_analysis.py # Combined car-bike data exploration 
├── car_price_model.pkl # Trained machine learning model 
├── car_price_prediction.py # Script to use model and predict
├── cleaned_car_bike_data.csv # Cleaned dataset used for training 
├── train_model.py # ML training script
├── static/ 
│ └── car_banner.jpg 


---

## 🛠️ Tech Stack

| Layer         | Technologies               |
|---------------|-----------------------------|
| Frontend      | HTML, CSS                  |
| Backend       | Python, Flask              |
| ML/Modeling   | scikit-learn, pandas       |
| Visualization | matplotlib, seaborn (in `car_anal.py`) |
| Model Output  | Pickle (`car_price_model.pkl`) |

---

## 🚀 How to Run This Project

1. **Clone the Repository**

```bash
git clone https://github.com/Isha452006/codealpha_carprediction_DS2
cd car-price-prediction
Install Required Packages
2. **install packages**
pip install -r requirements.txt
Run the Flask App
3. **run code**
python app.py
