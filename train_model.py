import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load your data (update the file path to your actual file location)
data = pd.read_csv('C:/Users/HP/Downloads/car data.csv')  # Adjust path to your actual file

# Select features (adjust based on your dataset)
X = data[['Present_Price', 'Driven_kms']]  # Features
y = data['Selling_Price']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model (using Linear Regression as an example)
model = LinearRegression()
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'car_price_model.pkl')  # This will create a 'car_price_model.pkl' file in the current directory

print("Model saved successfully.")
