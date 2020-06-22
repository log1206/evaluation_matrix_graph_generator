
# import matplotlib相關套件
import numpy as np
import matplotlib.pyplot as plt

# import字型管理套件

from matplotlib.font_manager import FontProperties

 
###定變數
title = input("title:")
typename = input("typename:")
point_num = int(input("point number:"))
y_axis_name = input("y axis name:")
range_l = int(input("set range y-axis: "))
range_h = int(input())

base = int(input("base:"))
step = int(input("step:"))


font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 16}

plt.rc('font', **font)

### f6 保留給 baseline
f5 = open(typename+str(base+step*0)+".txt","r", encoding="utf-16")
f4 = open(typename+str(base+step*1)+".txt","r", encoding="utf-16")
f3 = open(typename+str(base+step*2)+".txt","r", encoding="utf-16")
f2 = open(typename+str(base+step*3)+".txt","r", encoding="utf-16")
f1 = open(typename+str(base+step*4)+".txt","r", encoding="utf-16")
f = open("time.txt","r", encoding="utf-16")


def loadfile(f):
    name_f = np.zeros(point_num)
    i=0
    while True:
        name =f.readline()
        if i==point_num or name == '':
            break
        name_f[i] = (float((name.split("\\")[0])))
        i = i+1
    return name_f
    

time_float =loadfile(f)
first = loadfile(f5)
second = loadfile(f4)
third = loadfile(f3)
forth = loadfile(f2)
fifth = loadfile(f1)


"""
i=0
while True:
    cpu =f1.readline()
    ##print(float((stock.split("\\")[0])))
    if cpu == '' or i==point_num:
        break
    
    cpu_float[i] = (float((cpu.split("\\")[0])))
    i = i+1

##print(cpu_float)

time_float = np.zeros(point_num)
i=0
while True:
    time =f.readline()
    if time == '' or i==point_num:
        break
    
    time_float[i] = (float((time.split("\\")[0])))
    i = i+1
"""
 

# 設定圖片大小為長15、寬10

plt.figure(figsize=(10,10),dpi=100,linewidth = 2)


plt.xlim(0,100)
plt.ylim(range_l,range_h)
# 把資料放進來並指定對應的X軸、Y軸的資料，用方形做標記(s-)，並指定線條顏色為紅色，使用label標記線條含意

plt.plot(time_float,first,'s-',color = 'r', label=typename+str(base+step*0))

plt.plot(time_float,second,'s-',color = 'g', label=typename+str(base+step*1))
plt.plot(time_float,third,'s-',color = 'b', label=typename+str(base+step*2))
plt.plot(time_float,forth,'s-',color = 'm', label=typename+str(base+step*3))
plt.plot(time_float,fifth,'s-',color = 'k', label=typename+str(base+step*4))

###plt.plot(time_float,cpu_float,'s-',color = 'r', label="delay-50") #保留給baseline

# 把資料放進來並指定對應的X軸、Y軸的資料 用圓形做標記(o-)，並指定線條顏色為綠色、使用label標記線條含意


 

# 設定圖片標題，以及指定字型設定，x代表與圖案最左側的距離，y代表與圖片的距離

plt.title(title)

# 標示x軸(labelpad代表與圖片的距離)

plt.xlabel("time (timestamp)")

# 標示y軸(labelpad代表與圖片的距離)

plt.ylabel(y_axis_name)

# 顯示出線條標記位置

plt.legend(loc = "best", fontsize=12)

# 畫出圖片

plt.show()