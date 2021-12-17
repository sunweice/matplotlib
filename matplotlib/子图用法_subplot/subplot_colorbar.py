import matplotlib.pyplot as plt
import numpy as np



#添加colorbar
#一个图
a=np.random.rand(5)
b=np.random.rand(5)
c=np.random.rand(5)
fig=plt.figure()  #创建一个画布对象
plt.scatter(a,b,c=c,cmap='jet')  #绘制散点图
plt.colorbar()
plt.show()  #显示图像




#多个子图添加colorbar
a=np.random.rand(5)
b=np.random.rand(5)
c=np.random.rand(5)
d=np.random.rand(5)
fig,ax=plt.subplots(2,2)  #定义了一个元组，fig返回图像对象，ax返回子图图像的对象 [2,2]表示绘制4个子图，ax[0][1]表示对第一行，第二列子图进行操作
a00=ax[0][0].scatter(a,b,c=c,cmap='jet')  #绘制散点图
fig.colorbar(a00,ax=ax[0][0])  #第一个参数为mappable，可以映射的颜色对象，第二个参数ax为colorbar出现的子图位置
a01=ax[0][1].scatter(a,c,c=c,cmap='jet')  #绘制散点图
fig.colorbar(a01,ax=ax[0][1])  #第一个参数为mappable，可以映射的颜色对象，第二个参数ax为colorbar出现的子图位置
a10=ax[1][0].scatter(a,d,c=c,cmap='jet')  #绘制散点图
fig.colorbar(a10,ax=ax[1][0])  #第一个参数为mappable，可以映射的颜色对象，第二个参数ax为colorbar出现的子图位置
a11=ax[1][1].scatter(b,d,c=c,cmap='jet')  #绘制散点图
fig.colorbar(a11,ax=ax[1][1])  #第一个参数为mappable，可以映射的颜色对象，第二个参数ax为colorbar出现的子图位置
plt.show()  #显示图像