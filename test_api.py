import requests # Make sure you have this library: pip install requests

# --- Define the parameters for our test ---
# Using a dictionary like this is the clean, professional way to build a request.
# The 'requests' library will handle encoding the spaces and symbols correctly.
test_params = {
    'rank': 9200,
    'category': 'OBC - A',
    'quota': 'Home State'
}

# The URL of our running Flask server's endpoint
url = "http://127.0.0.1:5000/predict"

print(f"▶️  Sending request to: {url}")
print(f"▶️  With parameters: {test_params}\n")

try:
    # --- Make the GET request ---
    response = requests.get(url, params=test_params)

    # --- Check the results ---
    print(f"◀️  Server responded with status code: {response.status_code}")

    # A status code of 200 means "OK" / Success!
    if response.status_code == 200:
        print("✅ SUCCESS! The server responded correctly.")
        print("\n--- JSON Response ---")
        # .json() automatically converts the JSON text into a Python list/dictionary
        print(response.json())
    else:
        print("❌ FAILURE! The server returned an error.")
        print("\n--- Error Response ---")
        print(response.text)

except requests.exceptions.ConnectionError as e:
    print("\n❌ CONNECTION FAILED. Is the 'app.py' server running?")
    print(f"Error details: {e}")