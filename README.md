# Unit Test In Python


    import unittest

    class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  # test method names begin with 'test'
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)
        def testMultiply(self):
            self.assertEqual((0 * 10), 0)
            self.assertEqual((5 * 8), 40)

    if __name__ == '__main__':
        unittest.main()


### Assert Methods
    # test if a == b
      assertEqual(a, b)

    # test if a != b
      assertNotEqual(a, b)

    # test if x is True
      assertTrue(x)

    # test if x is False
      assertFalse(x)

    # test if a is b
      assertIs(a, b)

    # test if a is not b
      assertIsNot(a, b)

    # test if x is None
      assertIsNone(x)

    # test if x is not None
      assertIsNotNone(x)

    # test if a in b
      assertIn(a, b)

    # test if a not in b
      assertNotIn(a, b)

    # test if isinstance(a, b)
      assertIsInstance(a, b)

    # test if not isinstance(a, b)
      assertNotIsInstance(a, b)

    # test raise exception
      assertRaises(exception, fonction, *args, **kwargs)
