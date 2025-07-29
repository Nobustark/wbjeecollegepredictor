# csv_to_json.py
import pandas as pd
import json

# Define the input and output filenames
input_csv = 'wbjee_cutoffs_cleaned.csv'
output_js = 'database.js'

print(f"Reading data from '{input_csv}'...")

# Read the cleaned CSV file into a pandas DataFrame
df = pd.read_csv(input_csv)

# Convert the DataFrame to a list of dictionaries (which is valid JSON)
# orient='records' is the key here
data_list = df.to_dict(orient='records')

print(f"Successfully converted {len(data_list)} rows.")

# Create the JavaScript file content by assigning the data to a variable
# This makes it super easy to use in our HTML file
js_content = f"const wbjeeData = {json.dumps(data_list, indent=2)};"

# Write the content to the output .js file
with open(output_js, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"\nSuccess! Data has been saved to '{output_js}'.")
print("You can now use this file in your index.html.")