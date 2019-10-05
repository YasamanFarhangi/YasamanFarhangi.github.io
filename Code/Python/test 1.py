from Equation import Expression
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(float(input('start point: ')), float(input('endpoint: ')), int(input('accuracy: ')))
# y = 2 * x

fn1 = Expression(input('function: '))
fn2 = Expression(input('function: '))


plt.plot(x, fn1(x))
plt.plot(x, fn2(x))
plt.show()
