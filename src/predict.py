#!/usr/bin/python3

import sys
import numpy as np
from random import random

from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from json import dumps
import subprocess


diagnoses = [
    {'image_url':'https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Fundus_photograph_of_normal_left_eye.jpg/250px-Fundus_photograph_of_normal_left_eye.jpg',
    'case_pred': 90.0,
    'control_pred': 10.0},
    {'image_url':'http://www.njvision.net/wp-content/uploads/2015/05/faaea6a30b6bc45994eb59cf2062b659-300x300.jpg',
    'case_pred': 89.0,
    'control_pred': 11.0},
    {'image_url':'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Retinography.jpg/220px-Retinography.jpg',
    'case_pred': 98.0,
    'control_pred': 2.0}
]


parser = reqparse.RequestParser()
parser.add_argument('image_url', type=str)


class Prediction(Resource):
    def post(self):

        args = parser.parse_args()

        image_url = str(args['image_url'])


        data = predict()

        response = jsonify(data)

        response.status_code = 202

        return response


def predict():
    case_pred = np.round(random()*100., 2)
    control_pred = np.round(100. - case_pred,2)

    pred_dict = {
                "with_macular_degeneration": case_pred,
                "without_macular_degeneration": control_pred
                }

    return pred_dict