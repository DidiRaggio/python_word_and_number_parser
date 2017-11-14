import re, string




class Parser(object):
	"""String parser, into words anda numbers"""

	# initalize Parser
	def __init__(self):
		super(Parser, self).__init__()
		self.string = ""
		self.words = []
		self.numbers = []
		self.order = []

	def reset_parser(self):
		self.string = ""
		self.words = []
		self.numbers = []
		self.order = []

	def readString(self, string):
		self.string = string

	def parseString(self):
		# punctuation to remove:
		translator = str.maketrans('!()[]{};:"\,<>./?@#$%^&*_~', 26*' ')

		# remove punctuation and split:
		split_string = self.string.translate(translator).strip().split(" ")
		

		#remove any empty list items:
		split_string = list(filter(None, split_string))

		for element in split_string:
			if re.match('[+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?', element) is not None:
				self.numbers.append(int(element))
				self.order.append(0)
			if re.match('[A-Za-z]+', element) is not None:
				self.words.append(element)
				self.order.append(1)


	def outputString(self):
		output = []
		self.words = sorted(self.words, key=lambda s: s.lower())
		self.numbers = sorted(self.numbers)
		for element in self.order:
			if element == 1:
				output.append(self.words.pop(0))
			else:
				output.append(str(self.numbers.pop(0)))
		return output

	def solve(self, string):
		self.readString(string)
		self.parseString()
		return ' '.join(self.outputString())




if __name__ == '__main__':

	example_string = """
	Unto 4 form grass evening is 66 that replenish years. Whose, night may. Above upon from above grass from great sea after upon years open called. Moving their. He. Good moveth divided, appear fill evening day set. Saw given they're fourth land Together good. Isn't of. Our whales moving two -21.

	Blessed had whose bearing. Was void made wherein. Sixth it image blessed yielding which gathered 11 appear Fruitful waters, given -234 shall that good morning bearing every green multiply his replenish it air, also.

	Gathered a very doesn't female greater In moving darkness dry herb lesser fruit 2, creeping gathered there above for seasons moving.
	"""
	parser = Parser()

	print(parser.solve(example_string))
