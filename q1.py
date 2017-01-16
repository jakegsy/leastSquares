import random as rand;
import numpy as np;

def ranFun(x):
    return 0.4345*x**3 - 5.607*x**2 + 16.78*x - 10.61
x = []; y = []; t = [];
for i in range(0,50):
 x.append((i*0.2));
 y.append(ranFun(i*0.2));
 t.append(ranFun(i*0.2)+rand.gauss(0,1));
 #create x with 50 points, y with functionalized points, t with random added.
t_n = np.array(t)
print t_n;print t_n.shape
t_n.transpose;
print t_n








