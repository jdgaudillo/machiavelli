from flask import Flask
from flask_restful import Api

from src.predict import Prediction

app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

api.add_resource(Prediction, "/predictions")

if __name__ == "__main__":
  app.run()