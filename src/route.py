#!/usr/bin/python3

import sys
import numpy as np
from random import random

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from json import dumps
import subprocess

from src.predict import main


parser = reqparse.RequestParser()
parser.add_argument('image_url_1', type=str)
parser.add_argument('image_url_2', type=str)


class Prediction(Resource):
    def post(self):

        args = parser.parse_args()

        image_url_1 = str(args['image_url_1'])
        image_url_2 = str(args['image_url_2'])

        print(image_url_1)
        print(image_url_2)

        data = providePrediction(image_url_1, image_url_2)

        response = jsonify(data)

        response.status_code = 202

        return response


def providePrediction(image_url_1, image_url_2):
    pred = main(image_url_1, image_url_2)

    print(pred)

    prediction = {
                    "with diabetic retinopathy": pred[1],
                    "without diabetic retinopathy": pred[0]
                }

    return prediction
