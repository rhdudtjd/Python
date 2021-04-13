import matplotlib.pyplot as plt

graph = [-3, -2, -1, 0, 1, 2, 3]
x = []
y = []

for i in range(7):
    value = int(input("x 입력("+ str(i + 1) + ") : "))
    x.append(value)
    
print("------------------")

for i in range(7):
    value = int(input("y 입력("+ str(i + 1) + ") : "))
    y.append(value)

plt.plot(x, y)
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.xticks(graph)
plt.yticks(graph)
plt.show()