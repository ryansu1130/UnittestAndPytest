import wordCount
import unittest

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(wordCount.testWordCount("This is an activity"), 4)

    def testTwo(self):
        '''Test Two is designed to FAIL'''
        self.assertEqual(wordCount.testWordCount("This is Not an activity"), 4)

    def testThree(self):
        self.assertEqual(wordCount.testWordCount("Hello World"), 2)

    def testFour(self):
        '''Test Four is designed to FAIL'''
        self.assertEqual(wordCount.testWordCount("This is an activity     "), 4)

if __name__ == '__main__':
    unittest.main()
