import numpy as np
import matplotlib.pyplot as plt
import math

def DoNormalPDF(location):
    o = 2
    u = 70
    x = location
    return ((1/math.sqrt(2 * pi * o^2)) * math.exp((-1)/(2 * o^2)) * (x - u)^2)

def DoNormalPDFLoop(location_array):
    result_array = []
    for i in location_array:
        result_array.append(DoNormalPDF(i))
    return result_array

def BuildArray():
    lower_bound = 68
    upper_bound = 76
    step = 2
    return np.arange(lower_bound, upper_bound, 2)

def main():
    location_array = BuildArray()
    result_array = DoNormalPDFLoop(location_array)
    plt.bar(result_array, len(result_array))
