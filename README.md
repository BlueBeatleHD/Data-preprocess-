This is a small starter data cleaning and preprocessing script using python. The script reads a CSV file containing the raw data, drops rows with missing values, removes duplicate rows, and standardizes specified columns to lower case. The cleaned data is then saved to a new CSV file. 

Before you run the script, make sure to change the file paths.

  replace 'path/to/raw_data.csv', 'path/to/cleaned_data.csv', and 'column_to_standardize' with your actual file paths and the column you want to standardize


  1. Read the raw data into a DataFrame.
  2. Handling missing values by dropping rows with any missing values.
  3. Removing duplicate rows.
  4. Standardizing formats.
  5. Save the cleaned data to a new CSV file.
