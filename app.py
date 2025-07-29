import pandas as pd
from flask import Flask, request, jsonify, render_template # <-- ADD render_template
from flask_cors import CORS

# --- 1. Initialize the Flask App ---
app = Flask(__name__) # Flask will now look for the 'templates' folder
CORS(app)

# --- 2. Load and Clean Data ONCE at Startup ---
try:
    df = pd.read_csv('wbjee_cutoffs_cleaned.csv')
    df['category'] = df['category'].str.strip()
    df['quota'] = df['quota'].str.strip()
    print("--- Server Startup: Successfully loaded and cleaned CSV. ---")
except FileNotFoundError:
    print("--- FATAL SERVER ERROR: 'wbjee_cutoffs_cleaned.csv' not found. ---")
    df = pd.DataFrame()

# ======================================================================
# === NEW HOMEPAGE ROUTE TO SERVE YOUR FRONTEND ===
# ======================================================================
@app.route('/')
def home():
    """Serves the main index.html file from the 'templates' folder."""
    print("\n--- Request received for homepage (/), serving index.html ---")
    # render_template looks in the 'templates' folder for the file
    return render_template('index.html')
# ======================================================================


# --- API Endpoint: The Main Prediction Logic ---
@app.route('/predict', methods=['GET'])
def predict():
    # ... This function remains exactly the same ...
    print(f"\n--- New Request Received on /predict ---")
    # (The rest of your predict function code is unchanged)
    rank_str = request.args.get('rank')
    category = request.args.get('category')
    quota = request.args.get('quota')
    if not all([rank_str, category, quota]):
        return jsonify({"error": "Missing parameters."}), 400
    try:
        rank = int(rank_str)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid rank."}), 400
    category = category.strip()
    quota = quota.strip()
    if not df.empty:
        results = df[(df['category'] == category) & (df['quota'] == quota) & (df['closing_rank'] >= rank)].sort_values(by='closing_rank')
        return jsonify(results.to_dict(orient='records'))
    else:
        return jsonify({"error": "Server data not loaded."}), 500


# --- API Endpoint: For Populating Dropdown Options ---
@app.route('/options', methods=['GET'])
def get_options():
    # ... This function remains exactly the same ...
    print("\n--- New Request Received on /options ---")
    if not df.empty:
        categories = sorted(df['category'].unique().tolist())
        quotas = sorted(df['quota'].unique().tolist())
        return jsonify({'categories': categories, 'quotas': quotas})
    else:
        return jsonify({"error": "Server data not loaded."}), 500


# --- API Endpoint: For Dependent Dropdowns ---
@app.route('/mapping', methods=['GET'])
def get_mapping():
    # ... This function remains exactly the same ...
    print("\n--- New Request Received on /mapping ---")
    if not df.empty:
        mapping = df.groupby('quota')['category'].unique().apply(lambda x: sorted(list(x))).to_dict()
        return jsonify(mapping)
    else:
        return jsonify({"error": "Server data not loaded."}), 500


# --- Run the Flask App ---
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')