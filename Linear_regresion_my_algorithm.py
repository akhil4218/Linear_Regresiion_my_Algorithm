import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import mean
x_d=np.linspace(1,10,100000)
y_d=np.random.randn(len(x_d))
y_dd=(0.5*x_d)+6+y_d
a_d=pd.DataFrame(x_d,columns=["X"])
b_d=pd.DataFrame(y_dd,columns=["Y"])
#df=pd.read_csv("C:\\Users\\NIKHIL\\Desktop\\Temporary\\hi.csv",index_col=0)
#x=df["Sp. Def"].values
#y=df["Speed"].values

print(x,y)
length=int(max(x))+100
#####--->>>>>>>>>>>>>>>>>>Converting to mean
mean_x=mean(x)
mean_y=mean(y)

#print("means",mean_x,mean_y)

var_x=[]
for i in x:
    temp=i-mean_x
    var_x.append(temp)

var_y=[]
for j in y:
    flag=j-mean_y
    var_y.append(flag)

slope_num=[]
for a,b in zip(var_x,var_y):
    t=a*b
    slope_num.append(t)
    
#print(sum(slope_num))
slope_den=[]
for e in x:
    temp2=e-mean_x
    slope_den.append(temp2**2)
#print(slope_den)

slope=sum(slope_num) / sum(slope_den)
#print("slope",slope)

intercept= mean_y - (slope*mean_x)

print("intercpt form -> y = ",slope,"x +",intercept)

dum_x=[ff for ff in range(-length,length)]
dum_y=[]

for w in dum_x:
    d_y=slope*w+intercept
    dum_y.append(d_y)

#print("final values",dum_x,dum_y)

#plt.subplot(212)
plt.plot(x,y,"o")
plt.plot(dum_x,dum_y)
plt.show()
