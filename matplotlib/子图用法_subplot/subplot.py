import matplotlib.pyplot as plt
import numpy as np

#一个图
a=np.random.rand(5)
b=np.random.rand(5)
fig,ax=plt.subplots()  #定义了一个元组，fig返回图像对象，ax返回子图图像的对象
ax.set_aspect('equal') #设置纵横比，长宽相等
ax.scatter(a,b)  #绘制散点图
plt.show()  #显示图像


#多个图(事先添加)subplots
a=np.random.rand(5)
b=np.random.rand(5)
c=np.random.rand(5)
d=np.random.rand(5)
fig,ax=plt.subplots(2,2)  #定义了一个元组，fig返回图像对象，ax返回子图图像的对象 [2,2]表示绘制4个子图，ax[0][1]表示对第一行，第二列子图进行操作
ax[0][0].scatter(a,b)  #绘制散点图
ax[0][1].scatter(a,c)  #绘制散点图
ax[1][0].scatter(a,d)  #绘制散点图
ax[1][1].scatter(b,d)  #绘制散点图
plt.show()  #显示图像


#多个图(逐个添加)subplot
a=np.random.rand(5)
b=np.random.rand(5)
c=np.random.rand(5)
d=np.random.rand(5)
plt.subplot(2,2,1)  #对四个子图的第一个图进行操作
plt.plot(a,b,'b--') #绘制第一个子图,蓝色虚线表示
plt.show()  #显示图像




