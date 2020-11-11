# generalize optimization code for X being a matrix, where its rows are features and columns are examples
# code should work independently from number of features and number of examples
# use matrix multiplication (np.matmul or @)
# plot decision boundary on a plot x2(x1)
# calculating decision boundary might look like this:
# theta0 + theta1*x1 + theta2*x2 = 0
# theta2*x2 = -theta0 - theta1*x1
# x2 = -theta0/theta2 - theta1/theta2 * x1


from matplotlib import pyplot as plt
import numpy as np

X = np.array([[ 1, 1, 1, 1, 1, 1, 1, 1, 1,  1,  1], # bias' 'variables' already appended to X
              [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 25],
              [13, 9, 8, 6, 4, 2, 1, 0, 3,  4,  2]], dtype=np.float32)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1,  1,  1], dtype=np.float32)

theta = np.zeros((X.shape[0], 1))



