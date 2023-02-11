import matplotlib.pyplot as plt

# sample data
x = ["Home", "hi", "hhj", "hhh", 'kkk']
y = [2, 4, 6, 8, 10]

# plot the data as scatter points
plt.scatter(x, y)

# add a title and labels for the axes
plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# show the plot
plt.show()