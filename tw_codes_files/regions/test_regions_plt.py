from matplotlib import pyplot as plt

x = [i for i in range(24)]
y = x

plt.plot(x, y, color='green', marker='o', linestyle='solid')
#
# plt.plot(x, [5, 4, 3, 2, 1, 0], color='green', marker='o', linestyle='solid')


plt.xlabel('Часы')
plt.ylabel('Создано аккаунтов тыс.')

plt.show()