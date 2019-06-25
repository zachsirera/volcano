# Import necessary libraries
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Import typing requirements
from typing import List

# Import algorithms from adjacent files
import gradual
import steepest
import recursive
import optimum


def map() -> List[List[float]]:
	''' This is a function to read volcano.csv (from r) and map the data to an array to be processed by the algorithms. '''

	volcano_map = []

	with open('volcano.csv', newline='') as csvfile:
		volcano_reader = csv.reader(csvfile, delimiter=',')

		# Skip the first row, as it is just a header
		next(volcano_reader)

		for row in volcano_reader:
			new_row = []

			# Skip the first column as it is just a column index
			for item in row[1:]:
				num = int(item)
				new_row.append(num)
			volcano_map.append(new_row)

	return volcano_map




def plot(map_input: List[List[float]], step_array1, step_array2):
	''' This is a function to generate a surface plot of the path output from the pathfinder '''

	# Plot the volcano image
	array = np.array(map_input)
	plt.imshow(array)

	# Compile the path data.
	x1 = []
	y1 =[]

	x2 = []
	y2 = []

	for item in step_array1:
		x1.append(item.x)
		y1.append(item.y)

	for item in step_array2:
		x2.append(item.x)
		y2.append(item.y)

	# Superimpose the path over the volcano image and display
	plt.scatter(x1, y1, c='r', s=10)
	plt.scatter(x2, y2, c='y', s=10)
	plt.show()




def go(x: int, y: int):
	''' This is a function to begin the pathfinder. '''
	
	# Generate the map from the volcano dataset. 
	volcano_map = map()

	# Carry out the various ascents 
	starting = (x, y)
	steep = steepest.ascent(volcano_map, starting)
	grad = gradual.ascent(volcano_map, starting)
	# recur = recursive.ascent(volcano_map, starting)


	# Plot the map
	plot(volcano_map, steep, grad)



if __name__ == "__main__":
	go(0, 0)




	









