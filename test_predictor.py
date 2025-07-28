import pandas as pd

def get_user_input(df):
    """Gets and validates user input for rank, category, and quota."""
    
    # 1. Get WBJEE Rank
    while True:
        try:
            rank = int(input("Enter your WBJEE General Merit Rank (GMR): "))
            if rank > 0:
                break
            else:
                print("Please enter a positive number for your rank.")
        except ValueError:
            print("Invalid input. Please enter a number for your rank.")

    # 2. Get User Category
    # Display available categories to the user to avoid typos
    available_categories = sorted(df['category'].unique())
    print("\n--- Select Your Category ---")
    for i, category in enumerate(available_categories):
        print(f"  {i+1}: {category}")
    
    while True:
        try:
            choice = int(input(f"Enter the number for your category (1-{len(available_categories)}): "))
            if 1 <= choice <= len(available_categories):
                category = available_categories[choice - 1]
                break
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 3. Get User Quota
    # Display available quotas
    available_quotas = sorted(df['quota'].unique())
    print("\n--- Select Your Quota ---")
    for i, quota in enumerate(available_quotas):
        print(f"  {i+1}: {quota}")

    while True:
        try:
            choice = int(input(f"Enter the number for your quota (1-{len(available_quotas)}): "))
            if 1 <= choice <= len(available_quotas):
                quota = available_quotas[choice - 1]
                break
            else:
                print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    return rank, category, quota

def find_college_options(df, rank, category, quota):
    """
    Filters the DataFrame to find matching college options based on user input.
    """
    print(f"\nSearching for options with Rank <= {rank}, Category: '{category}', Quota: '{quota}'...")
    
    # The core prediction logic:
    # 1. Filter by the exact category chosen by the user.
    # 2. Filter by the exact quota.
    # 3. Find all rows where the user's rank is within the opening and closing range.
    #    The most important condition is user_rank <= closing_rank.
    
    results = df[
        (df['category'] == category) &
        (df['quota'] == quota) &
        (df['closing_rank'] >= rank)
    ]
    
    # Sort the results to show the most competitive options first (lowest closing rank)
    results = results.sort_values(by='closing_rank')
    
    return results

# --- Main Script Execution ---
if __name__ == "__main__":
    try:
        # Load the data from the CSV file
        data = pd.read_csv('wbjee_cutoffs_cleaned.csv')
        print("Successfully loaded WBJEE cutoff data.")
    except FileNotFoundError:
        print("Error: 'wbjee_cutoffs_cleaned.csv' not found.")
        print("Please make sure the CSV file is in the same directory as this script.")
        exit()

    while True: # Loop to allow multiple searches
        # Get input from the user
        user_rank, user_category, user_quota = get_user_input(data)

        # Find and display the results
        options = find_college_options(data, user_rank, user_category, user_quota)

        if options.empty:
            print("\n----------------- RESULTS -----------------")
            print("Sorry, based on the previous year's data, no options were found for your criteria.")
            print("Consider trying a broader category like 'Open' if applicable.")
            print("-------------------------------------------\n")
        else:
            print("\n----------------- RESULTS: You have a chance in the following colleges -----------------")
            # Set pandas to display all rows without truncation
            pd.set_option('display.max_rows', None)
            # Print only the relevant columns for the user
            print(options[['institute', 'program', 'opening_rank', 'closing_rank']].to_string(index=False))
            print("------------------------------------------------------------------------------------------\n")
        
        # Ask user if they want to search again
        again = input("Do you want to perform another search? (yes/no): ").lower().strip()
        if again != 'yes':
            print("Exiting predictor. Good luck!")
            break