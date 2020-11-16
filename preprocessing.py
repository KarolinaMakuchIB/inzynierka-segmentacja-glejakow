# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:10:58 2020

@author: kpmak
"""
import data_loader
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def gaussian_smoothing(image, sigma):
    size = np.ceil(sigma*2.54)//2*2+1
    shape = (size,size)
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
        
    result = signal.convolve2d(image,h)
    return result

def normalize(image):
    return (image - np.min(image))/(np.max(image) - np.min(image))
