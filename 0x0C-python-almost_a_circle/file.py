#!/usr/bin/python3
import unittest



class TestStringMethod(unittest.TestCase):
    def setUp(self) -> None:
        ...

        # return super().setUp()
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_issuper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        self.assertEqual('Hello World'.split(), ['Hello', 'World'])
        with self.assertRaises(TypeError):
            'Hello World'.split(2)

    def tearDown(self) -> None:
        ...

if __name__ == '__main__':
    unittest.main()
