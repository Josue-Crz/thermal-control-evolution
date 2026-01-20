from flask import Flask, render_template, url_for
import os
import requests

# customize directory of flask application
custom_template_dir = os.path.abspath('/workspaces/themal-control-evolution/src/template')
app = Flask(__name__, template_folder=custom_template_dir)


# FIXME: Make modularity of a POST request function that can be imported and reused via the bridgeArduinoTemplate.py to be called within here
@app.route('/') # scours the template_folder within subdirectory template for index.html
def index():
    target_url = ""
    payload = {"temperature": 22.5, 
               "status": "active", 
               "userSwitchState": True, 
               "POST-Status": "Unknown"}

    # 1. Explicitly define headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "ngrok-skip-browser-warning": "69420" # This bypasses the ngrok splash screen
    }

    # 2. Use requests.post for better readability
    # Adding timeout is also good practice for networked requests
    try:
        response = requests.post(
            target_url, 
            json=payload, 
            headers=headers, 
            timeout=5
        )
        return f"Laptop responded: {response.text}"
    except requests.exceptions.RequestException as e:
        return f"Connection Error: {e}"




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)