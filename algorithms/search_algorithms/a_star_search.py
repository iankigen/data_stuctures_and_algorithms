"""
A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs:
starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest
cost (least distance travelled, shortest time, etc.).


"""
tree = {
	'S': [['A', 1], ['B', 5], ['C', 8]],
	'A': [['S', 1], ['D', 3], ['E', 7], ['G', 9]],
	'B': [['S', 5], ['G', 4]],
	'C': [['S', 8], ['G', 5]],
	'D': [['A', 3]],
	'E': [['A', 7]]
}

heuristic = {'S': 8, 'A': 8, 'B': 4, 'C': 3, 'D': 5000, 'E': 5000, 'G': 0}

cost = {
	'S': 0
}  # cost for visiting each node


def a_star_search():
	global tree, heuristic

	visited_nodes = []  # visited nodes
	opened = [['S', 8]]  # opened nodes

	# find the visited nodes
	while True:
		fn = [i[1] for i in opened]  # fn = f(n) = g(n) + h(n)
		chosen_index = fn.index(min(fn))

		node = opened[chosen_index][0]
		visited_nodes.append(opened[chosen_index])

		del opened[chosen_index]

		if visited_nodes[-1][0] == 'G':
			break  # break the goal has been found
		for item in tree[node]:
			if item[0] in [visited_node[0] for visited_node in visited_nodes]:
				continue
			cost.update({item[0]: cost[node] + item[1]})  # add nodes to cost dictionary
			fn_node = cost[node] + heuristic[item[0]] + item[1]  # calculate f(n) of current node
			temp = [item[0], fn_node]
			opened.append(temp)  # store f(n) of current node in array opened
			print('opened', opened)

	#  find optimal sequence for the goal node
	trace_node = 'G'
	optimal_sequence = ['G']
	for i in range(len(visited_nodes) - 2, -1, -1):  # start from the second last after G, range(start, stop, step)
		check_node = visited_nodes[i][0]
		if trace_node in [children[0] for children in tree[check_node]]:
			children_cost = [temp[1] for temp in tree[check_node]]
			children_nodes = [temp[0] for temp in tree[check_node]]

			# check whether h(s) + g(s) = f(s). If so, append current node to optimal sequence and change the
			# correct optimal tracing node to current node
			if cost[check_node] + children_cost[children_nodes.index(trace_node)] == cost[trace_node]:
				optimal_sequence.append(check_node)
				trace_node = check_node
	optimal_sequence.reverse()  # reverse the optimal sequence

	return visited_nodes, optimal_sequence


if __name__ == '__main__':
	visited_nodes, optimal_sequence = a_star_search()
	print('visited nodes: ' + str(visited_nodes))
	print('optimal nodes sequence: ' + str(optimal_sequence))
