Lab 7 Script - Neil Chopra
======

Here is how you can run a python script that I created, which uses matplotlib and numpy concurrently to graph data. 

Installing Python Packages
======

First, install **matplotlib** and **numpy** via command line:

```pip install matplotlib```
```pip install numpy```

In order to use these Python packages, we have to import the modules at the beginning of our script

```
import matplotlib.pyplot as plt
import numpy as np
```

***It's very important both numpy AND matplotlib.pyplot are imported, otherwise the script will not function properly***

Creating a bar graph and displaying our graph
=====

To create a bar graph, you must assign variables to both the X-axis and the Y-axis, this can be done in an array:

```
x_axis = np.array(["A", "B", "C", "D", "E"])
y_axis = np.array([10, 15, 37, 17, 25])
```

Once we have established our x and y-axis variables, we are able to display the bar graph like so:

```
plt.bar(x_axis, y_axis)
plt.show()
```
Now that we know how to create a bar graph, and how to display our graphs - let's dive into **how to plot a singular line on the graph**:

Plotting and Graphing a Line
============================
Whenever plotting a line on a graph, we need to create and establish the x and y-axis location for our plots:

```
point_x = np.array([0, 2])
point_y = np.array([3, 8])
```

Actually graphing the line itself is very similar, although instead of the **bar** suffix when we're calling the graph, we will use the **plot** suffix:

```
plt.plot(point_x, point_y, marker = 'o')
plt.show()
```

Notice how I have **marker = 'o'** within my plot statement? This is used to create a marker in which your data plot actually resides, this helps make your graph look more clean and organized.

Now that I have shown you how to create and plot a line on a graph, we will dive into ***creating a pie graph and adding a legend to the graph***:

Creating a Pie Graph and Adding a Legend
========================================

When creating a pie chart, we only have one axis value. An array is created to display the difference between each value and the frequency of the value:

```
pie_y = np.array([25, 50, 10, 5, 2, 3, 5])
```
Now, we want to add labels. Create another variable that is a list, that corresponds to each value letting us know what item is what, and how common is it. In this example, I will use Comic Book characters:

```
pie_labels = ["The Flash", "Doctor Strange", "Blue Beetle", "Silver Surfer", "The Thing", "Moon Knight", "Swamp Things"]
```

In order to display the legend, we will include it after our variable is called:

```
plt.pie(pie_y, labels = pie_labels)
```

Finally, you can customize the position and add a title within your legend using the **title** and **loc** command within your ***plt.pie*** statement. If the legend is formatted, covering the pie graph - You can change the position using the **bbox_to_anchor** command:

```
plt.legend(bbox_to_anchor = (1.2, 0.9), loc = 'upper left', title = "List of Comic Book Characters: ")
```

To show your pie graph:

```
plt.show()
```


