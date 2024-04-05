import unittest

from maze import *

# tag, value, children, props
class TestMaze(unittest.TestCase):
    def test_create_maze(self):
        numCols = 12
        numRows = 16
        m1 = Maze(0, 0, numRows, numCols, 10, 10)
        actual = [len(m1.cells), len(m1.cells[0])]
        expected = [numCols, numRows]
        self.log_test("test_create_maze", expected, actual)
        self.assertEqual(expected, actual)

    def log_test(self, name, expected, actual):
        print(f"\nRunning {name}")
        print(f"actual:  {actual} \nexpected: {expected}")
        print("============================================================")


if __name__ == "__main__":
    unittest.main()