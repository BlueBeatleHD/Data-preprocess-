import os
import pandas as pd

def clean_and_preprocess_data(input_folder, output_folder, columns_to_standardize):
    try:
        for filename in os.listdir(input_folder):
            if filename.endswith(".csv"):
                input_file_path = os.path.join(input_folder, filename)
                output_file_path = os.path.join(output_folder, filename)

                try:
                    raw_data = pd.read_csv(input_file_path)
                except pd.errors.EmptyDataError:
                    print(f"Error: File '{filename}' is empty. Skipping file.")
                    continue
                except pd.errors.ParserError as e:
                    print(f"Error: Unable to parse file '{filename}'. {e}")
                    continue

                cleaned_data = raw_data.dropna()
                cleaned_data = cleaned_data.drop_duplicates()

                for column in columns_to_standardize:
                    if column in cleaned_data.columns:
                        cleaned_data[column] = cleaned_data[column].str.lower()
                    else:
                        print(f"Warning: Column '{column}' not found in file '{filename}'")

                try:
                    cleaned_data.to_csv(output_file_path, index=False)
                    print(f"Processed file: {filename}")
                except PermissionError:
                    print(f"Error: Permission denied to write file '{output_file_path}'.")
                except Exception as e:
                    print(f"Error: Unable to save file '{output_file_path}'. {e}")

    except OSError as e:
        print(f"Error: Unable to access input folder '{input_folder}' or output folder '{output_folder}'. {e}")

if __name__ == "__main__":
    input_folder_path = 'path/to/input_folder'
    output_folder_path = 'path/to/output_folder'
    columns_to_standardize = ['column1', 'column2', 'column3']

    os.makedirs(output_folder_path, exist_ok=True)
    clean_and_preprocess_data(input_folder_path, output_folder_path, columns_to_standardize)
    print("Data cleaning and preprocessing completed for all files in the folder.")
