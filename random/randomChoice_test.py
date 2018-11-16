from randomChoice import random_nums
import unittest
import random

class RandomTest(unittest.TestCase):

    def test_choice(self):
        nums = random_nums()
        self.assertIn(random.choice(nums), nums)

if __name__ == '__main__':
  unittest.main()
