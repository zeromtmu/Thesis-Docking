class params(object):
	"""docstring for params"""
	def __init__(self, searchSpace,
					centerSpace,
					generations,
					pocketSize,
					treeNodes,
					mutProbability,
					isLocalSearch,
					typeLS,
					typeCO,
					nodeByTree,
					tempLS,
					minTemp,
					alphaTemp,
					numberIteration,
					reset,
					typereset,
					typemut,
					iskb,
					kbprob,
					distanceCritLVL):
		self.searchSpace = searchSpace
		self.centerSpace = centerSpace
		self.generations = generations
		self.pocketSize = pocketSize
		self.treeNodes = treeNodes
		self.mutProbability = mutProbability
		self.isLocalSearch = isLocalSearch
		self.typeLS = typeLS
		self.typeCO = typeCO
		self.nodeByTree = nodeByTree
		self.tempLS = tempLS
		self.minTemp = minTemp
		self.alphaTemp = alphaTemp
		self.numberIteration = numberIteration
		self.reset = reset
		self.typereset = typereset
		self.typemut = typemut
		self.iskb = iskb
		self.kbProb = kbprob
		self.distCriLVL = distanceCritLVL
		