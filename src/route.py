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


class Diagnosis(Resource):
    def get(self):
        return jsonify(diagnoses)


class Prediction(Resource):
    def post(self):

        args = parser.parse_args()

        image_url_1 = str(args['image_url_1'])
        image_url_2 = str(args['image_url_2'])

        data = providePrediction(image_url_1)

        response = jsonify(data)

        response.status_code = 202

        return response


def providePrediction(image_url_1):
    control, case = main(image_url_1)

    prediction = {
                    "with diabetic retinopathy": case,
                    "without diabetic retinopathy": control
                }

    return prediction
