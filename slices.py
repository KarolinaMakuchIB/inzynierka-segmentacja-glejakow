# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 15:37:53 2020

@author: kpmak
"""
#importing libraries and functions
import data_loader
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

#loading case to display
case1 = load_case('001')

#function displaying slices
def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")

data = {}
slices = {}
for i in range(0, len(case1)):
    data[i] = case1[i]
    data[i].get_fdata()
    data[i] = data[i].get_fdata()
    slices[i] = data[i][:,:,80]

show_slices([slices[0], slices[1], slices[2], slices[3], slices[4]])
