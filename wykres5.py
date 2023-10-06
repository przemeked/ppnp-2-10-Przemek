import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 8, 27, 64, 125]

plt.plot(x, y1, color="red", label='y = x ^ 2')
plt.plot(x, y2, color="orange", label='y = x ^ 3')

plt.xlabel('X')
plt.xlabel('Y')
plt.title("dwa wykres na ttym samym")
plt.legend()

plt.show()