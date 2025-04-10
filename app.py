from flask import Flask, render_template, request
from waitress import serve
import joblib
import socket  # Import socket to get the hostname/IP

# Initialize Flask app
app = Flask(__name__)

# Load trained model
model = joblib.load('car_price_model.pkl')  # Update with your model path

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        present_price = float(request.form['present_price'])
        driven_kms = float(request.form['driven_kms'])
        predicted_price = model.predict([[present_price, driven_kms]])
        return render_template('index.html', prediction=predicted_price[0])
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Get the local machine's IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)

    print(f"Starting the server with Waitress...")
    print(f"Access the app at: http://{local_ip}:5000")

    # Run the app with Waitress
    serve(app, host="0.0.0.0", port=5000)
