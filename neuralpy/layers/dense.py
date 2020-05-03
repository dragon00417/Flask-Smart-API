import numpy as np

class Dense:
	def __init__(self, n_inputs, n_nodes):
		self.__n_inputs = n_inputs
		self.__n_nodes = n_nodes

		self.__weights = np.random.randn(n_inputs, n_nodes)
		self.__bias = np.zeros((1, n_nodes), dtype=np.float)

	def forward(self, x):
		self.output = np.dot(x, self.__weights) + self.__bias

	def get_weights(self):
		return {'weights': self.__weights, 'bias': self.__bias}

	def get_details(self):
		return {
			'name': "Dense",
			'n_inputs': self.__n_inputs,
			'n_nodes': self.__n_nodes,
			'n_params': self.__n_inputs * self.__n_nodes + self.__n_nodes
		}