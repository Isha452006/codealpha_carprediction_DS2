import pandas as pd

# Provide the correct file path to your CSV in the Downloads folder
data = pd.read_csv('C:/Users/HP/Downloads/car data.csv')

# Print column names to check if 'Present_Price' and 'Driven_kms' exist
print("Columns in the data:", data.columns)

# Check if the required columns exist in the DataFrame
required_columns = ['Present_Price', 'Driven_kms']  # Update column name here to 'Driven_kms'
if all(col in data.columns for col in required_columns):
    # If both columns exist, select them
    X = data[required_columns]
    print("Selected features:", X.head())
else:
    # If columns are missing, inform the user
    missing_cols = [col for col in required_columns if col not in data.columns]
    print(f"Missing columns: {', '.join(missing_cols)}")

# Example of how to train the model if columns are present
# model = train_model(data)  # Uncomment when ready to train
