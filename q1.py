import random as rand;

def ranFun(x):
    return 0.4345*x**3 - 5.607*x**2 + 16.78*x - 10.61
x = []

for i in range(0,50):
 x.append(ranFun(i*0.2) + rand.gauss(0,1));

print x


