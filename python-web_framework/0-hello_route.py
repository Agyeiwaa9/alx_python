from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the root URL ("/") with the option strict_slashes=False
@app.route('/', strict_slashes=False)
def hello():
    """Route handler for the root URL.
    
    Returns:
        str: The message "Hello HBNB!" to be displayed on the webpage.
    """
    return "Hello HBNB!"

# Run the Flask app when the script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
