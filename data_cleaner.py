import pandas as pd

# --- Configuration ---
# Define the input and output filenames
# This makes the script easy to modify later
input_filename = 'wbjee_cutoffs.csv'
output_filename = 'wbjee_cutoffs_cleaned.csv'

# --- Main Cleaning Logic ---
def clean_data():
    """
    Reads the raw CSV, cleans the institute names, and saves a new CSV.
    """
    try:
        # 1. Load the dataset
        df = pd.read_csv(input_filename)
        print(f"Successfully loaded '{input_filename}'.")
        print("Original institute names (first 5):")
        print(df['institute'].head().to_string())
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        print("Please make sure it is in the same directory as this script.")
        return # Exit the function if file is not found

    # 2. Clean the 'institute' column
    # The logic: for each name, split the string by the comma and take the first part.
    # .str accessor in pandas applies string operations to the entire column.
    # .split(',', n=1) splits only on the first comma.
    # .str[0] selects the first element of the resulting list (the part before the comma).
    # .strip() removes any accidental leading/trailing whitespace.
    
    df['institute'] = df['institute'].str.split(',', n=1).str[0].str.strip()
    
    print("\nCleaning complete.")
    print("Cleaned institute names (first 5):")
    print(df['institute'].head().to_string())

    # 3. Save the cleaned data to a new file
    # index=False prevents pandas from writing the DataFrame index as a column
    df.to_csv(output_filename, index=False)
    
    print(f"\nSuccess! Cleaned data has been saved to '{output_filename}'.")
    print("You should now use this new file for the predictor.")

# --- Run the Script ---
if __name__ == "__main__":
    clean_data()