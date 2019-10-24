import unittest
import main

class Testmain(unittest.TestCase):
    def test_do_stuff1(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 100)

    def test_do_stuff2(self):
        test_param = "test String"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number:')


if __name__ == "__main__":
    unittest.main()