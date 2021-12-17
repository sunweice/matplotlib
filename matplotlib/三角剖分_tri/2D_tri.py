import matplotlib.pyplot as plt
import matplotlib.tri as tri
import numpy as np

a=np.random.rand(5)
b=np.random.rand(5)
triang=tri.Triangulation(a,b)  #输入散点，完成剖分
plt.triplot(triang) #绘制对象
plt.show()
