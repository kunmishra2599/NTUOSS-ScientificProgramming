import numpy as np
import timeit

x = [2,5,10,394,420,50000,12309203920,5e+15]
y = np.array([2,5,10,394,420,50000,12309203920,5e+15])

def hellaMath(items):
    return (np.tan(items*np.sin(items)*np.cos(items)))**25

# print('x: '+ str(x))
# print('y: '+str(y))

a1 = np.array([10,20,30])

a2 = np.array([[10,20,30],[40,50,60],[70,80,90],[100,110,120]])

# print(a1[1])
# print(a2[[0,1,2,3],[0,1,0,1]])
# print(a2[0,1])
# print(a2[2,2])
# print(a2[0,0],a2[1,1],a2[2,2])

print(a2*a2)
