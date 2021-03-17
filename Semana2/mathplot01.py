import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os



x = [0,1,2,3,4]
y = [0,2,4,6,8]

# Resize your graph

plt.figure(figsize=(5,3), dpi=100)

# plt.plot(x,y,label='2x', c = 'red', linewidth=2, marker = '.', linestyle='--', markersize = 10,markeredgecolor='blue')
#fmt = '[color][marker][line]'
plt.plot(x,y,'r^--',label='2x')

## Line number two
x2 = np.arange(0,4.5,0.5)
plt.plot(x2[:5],x2[:5]**2,'g+-',label='x2')
plt.plot(x2[4:],x2[4:]**2,'g+--',label='x2')

plt.title('Our First Graph', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])

plt.legend()

os.chdir('mathplot01arquivo')
plt.savefig('mygraph.png', dpi=300)
plt.show()