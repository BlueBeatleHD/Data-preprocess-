import pandas as pd

def clean_and_preprocess_data(input_file, output_file):
    raw_data = pd.read_csv(input_file)
    cleaned_data = raw_data.dropna()
    cleaned_data = cleaned_data.drop_duplicates()
    cleaned_data['column_to_standardize'] = cleaned_data['column_to_standardize'].str.lower()
    cleaned_data.to_csv(output_file, index=False)

if __name__ == "__main__": #specify the input and output file path
    input_file_path = 'path/to/raw_data.csv'
    output_file_path = 'path/to/cleaned_data.csv'
    clean_and_preprocess_data(input_file_path, output_file_path)
    print("Data cleaning and preprocessing completed.")
