import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50]
y = [0.0884,
     0.0976,
     0.0984,
     0.1044,
     0.1047,
     ]
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.plot(x, y)

plt.xlabel("缺失率")
plt.ylabel("rmse")

plt.show()
