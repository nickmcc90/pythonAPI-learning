from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__) # init app with Flask
api = Api(app) # wrapping the app in an api, initing a restful api

names = {"tim": {"age": 17, "gender": "male"}, "bob": {"age": 70, "gender": "male"}}

class HelloWorld(Resource):  # this class inherits attributes from the Resource class, and we can overwrite things.
  def get(self, name, test): # we can use the input parameter "name" and "test" that people put in the <> in the url.
    return {"name": name, "test": test}
  
  def post(self):
    return {"data": "Posted"}
  
api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")  # here we register the class HelloWorld as a resource. Args: "class", "make it accessible through what url?"


# we only want debug = true in a development environment. DON'T RUN THIS IN A PRODUCT ENVIRONMENT
if __name__ == "__main__":
  app.run(debug=True)