from matplotlib import pyplot as plt

plt.plot([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], color='green', marker='o', linestyle='solid')

plt.plot([0, 1, 2, 3, 4, 5], [5, 4, 3, 2, 1, 0], color='green', marker='o', linestyle='solid')


plt.xlabel('Часы')
plt.ylabel('Создано аккаунтов тыс.')

plt.show()