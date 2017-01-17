import random as rand;
import numpy as np;
import matplotlib.pyplot as plt

def ranFun(x):
    return 0.4345*x**3 - 5.607*x**2 + 16.78*x - 10.61
x = []; y = []; t = [];
for i in range(0,50):
 x.append((i*0.2))
 y.append(ranFun(i*0.2));
 t.append(ranFun(i*0.2)+rand.gauss(0,1));

 #create x with 50 points, y with functionalized points, t with random added.
t_row = np.asmatrix(t)
t_col = t_row.transpose()


def x_to_XX(input,m):
    ls = []
    xx = np.zeros(shape=(m,len(input)))
    for i in range(len(input)):
        for j in range(m):
            xx[j,i] = input[i]**j
    return np.asmatrix(xx)
xx = x_to_XX(x,4)
print xx.shape
row = xx
col = xx.transpose()
xTxx = np.matmul(row,col)
print xTxx.shape
xTxx_inverse = np.linalg.inv(xTxx)
xTxx_inverse_xT = np.matmul(xTxx_inverse, row)
print xTxx_inverse_xT.shape
w_1 = np.matmul(xTxx_inverse_xT,t_col)


xx = x_to_XX(x,4).transpose()
xxP = np.linalg.pinv(xx)
w_2 = np.matmul(xxP,t_col)
print w_2






