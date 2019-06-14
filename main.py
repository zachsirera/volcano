import csv
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from typing import List

class node:
	''' This is a class to define a node and its neighboring nodes. '''

	def __init__(self, map_input: List[List[float]], x: int, y: int):

		# This class assumes that North is "up" in the array, that is a row is north of another if its index is less. Likewise for E/W.
		# X is the E/W index, Y is the N/S index 

		
		map_height = len(map_input[0])
		map_width = len(map_input)

		self.x = x
		self.y = y

		self.height = self.get_height(map_input, x, y)

		if y - 1 < 0 or y - 1 > map_height:
			self.n = None
		else:
			self.n = (x, y - 1)

		if y + 1 < 0 or y + 1 > map_height:
			self.s = None
		else:
			self.s = (x, y + 1)

		if x - 1 < 0 or x - 1 > map_width:
			self.e = None
		else:
			self.e = (x - 1, y)

		if x + 1 < 0 or x + 1 > map_width:
			self.w = None 
		else:
			self.w = (x + 1, y)

		try:
			self.n_height = self.get_height(map_input, self.n[0], self.n[1])
		except TypeError :
			self.n_height = None

		try:
			self.s_height = self.get_height(map_input, self.s[0], self.s[1])
		except TypeError:
			self.s_height = None

		try:
			self.e_height = self.get_height(map_input, self.e[0], self.e[1])
		except TypeError:
			self.e_height = None

		try:
			self.w_height = self.get_height(map_input, self.w[0], self.w[1])
		except TypeError:
			self.w_height = None
		

		# Maybe later if more complexity is desired

		# self.nw = (x + 1, y - 1)
		# self.ne = (x - 1, y - 1)
		# self.sw = (x + 1, y + 1)
		# self.se = (x - 1, y + 1)


	def get_height(self, map_input: List[List[float]], x: int, y: int) -> float:
		''' this is a function to return the height at a node. '''

		return map_input[x][y]




	def steep_grade(self):
		''' This function calculates the gradient between a node and all adjacent nodes and returns the indices of the node
		with the steepest grade. '''





def map() -> List[List[float]]:
	''' This is a function to read volcano.csv (from r) and map the data to an array. '''

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




def test(map_input: List[List[float]]):
	''' This is a test '''

	# starting = (0, 0)

	starting_node = node(map_input, 0, 0)

	return starting_node





	




def steep_traverse(map_input: List[List[float]], starting: tuple) -> List[tuple]:
	''' This is a function to traverse the volcano from it's lowest point to its highest point.

	With this function, traversal follows the "steepest ascent" method, moving from one node to the steepest adjacent node.

	This function takes as its argument a map in the form of an array and the starting point in the form of a tuple, and 
	calculates the traversal path. 
	'''


	steps = []

	max_height = 0
	
	for row in map_input:
		height = max(row)
		if height > max_height:
			max_height = height

	current_node = node(map_input, starting[0], starting[1])
	previous_node = None

	while True:

		gradient = []


		# Take the steepest step possible
		if current_node.n_height == None:
			pass
		else:
			grade = current_node.n_height - current_node.height
			obj = {
				'grade': grade,
				'node_x': current_node.n[0],
				'node_y': current_node.n[1],
				'previous_x': current_node.x,
				'previous_y': current_node.y
			}
			gradient.append(obj)

		if current_node.s_height == None:
			pass
		else:
			grade = current_node.s_height - current_node.height
			obj = {
				'grade': grade,
				'node_x': current_node.s[0],
				'node_y': current_node.s[1],
				'previous_x': current_node.x,
				'previous_y': current_node.y
			}
			gradient.append(obj)

		if current_node.e_height == None:
			pass
		else:
			grade = current_node.e_height - current_node.height
			obj = {
				'grade': grade,
				'node_x': current_node.e[0],
				'node_y': current_node.e[1],
				'previous_x': current_node.x,
				'previous_y': current_node.y
			}
			gradient.append(obj)

		if current_node.w_height == None:
			pass
		else:
			grade = current_node.w_height - current_node.height
			obj = {
				'grade': grade,
				'node_x': current_node.w[0],
				'node_y': current_node.w[1],
				'previous_x': current_node.x,
				'previous_y': current_node.y
			}
			gradient.append(obj)

		steepest = max(gradient, key=lambda x:x['grade'])

		if steepest['grade'] < 0 and map_input[current_node.x][current_node.y] != max_height:
			current_node = previous_node

		else: 
			steps.append(current_node)

		previous_node = current_node
		
		current_node = node(map_input, steepest['node_x'], steepest['node_y'])

		# If there is nowhere to go, you have reached a local maximum
		if current_node == previous_node or len(steps) == 1000:
			break
		else:
			

	return steps



def plot(map_input: List[List[float]], step_array):
	''' This is a function to generate a surface plot of the path output from the pathfinder '''

	# Plot the volcano image
	array = np.array(map_input)
	plt.imshow(array)

	# Compile the path data.
	x = []
	y =[]

	for item in step_array:
		x.append(item.x)
		y.append(item.y)

	# Superimpose the path over the volcano image and display
	plt.scatter(x, y, c='r', s=10)
	plt.show()




def go(x: int, y: int):
	''' This is a function to begin the pathfinder. '''
	
	# Generate the map from the volcano dataset. 
	volcano_map = map()

	# Carry out the steep traverse method
	starting = (x, y)
	initial_height = volcano_map[x][y]
	steps = steep_traverse(volcano_map, starting)

	# final_height = volcano_map[steps[-1]['previous_x']][steps[-1][previous_y]]

	# Plot the map
	plot(volcano_map, steps)



if __name__ == "__main__":
	go(0, 0)




	









