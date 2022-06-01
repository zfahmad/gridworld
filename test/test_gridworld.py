import unittest
from src.gridworld import Gridworld

gw = Gridworld(4, 5, 0, 19)

class TestGridworld(unittest.TestCase):
    def test_get_actions(self):
        expected = ["N", "S", "E", "W"]
        output = gw.get_actions(0)
        self.assertListEqual(output, expected)
        output = gw.get_actions(19)
        self.assertListEqual(output, expected)
        output = gw.get_actions(6)
        self.assertListEqual(output, expected)
        output = gw.get_actions(10)
        self.assertListEqual(output, expected)

    def test_apply_action(self):
    
        expected = [1, 7, 11, 5]
        for action, result in zip(["N", "E", "S", "W"], expected):
            output = gw.apply_action(6, action)
            self.assertEqual(result, output)
        
        expected = [0, 6, 10, 5]
        for action, result in zip(["N", "E", "S", "W"], expected):
            output = gw.apply_action(5, action)
            self.assertEqual(result, output)
        
    def test_is_goal(self):
        output = gw.is_goal(19)
        self.assertTupleEqual(output, (True, 1))
        output = gw.is_goal(1)
        self.assertTupleEqual(output, (False, 0))


if __name__ == '__main__':
    unittest.main()
