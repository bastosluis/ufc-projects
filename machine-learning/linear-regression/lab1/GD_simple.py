# Gradient Descendent Simple (Linear Regression):
# 
import numpy as np
import matplotlib.pyplot as plt  # Biblioteca para gerar gráficos

peixe_dataset = np.genfromtxt('./peixe.txt', delimiter=',')

pace = 0.000001
t = 0       #iteração
x = peixe_dataset[:,[0]]
y = peixe_dataset[:,[-1]]
w = np.zeros((3,1))
w0 = 0
w1 = 0
errorlist = []
it = []
while t < 1000:
  t += 1
  y_p = w0 + (w1*x) 
  errors = y - y_p
  errorlist.append(np.mean(errors**2))
  it.append(t)
  w0 = w0 + pace * np.mean(errors)
  w1 = w1 + pace * np.mean(errors * x)

space = np.linspace(np.min(x), np.max(x))
funct = w0 + w1*space

plt.plot(it,errorlist)
plt.show()

plt.plot(x,y, 'bo')
plt.plot(space, funct, '-r', label='y=w0+w1*x')
plt.show()
