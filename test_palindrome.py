import unittest
import palindrome

class TestCase(unittest.TestCase):
    def testOne(self):
        self.assertEqual(palindrome.testPalindrome("racecar"), True)
    def testTwo(self):
        self.assertEqual(palindrome.testPalindrome("human"), False)
    def testThree(self):
        self.assertEqual(palindrome.testPalindrome("saippuakivikauppias"), True)
    def testFour(self):
        '''Test Four Is Written To Fail On Purpose'''
        self.assertEqual(palindrome.testPalindrome("saippuakivikauppias"), False)

if __name__ == '__main__':
    unittest.main()
