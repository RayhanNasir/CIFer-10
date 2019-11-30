"""
Author: Toriq, Mohammad Ibrahim, rayhan

Desc: Network architecture for classifing cifer-10 dataset images

"""

import keras, os
from keras.layers import (Dense, Activation, Flatten, Conv2D, MaxPooling2D, Dropout, BatchNormalization)
from keras.models import Sequential, load_model
from keras.callbacks import ModelCheckpoint, EarlyStopping

from keras.utils import np_utils


from keras.layers import Conv2D, MaxPooling2D

from keras import regularizers
from keras.callbacks import LearningRateScheduler
# project modules 

from ..import config

model_checkpoint_dir = os.path.join(config.checkpoint_path(), "baseline.h5")
saved_model_dir = os.path.join(config.output_path(), "baseline.h5")

# definning CNN model
weight_decay = 1e-4
def get_model():
	model = Sequential()

	model.add(Conv2D(32, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay), input_shape = config.img_shape))
	model.add(Activation('elu'))

	model.add(BatchNormalization())
	model.add(Conv2D(32, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
	model.add(Activation('elu'))
	model.add(BatchNormalization())
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.2))
 
	model.add(Conv2D(64, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
	model.add(Activation('elu'))
	model.add(BatchNormalization())
	model.add(Conv2D(64, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
	model.add(Activation('elu'))
	model.add(BatchNormalization())
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.3))
 
	model.add(Conv2D(128, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
	model.add(Activation('elu'))
	model.add(BatchNormalization())
	model.add(Conv2D(128, (3,3), padding='same', kernel_regularizer=regularizers.l2(weight_decay)))
	model.add(Activation('elu'))
	model.add(BatchNormalization())
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.4))
 
	model.add(Flatten())
	model.add(Dense(config.nb_class, activation='softmax'))



	return model

def read_model():

	model = load_model(saved_model_dir)
	
	return model 

def save_model_checkpoint():

	return ModelCheckpoint(model_checkpoint_dir, monitor = "val_loss" , verbose = 2,
	 save_best_only = True, save_weights_only = False, mode = 'auto' , period = 1)

def set_early_stopping():

	return EarlyStopping(monitor= 'val_loss',patience= 15, verbose=2, mode= 'auto')


if __name__ == "__main__":

	m= get_model()
	m.summary()

