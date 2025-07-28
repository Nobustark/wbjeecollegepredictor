import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS # Import the CORS library

# --- 1. Initialize the Flask App ---
app = Flask(__name__)

# --- 2. Enable CORS (Cross-Origin Resource Sharing) ---
# This is essential for allowing your HTML file (frontend) to make requests
# to this server (backend) without being blocked by browser security policies.
CORS(app)

# --- 3. Load and Clean Data ONCE at Startup ---
try:
    # Load the base CSV
    df = pd.read_csv('wbjee_cutoffs_cleaned.csv')
    
    # Proactive Data Cleaning: Remove leading/trailing spaces from key columns
    df['category'] = df['category'].str.strip()
    df['quota'] = df['quota'].str.strip()
    
    print("--- Server Startup: Successfully loaded and cleaned 'wbjee_cutoffs_cleaned.csv'. ---")

except FileNotFoundError:
    print("--- FATAL SERVER ERROR: 'wbjee_cutoffs_cleaned.csv' not found. ---")
    df = pd.DataFrame()


# --- 4. The Main Prediction Endpoint ---
@app.route('/predict', methods=['GET'])
def predict():
    print(f"\n--- New Request Received on /predict ---")
    print(f"DEBUG: Raw request arguments: {request.args}")
    
    rank_str = request.args.get('rank')
    category = request.args.get('category')
    quota = request.args.get('quota')
    
    if not all([rank_str, category, quota]):
        error_message = {"error": "Missing parameters. Please provide 'rank', 'category', and 'quota'."}
        return jsonify(error_message), 400
        
    try:
        rank = int(rank_str)
    except (ValueError, TypeError):
        error_message = {"error": "Invalid rank. Rank must be a whole number."}
        return jsonify(error_message), 400

    category = category.strip()
    quota = quota.strip()

    print(f"INFO: Searching for Rank <= {rank}, Category = '{category}', Quota = '{quota}'")

    if not df.empty:
        results = df[
            (df['category'] == category) &
            (df['quota'] == quota) &
            (df['closing_rank'] >= rank)
        ].sort_values(by='closing_rank')
        
        results_json = results.to_dict(orient='records')
        print(f"SUCCESS: Found {len(results_json)} results.")
        return jsonify(results_json)
    else:
        error_message = {"error": "Server data is not loaded. Check server logs."}
        return jsonify(error_message), 500


# --- 5. The Endpoint for Populating Dropdown Options ---
@app.route('/options', methods=['GET'])
def get_options():
    """Provides a list of unique categories and quotas for the dropdowns."""
    print("\n--- New Request Received on /options ---")
    if not df.empty:
        categories = sorted(df['category'].unique().tolist())
        quotas = sorted(df['quota'].unique().tolist())
        
        response = {
            'categories': categories,
            'quotas': quotas
        }
        print(f"SUCCESS: Sending dropdown options.")
        return jsonify(response)
    else:
        return jsonify({"error": "Server data not loaded."}), 500

# ADD THIS NEW FUNCTION TO app.py

@app.route('/mapping', methods=['GET'])
def get_mapping():
    """Provides a mapping of which categories are valid for each quota."""
    print("\n--- New Request Received on /mapping ---")
    if not df.empty:
        # This groups the data by 'quota', and for each quota, it creates a
        # unique, sorted list of all associated 'category' values.
        mapping = df.groupby('quota')['category'].unique().apply(lambda x: sorted(list(x))).to_dict()
        
        print(f"SUCCESS: Sending quota-to-category mapping.")
        return jsonify(mapping)
    else:
        return jsonify({"error": "Server data not loaded."}), 500

# --- 6. Run the Flask App ---
if __name__ == '__main__':
    # host='0.0.0.0' makes the server accessible from other devices on your network
    app.run(debug=True, host='0.0.0.0')