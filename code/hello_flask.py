from flask import Flask		# Load the Flask module into your Python script
app = Flask(__name__)		# Create a Flask object called app

@app.route("/")				# Run the code below this function when someone
							# accesses the root URL of the server

def hello():				# Defining function
    return "Hello World!"	# Send the text "Hello World!" to the client's
							# web browser

if __name__ == "__main__":	# If this script was run directly from the
							# command line
    app.run(host='0.0.0.0', port=80, debug=True) # Have the server listen on port
												 # 80 and report any errors.
