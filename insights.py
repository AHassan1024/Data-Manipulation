import pandas as pd
from IPython.display import display

# Load the flight data from the CSV file
flight_data = pd.read_csv('mock_flight_data.csv')

# Display the first few rows of the dataset
print("Data Overview:")
display(flight_data.head())

# Check the number of rows and columns in the dataset
print("\nData Shape:")
print(flight_data.shape)

# Check data types and non-null counts for each field
print("\nData Information:")
print(flight_data.info())

# Summary statistics for numeric columns
print("\nSummary Statistics:")
print(flight_data.describe())

# Check for missing values in each column
print("\nMissing Values:")
print(flight_data.isnull().sum())
