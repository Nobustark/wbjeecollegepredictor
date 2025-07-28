import pandas as pd
from bs4 import BeautifulSoup

# --- 1. Load the HTML Data ---
# Let's assume your HTML is saved in a file named 'wbjee_data.html'.
# If you were scraping from a live site, you'd use the requests library first.
try:
    with open('wbjee_data.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
except FileNotFoundError:
    print("Error: 'wbjee_data.html' not found. Please save your HTML data in this file.")
    exit()

# --- 2. Parse the HTML with BeautifulSoup ---
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table. If there are multiple tables, you might need a more specific selector.
# For now, let's assume it's the first table.
table = soup.find('table')
if not table:
    print("Error: No <table> tag found in the HTML file.")
    exit()

# --- 3. Extract Data from Table Rows ---
all_rows_data = []
# Find all table rows 'tr' within the table body 'tbody'
for row in table.find_all('tr'):
    # Find all table data cells 'td' in the current row
    cells = row.find_all('td')
    
    # We expect 10 cells based on your example.
    # We only process rows that have the correct number of cells.
    if len(cells) == 10:
        # Extract text from each cell, cleaning up whitespace with .strip()
        serial_no = cells[0].text.strip()
        round_no = cells[1].text.strip()
        institute = cells[2].text.strip()
        program = cells[3].text.strip()
        # We can ignore cells[4] and [5] for now as they seem constant
        quota = cells[6].text.strip()
        category = cells[7].text.strip()
        opening_rank = cells[8].text.strip()
        closing_rank = cells[9].text.strip()

        # Append the extracted data as a dictionary to our list
        all_rows_data.append({
            'round': round_no,
            'institute': institute,
            'program': program,
            'quota': quota,
            'category': category,
            'opening_rank': opening_rank,
            'closing_rank': closing_rank,
        })

print(f"Successfully extracted {len(all_rows_data)} rows of data.")

# --- 4. Clean and Structure the Data with Pandas ---
if all_rows_data:
    # Create a pandas DataFrame from our list of dictionaries
    df = pd.DataFrame(all_rows_data)

    # --- Data Cleaning ---
    # Convert rank columns to numbers. 'coerce' will turn non-numeric values (like 'P') into NaN (Not a Number)
    df['opening_rank'] = pd.to_numeric(df['opening_rank'], errors='coerce')
    df['closing_rank'] = pd.to_numeric(df['closing_rank'], errors='coerce')

    # Drop rows where ranks could not be converted (they are not useful for prediction)
    df.dropna(subset=['opening_rank', 'closing_rank'], inplace=True)

    # Convert ranks to integers
    df['opening_rank'] = df['opening_rank'].astype(int)
    df['closing_rank'] = df['closing_rank'].astype(int)
    
    # Optional: Clean up program names (e.g., remove '(TFW)')
    df['program'] = df['program'].str.replace(' (TFW)', '', regex=False)
    
    print("Data cleaned. Displaying first 5 rows of the structured data:")
    print(df.head())

    # --- 5. Save to a CSV file ---
    output_filename = 'wbjee_cutoffs.csv'
    df.to_csv(output_filename, index=False)
    
    print(f"\nSuccess! Clean data has been saved to '{output_filename}'")
else:
    print("No data was extracted. Please check your HTML file and table structure.")