import unittest
from src.gridworld import Gridworld

gw = Gridworld(4, 5, 0, 19)

class TestGridworld(unittest.TestCase):
    def test_get_actions(self):
        output = gw.get_actions(0)
        self.assertListEqual(output, ['E', 'S'])
        output = gw.get_actions(19)
        self.assertListEqual(output, ['W', 'N'])
        output = gw.get_actions(6)
        self.assertListEqual(output, ['W', 'E', 'N', 'S'])
        output = gw.get_actions(10)
        self.assertListEqual(output, ['E', 'N', 'S'])

    def test_apply_action(self):
    
        expected = [1, 7, 11, 5]
        for action, result in zip(["N", "E", "S", "W"], expected):
            output = gw.apply_action(6, action)
            self.assertEqual(result, output)
        
        expected = [0, 6, 10, 5]
        for action, result in zip(["N", "E", "S", "W"], expected):
            output = gw.apply_action(5, action)
            self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
