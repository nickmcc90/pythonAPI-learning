from flask import Flask, request, jsonify

app = Flask(__name__)   # needed for initialization


#let's create a route, also called an endpoint to get data from

@app.route("/")   # to make this route accessible we add a decorater "@" with the path we want to access in a string.
def home():   # route
  return "Home"  # data we want user to have access to when they reach this route

####

#let's create a more complicated GET route.
@app.route("/get-user/<user_id>") # the <> variable is known as a path parameter. Read more in notes.txt
def get_user(user_id):  # the parameter in here matches the one in the url
  user_data = {
    "user_id": user_id,
    "name": "John Doe",
    "email": "johndoe@example.com"
  }

  # when we are accessing a route we can a query parameter. This is an extra value included in the main path.
  # this would be like if the path was "/get-user/123?extra=hello world"
  # the question mark is necessary for query requests.
  
  #args stores all the query parameters in a dictionary.
  extra = request.args.get("extra")

  # if extra exists... 
  if extra:
    user_data["extra"] = extra

  # whenever we return data from an api, we use JSON.
  return jsonify(user_data), 200


####

#POST method
@app.route("/create-user", methods=["POST"])
def create_user():

  #if request.method == "POST"
  # we would only include the above statement if we had multiple methods in the array.

  # gets all the json that was passed in the body of the request
  data = request.get_json()

  # maybe some code here that adds this info to a database.

  # we return the data back to let the user know it was created successfully?
  return jsonify(data), 201



if __name__ == "__main__":    # needed for initialization
  app.run(debug=True)