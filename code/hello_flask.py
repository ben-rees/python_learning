# Load the Flask module into your Python script
from flask import Flask
# Create a Flask object called app
app = Flask(__name__)	

# Run the code below this function when someone accesses the root URL of the server
# You could say "/function" and then it would run when someone visits
# http://IP address/function
@app.route("/")

# Defining function
def hello():
# return the string "Hello World!" when the function is called
# to the client's web browser.
    return "Hello World!"

# If this script was run directly from the command line
if __name__ == "__main__":
# Have the server listen on port 80
    app.run(host='0.0.0.0', port=80, debug=True) 
												 # 80 and report any errors.
