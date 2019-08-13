import warnings
warnings.filterwarnings("ignore")

import time
import os
import sys
import argparse
import numpy as np
from PIL import Image
from io import BytesIO
import requests

# Import modules from keras
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.preprocessing import image
from keras.backend import manual_variable_initialization
from tensorflow.python.keras.applications.inception_v3 import preprocess_input

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
manual_variable_initialization(True)


def predict(model, img, target_size):

	if img.size != target_size:
		img = img.resize(target_size)

	x = image.img_to_array(img)
	x = np.expand_dims(x, axis=0)
	x = preprocess_input(x)

	clock_initial = time.clock()
	preds = model.predict(x)
	clock_final = time.clock()

	# Class 0: Normal
	# Class 1: With Diabetic Retinopathy

	#print('Class 0:', preds[0,0] * 100., '%')
	#print('Class 1:', preds[0,1] * 100, '%')

	control = np.round(preds[0,0]*100, 2)
	case = np.round(preds[0,1]*100, 2)

	pred = [control, case]

	return pred



def main(image_url_1, image_url_2):
	start_time = time.time()

	target_size = (229, 229)

	model = load_model("src/model.h5")

	preds = []

	for image_url in [image_url_1, image_url_2]:

		response = requests.get(image_url)
		img = Image.open(BytesIO(response.content))

		pred = predict(model, img, target_size)
		preds.append(pred)

	prediction = np.mean(preds, axis=0)

	print("Runtime: ", np.round(time.time() - start_time, 2), " seconds")

	return prediction

