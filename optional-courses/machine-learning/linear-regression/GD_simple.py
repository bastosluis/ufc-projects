# Gradient Descendent Simple (Linear Regression):
import numpy as np

pace = 0.01
t = 0       #iteração
x = np.c_[np.ones((peixe_dataset.shape[0],1)), peixe_dataset[:,[0,-2]]] 
y = peixe_dataset[:,[-1]]
w0, w1 = 0
while t < 100:
  t += 1
  y_p = w0 + (w1*x) 
  errors = y - y_p
  w0 = w0 + pace * np.mean(errors)
  w1 = w1 + pace * np.mean(errors * x)
print(w)