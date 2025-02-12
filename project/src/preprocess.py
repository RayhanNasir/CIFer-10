"""
Author: Ibrahim
Descrption: preprocess CIfer-10 datasets

"""

import numpy as np
import cv2, os
import pandas as pd

from sklearn.preprocessing import LabelBinarizer 

#project pakages
from ..import config

x_train= np.ndarray((config.train_sample_num,config.img_size,config.img_size,config.img_channel),dtype=np.float32)

def normalization(x):
	x = np.divide(x, 255.0)
	x = np.subtract(x, 0.5)
	x = np.multiply(x, 2.0)
	
	return x

def load_train_data():
	train_data_dir = os.path.join(config.dataset_path(), "train")
	#print(os.listdir(train_data_dir))
	train_images= sorted(os.listdir(train_data_dir),key=lambda x: int(x.split(".")[0]))
	
	#print(train_images)
	train_images= [os.path.join(train_data_dir,img_path)
		for img_path in train_images]
	#print(train_images)
	
	#loading image labels 
	train_labels_df= pd.read_csv(os.path.join(config.dataset_path(),
				"trainLabels.csv"))
	train_labels= train_labels_df["label"].values

	#one hot encoding
	encoder = LabelBinarizer()
	y_labels= encoder.fit_transform(train_labels)

	print("LOading train images...........")

	#loading images from absulate directory using opencv

	for i, img_dir in enumerate(train_images):
		img = cv2.imread(img_dir)
		img = normalization(img)
		#print(img)
		x_train[i]=img
	return x_train, y_labels


if __name__ == "__main__":
	x,y = load_train_data()
	print(x.shape)
	print(y.shape)
