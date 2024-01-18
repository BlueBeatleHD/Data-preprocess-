import pandas as pd

def clean_and_preprocess_data(input_file, output_file):
    # Read the raw data into a DataFrame
    raw_data = pd.read_csv(input_file)

    # Handling missing values by dropping rows with any missing values
    cleaned_data = raw_data.dropna()

    # Removing duplicate rows
    cleaned_data = cleaned_data.drop_duplicates()

    # Standardizing formats (e.g., converting text to lowercase)
    cleaned_data['column_to_standardize'] = cleaned_data['column_to_standardize'].str.lower()

    # Save the cleaned data to a new CSV file
    cleaned_data.to_csv(output_file, index=False)

if __name__ == "__main__":
    # Specify the input and output file paths
    input_file_path = 'path/to/raw_data.csv'
    output_file_path = 'path/to/cleaned_data.csv'

    # Call the function to clean and preprocess the data
    clean_and_preprocess_data(input_file_path, output_file_path)

    print("Data cleaning and preprocessing completed.")
