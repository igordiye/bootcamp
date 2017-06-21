"""
This is a module of useful functions generated during bootcamp June 2017
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def compute_ecdf(data):
    """A function to compute ECDF
    Lesson 23-34"""
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)

    return x, y
