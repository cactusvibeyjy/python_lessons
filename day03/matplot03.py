import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame([
    [500,450,520,610],
    [690,700,820,900],
    [1100,1030,1200,1380],
    [1500,1650,1700,1850],
    [1990,2020,2300,2420],
    [1020,1600,2200,2550]
])
y1 =[500,450,520,610]
y2 =[690,700,820,900]
y3=[1100,1030,1200,1380]
y4=[1500,1650,1700,1850]
y5=[1990,2020,2300,2420]
y6=[1020,1600,2200,2550]
x=range(len(y1))
color = ['b', 'orange', 'green', 'red', 'purple', 'brown']
xLabel = ['first', 'second', 'third', 'fourth']
plt.plot(x, y1, color ='b')
plt.plot(x, y2, color ='orange')
plt.plot(x, y3, color ='green')
plt.plot(x, y4, color ='red')
plt.plot(x, y5, color ='purple')
plt.plot(x, y6, color ='brown')

plt.title('2015 ~2020 Quarterly sales')
plt.xlabel('Quaters')
plt.ylabel('sales')
plt.legend(['2015','2016','2017','2018','2019','2020'], loc='upper left')
plt.xticks(x, xLabel)
plt.show()