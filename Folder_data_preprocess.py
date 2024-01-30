import os
import pandas as pd

def clean_and_preprocess_data(input_folder, output_folder):
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".csv"):  # This process only CSV files
            input_file_path = os.path.join(input_folder, filename)
            output_file_path = os.path.join(output_folder, filename)

            raw_data = pd.read_csv(input_file_path)

            cleaned_data = raw_data.dropna()

            cleaned_data = cleaned_data.drop_duplicates()

            cleaned_data['column_to_standardize'] = cleaned_data['column_to_standardize'].str.lower()

            cleaned_data.to_csv(output_file_path, index=False)

            print(f"Processed file: {filename}")

if __name__ == "__main__":

    #  If you want to run this where the script is located you can use "script_dir = os.path.dirname(os.path.realpath(__file__))"

    input_folder_path = 'path/to/input_folder' ## Input path here, within quotes
    output_folder_path = 'path/to/output_folder' ## Output path here 

    os.makedirs(output_folder_path, exist_ok=True)

    clean_and_preprocess_data(input_folder_path, output_folder_path)

    print("Data cleaning and preprocessing completed for all files in the folder.")


