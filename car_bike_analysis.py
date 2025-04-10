import pandas as pd

# Step 1: Load the dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
# Step 2: Clean the dataset
def clean_data(data):
    print("Cleaning data...")

    # Check for missing values
    missing_values = data.isnull().sum()
    print("Missing values in each column:")
    print(missing_values)

    # Drop rows with missing values
    data.dropna(inplace=True)

    # Ensure correct data types
    # Try to convert columns that should be numeric to numeric, and coerce errors to NaN
    data['Selling_Price'] = pd.to_numeric(data['Selling_Price'], errors='coerce')
    data['Present_Price'] = pd.to_numeric(data['Present_Price'], errors='coerce')
    data['Driven_kms'] = pd.to_numeric(data['Driven_kms'], errors='coerce')

    # Check if the conversion worked
    print("Data types after conversion:")
    print(data.dtypes)

    # Remove outliers (optional step)
    data = data[data['Selling_Price'] < data['Selling_Price'].quantile(0.95)]  # Remove top 5% outliers in price

    return data


# Step 3: Analyze the data
def analyze_data(data):
    print("Performing basic analysis...")

    # Display basic statistical summary
    print("\nStatistical Summary:")
    print(data.describe())

    # Calculate additional columns, e.g., price difference
    data['Price_Difference'] = data['Present_Price'] - data['Selling_Price']
    print("\nPrice Difference column added.")

    # Filter numeric columns before calculating correlation
    numeric_data = data.select_dtypes(include=['number'])

    # Check correlation between numeric columns
    print("\nCorrelation between numerical columns:")
    print(numeric_data.corr())


# Main function to execute the steps
def main():
    file_path = r'C:\Users\HP\Downloads\car data.csv'  # Replace with the correct file path
    data = load_data(file_path)

    if data is not None:
        # Clean the data
        data = clean_data(data)

        # Analyze the data
        analyze_data(data)

        # Optional: Save the cleaned data to a new CSV file
        data.to_csv('cleaned_car_bike_data.csv', index=False)
        print("Cleaned data saved as 'cleaned_car_bike_data.csv'.")

# Run the script
if __name__ == "__main__":
    main()
