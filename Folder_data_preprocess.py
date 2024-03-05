import os
import pandas as pd

def clean_and_preprocess_data(input_folder, output_folder, columns_to_standardize):
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            raw_data = pd.read_csv(input_file_path)
            cleaned_data = raw_data.dropna()
            cleaned_data = cleaned_data.drop_duplicates()

            for column in columns_to_standardize:
                if column in cleaned_data.columns:
                    cleaned_data[column] = cleaned_data[column].str.lower()
                else:
                    print(f"Warning: Column '{column}' not found in file '{filename}'")

            cleaned_data.to_csv(output_file_path, index=False)
            print(f"Processed file: {filename}")

if __name__ == "__main__":
    input_folder_path = 'path/to/input_folder'
    output_folder_path = 'path/to/output_folder'
    columns_to_standardize = ['column1', 'column2', 'column3']  # Specify columns here

    os.makedirs(output_folder_path, exist_ok=True)
    clean_and_preprocess_data(input_folder_path, output_folder_path, columns_to_standardize)
    print("Data cleaning and preprocessing completed for all files in the folder.")
