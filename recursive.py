from typing import List


class node:
	''' This is a class to define a node and its neighboring nodes.'''

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

		

		next_node = max([])

		





	def get_height(self, map_input: List[List[float]], x: int, y: int) -> float:
		''' this is a function to return the height at a node. '''

		return map_input[x][y]




def ascent(map_input: List[List[float]], starting: tuple) -> List[tuple]:
	''' This is a function to handle the ascent recursively, first collecting the information about all of the nodes and 
	then asigning a path. The recursive algorithm will take the steepest path up, unless it reaches a local maxima, at which 
	point it will backtrack to find another path. 


	Inputs and outputs are the same as all of the other ascent/traversal functions. 

	'''

	# Create the empty lists handle the data
	visited = []
	unvisited = []
	steps = []

	for row in map_input:
		for item in row:
			if item in visited:
				break
			else:
				visited.append(item)
				# current_node = 
				pass
