from main import shift, convertToList
import unittest

class testfunctions(unittest.TestCase):
    def testConvertTolist(self):
        self.assertEqual(convertToList(None), "No string entered.")
        self.assertEqual(convertToList(""), "No string entered.")
        self.assertEqual(convertToList(" "), [" "])
        sentence = "The rain in Spain falls mainly in the plains."
        lst = list(sentence)
        self.assertEqual(convertToList(sentence), lst)

    def testShift(self):
        self.assertEqual(shift(None), "No string entered.")
        sentence = "The rain in Spain falls mainly in the plains."
        lst = list(sentence)
        encrypt = 'Uif sbjo jo Tqbjo gbmmt nbjomz jo uif qmbjot.'
        self.assertEqual(shift(lst), encrypt)
		self.assertEqual(shift(sentence), "No string entered.")
        self.assertEqual(shift(""), "No string entered.")


if __name__ == '__main__': 
    unittest.main()