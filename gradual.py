# This file extends main.py to implement a gradual ascent algorithm, where the pathfinder moves always to the most gradual 
# adjaent node until it reaches a maxima. 


from typing import List

class node:
	''' This is a class to define a node and its neighboring nodes. '''

	def __init__(self, map_input: List[List[float]], x: int, y: int):

		# This class assumes that North is "up" in the array, that is a row is north of another if its index is less. Likewise for E/W.
		# X is the E/W index, Y is the N/S index 

		# Handle inputs to class		
		map_height = len(map_input[0])
		map_width = len(map_input)
		self.x = x
		self.y = y

		# Get height of current node
		self.height = self.get_height(map_input, x, y)

		# Get the indices of adjacent nodes, if available
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

		# Get the height of adjacent nodes, if available
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

	




	def get_height(self, map_input: List[List[float]], x: int, y: int) -> float:
		''' this is a function to return the height at a node. '''

		return map_input[x][y]





def ascent(map_input: List[List[float]], starting: tuple) -> List[tuple]:
	''' This is a function to invoke a gradual traverse, similar to steep traverse. The principle difference being that 
	instead of picking the steepest step, the algorithm will pick the step with the most gradual positive slope.

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


		pos_gradient = [] 
		for index, item in enumerate(gradient):
			if item['grade'] <= 0:
				pos_gradient.append(item)


		gradual = min(pos_gradient, key=lambda x:x['grade'])

		if gradual['grade'] < 0 and map_input[current_node.x][current_node.y] != max_height:
			current_node = previous_node
		# If there is nowhere to go, you have reached a local maximum
		elif current_node == previous_node or len(steps) == 1000:
			break
		else: 
			steps.append(current_node)
			previous_node = current_node
			current_node = node(map_input, gradual['node_x'], gradual['node_y'])

	return steps



