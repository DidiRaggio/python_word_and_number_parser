import unittest
from word_and_number_parser import Parser


class TestParser(unittest.TestCase):



	#CREATE METHODS TO INITIALIZE TESTING EXAMPLES, BEFORE EACH TEST CASE
	def setUp(self):
		self.input_string1 = "1"
		self.input_string2 = "car truck bus"
		self.input_string3 = "8 4 6 1 -2 9 5"
		self.input_string4 = "car truck 8 4 bus 6 1"
		self.input_string5 = """
		Jessica is 15 years old and Daniel is -27 years old. Edward is 97, and his grandfather Oscar, is 102.
		Blah -0, 4 7, 9 9,9 Eleven
		"""
		self.parser = Parser()


	def test_initialize_parser(self):
		parser = self.parser
		self.assertIsInstance(parser, Parser)
		self.assertIsInstance(parser.words, list)
		self.assertIsInstance(parser.numbers, list)
		self.assertIsInstance(parser.order, list)

	def test_parser_read_string(self):
		self.assertEqual(self.parser.string, "")
		self.parser.readString(self.input_string1)
		self.assertEqual(self.parser.string, "1")
		self.parser.readString(self.input_string4)
		self.assertEqual(self.parser.string, "car truck 8 4 bus 6 1")

	def test_parser_parse_string(self):
		p = self.parser
		
		#Parser does not read punctuation
		p.readString('! ( ) [ ] { } ; : " \ , < > . / ? @ # $ % ^ & * _ ~ ')
		p.parseString()
		self.assertEqual(p.words, [])
		self.assertEqual(p.numbers, [])
		self.assertEqual(p.order, [])
		p.reset_parser()

		# Parses single item:
		p.readString(self.input_string1)
		p.parseString()
		self.assertEqual(p.words, [])
		self.assertEqual(p.numbers, [1])
		self.assertEqual(p.order, [0])
		p.reset_parser()

		# Parses words:
		p.readString(self.input_string2)
		p.parseString()
		self.assertEqual(p.words, ["car", "truck", "bus"])
		self.assertEqual(p.numbers, [])
		self.assertEqual(p.order, [1, 1, 1])
		p.reset_parser()

		# Parses numbers:
		p.readString(self.input_string3)
		p.parseString()
		self.assertEqual(p.words, [])
		self.assertEqual(p.numbers, [8, 4, 6, 1, -2, 9, 5])
		self.assertEqual(p.order, [0, 0, 0, 0, 0, 0, 0])
		p.reset_parser()

		# Parses numbers and words:
		p.readString(self.input_string4)
		p.parseString()
		self.assertEqual(p.words, ["car", "truck", "bus"])
		self.assertEqual(p.numbers, [8,4,6,1])
		self.assertEqual(p.order, [1, 1, 0, 0, 1, 0, 0])
		p.reset_parser()

		#Parses multiline string of words and numbers:
		p.readString(self.input_string5)
		p.parseString()
		self.assertEqual(p.words, ['Jessica','is','years','old','and','Daniel','is','years','old','Edward','is','and','his','grandfather','Oscar','is','Eleven'])
		self.assertEqual(p.numbers, [15, -27, 97, 102, 0, 4, 7, 9, 9, 9])
		self.assertEqual(p.order, [1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1])
		p.reset_parser()


	def test_parser_output_string(self):
		p = self.parser
		p.readString(self.input_string5)
		p.parseString()
		num_words = len(p.words)
		num_numbers = len(p.numbers)
		self.assertEqual(len(p.outputString()), num_words + num_numbers)


if __name__ == '__main__':
	unittest.main()
