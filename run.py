from flask import Flask
from flask_restful import Api
import logging

from src.predict import Prediction

app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

api.add_resource(Prediction, "/predictions")
api.add_resource(Diagnosis, "/")

if __name__ == "__main__":
  app.run()