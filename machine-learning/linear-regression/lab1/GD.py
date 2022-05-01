pace = 0.01
t = 0       #iteração
x = np.c_[np.ones((peixe_dataset.shape[0],1)), peixe_dataset[:,[0,-2]]] 
y = peixe_dataset[:,[-1]]
w = np.zeros((3,1))
while t < 100:
  t += 1
  y_p = x @ w
  errors = y - y_p
  w = w + pace * np.mean(errors * x)
print(w)
