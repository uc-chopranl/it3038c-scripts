# Neil Chopra
# Lab 7 - Scripting Language

import matplotlib.pyplot as plt
import numpy as np

# Creating a bar graph
x_axis = np.array(["A", "B", "C", "D", "E"])

y_axis = np.array([10, 15, 37, 17, 25])

# Display bar graph
plt.bar(x_axis, y_axis)
plt.show()

# Draw a Line
point_x = np.array([0, 2])
point_y = np.array([3, 8])

# Plot a Line on a Graph
plt.plot(point_x, point_y, marker = 'o')
plt.show()

# Create a Pie Chart and adding a Legend
pie_y = np.array([25, 50, 10, 5, 2, 3, 5])
pie_labels = ["The Flash", "Doctor Strange", "Blue Beetle", "Silver Surfer", "The Thing", "Moon Knight", "Swamp Things"]

#Display Pie Chart and Legend
plt.pie(pie_y, labels = pie_labels)

#Position Legend next to Pie Graph and Include Legend Title
plt.legend(bbox_to_anchor = (1.2, 0.9), loc = 'upper left', title = "List of Comic Book Characters: ")
plt.show()

