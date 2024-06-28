from flask import Flask, request, jsonify

app = Flask(__name__)   # needed for initialization


#let's create a route, also called an endpoint to get data from

@app.route("/")   # to make this route accessible we add a decorater "@" with the path we want to access in a string.
def home():   # route
  return "Home"  # data we want user to have access to when they reach this route


if __name__ == "__main__":    # needed for initialization
  app.run(debug=True)