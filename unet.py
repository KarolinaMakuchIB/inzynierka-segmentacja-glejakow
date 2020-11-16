# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 19:29:01 2020

@author: kpmak
"""
#importing libraries
from tensorflow.python.keras.layers import Dense, Flatten, Dropout, Conv2D, MaxPooling2D, Input, Concatenate, Conv2DTranspose, UpSampling2D
from tensorflow.python.keras import Sequential
from keras.models import Model
import numpy as np
import slices

#getting one image to get data size
image = slices[0]
img_rows, img_cols = np.shape(image)
inputs = Input((img_rows, img_cols, 1))
    
#function containing two 2D convolutions
def double_conv(x, filters):
    conv = Conv2D(filters, (3, 3), activation='relu', padding='same')(x)
    conv = Conv2D(filters, (3, 3), activation='relu', padding='same')(conv)
    return conv

#Unet architecture
def Unet():
    inputs = Input((img_rows, img_cols, 1))
    unet_filters = [64, 128, 256, 512, 1024]
    
    
    conv1 = double_conv(inputs, unet_filters[0])
    pool1 = MaxPooling2D(pool_size=(2, 2), strides = 2)(conv1)

    conv2 = double_conv(pool1, unet_filters[1])
    pool2 = MaxPooling2D(pool_size=(2, 2), strides = 2)(conv2)

    conv3 = double_conv(pool2, unet_filters[2])
    pool3 = MaxPooling2D(pool_size=(2, 2), strides = 2)(conv3)

    conv4 = double_conv(pool3, unet_filters[3])
    pool4 = MaxPooling2D(pool_size=(2, 2), strides = 2)(conv4)

    conv5 = double_conv(pool4, unet_filters[4])
    
    up_samp = UpSampling2D((2,2))(conv5)
    concat = Concatenate()([conv4,up_samp])
    conv6 = double_conv(concat, unet_filters[4])

    up_samp2 = UpSampling2D((2,2))(conv6)
    concat2 = Concatenate()([conv3, up_samp2])
    conv7 = double_conv(concat2, unet_filters[3])

    up_samp3 = UpSampling2D((2,2))(conv7)
    concat3 = Concatenate()([conv2, up_samp3])
    conv8 = double_conv(concat3, unet_filters[2])

    up_samp4 = UpSampling2D((2,2))(conv8)
    concat4 = Concatenate()([conv1, up_samp4])
    conv9 = double_conv(concat4, unet_filters[1])

    conv10 = Conv2D(1, (1, 1), activation='sigmoid')(conv9)

    model = Model(inputs=[inputs], outputs=[conv10])
    return model

#creating network and displaying it in console
model = Unet()
model.summary()