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

		
if __name__ == '__main__':
    unittest.main()