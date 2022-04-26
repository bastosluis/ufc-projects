import numpy as np

def normalize_row(row, mean, std):
    return (row-mean)/std

def denormalize_row(row, mean, std):
    return mean+(row*x)

def normalize()