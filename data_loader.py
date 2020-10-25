# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:13:46 2020

@author: kpmak
"""
from pathlib import Path

import nibabel as nib
import os 

def get_full_case_id(cid):
    try:
        case_id = "BraTS20_Training_"+cid
        
    except ValueError:
        case_id = cid

    return case_id


def get_case_path(cid):

    data_path = 'MICCAI_BraTS2020_TrainingData/MICCAI_BraTS2020_TrainingData/'
    case_id = get_full_case_id(cid)
    case_path = data_path + case_id

    return case_path


def load_flair(cid):
    
    data_path = get_case_path(cid)
    file_name = "/BraTS20_Training_"+cid
    flair = nib.load(str(data_path + file_name + "_flair.nii.gz"))
    
    return flair


def load_seg(cid):
    
    data_path = get_case_path(cid)
    file_name = "/BraTS20_Training_"+cid
    seg = nib.load(str(data_path + file_name + "_seg.nii.gz"))
    
    return seg


def load_t1(cid):
    
    data_path = get_case_path(cid)
    file_name = "/BraTS20_Training_"+cid
    t1 = nib.load(str(data_path + file_name + "_t1.nii.gz"))
    
    return t1


def load_t1ce(cid):
    
    data_path = get_case_path(cid)
    file_name = "/BraTS20_Training_"+cid
    t1ce = nib.load(str(data_path + file_name + "_t1ce.nii.gz"))
    
    return t1ce


def load_t2(cid):
    
    data_path = get_case_path(cid)
    file_name = "/BraTS20_Training_"+cid
    t2 = nib.load(str(data_path + file_name + "_t2.nii.gz"))
    
    return t2


def load_case(cid):
    
    flair = load_flair(cid)
    seg = load_seg(cid)
    t1 = load_t1(cid)
    t1ce = load_t1ce(cid)
    t2 = load_t2(cid)
    
    return flair, seg, t1, t1ce, t2