# using real data, optimize classifier to predict given values

# split dataset into a training set and a test set
# train model on the training set
# calculate TP, FP, TN, FN on test set
# calculate sensitivity, specificity, positive predictivity and negative predictivity


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('./data.txt')
data = data.values
