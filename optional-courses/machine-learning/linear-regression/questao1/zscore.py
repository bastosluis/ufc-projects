import numpy as np

def normalize(x, mean, std):
    return (x-mean)/std

def denormalize(x, mean, std):
    return mean+(std*x)