import unittest
from gradebook import display_averages, read_grades_file

class TestGradebook(unittest.TestCase):

    def test_file_exists(self):
        expected_names = ['Pari', 'Igor', 'Giovanni']
        expected_grades = [
            [90, 88.5, 82, 95, 99.5],
            [78, 88.5, 77.25, 99, 100],
            [74, 89.25, 90, 99, 100]
        ]
        result = read_grades_file('grades.txt')
        self.assertTrue(result and expected_names == result[0] and expected_grades == result[1])

    def test_file_does_not_exist(self):
        result = read_grades_file('grades.tt')
        self.assertFalse(result)

    def test_display_exception(self):        
        self.assertRaises(ValueError, display_averages, ['a', 'b'], [[1, 2]])

if __name__ == '__main__':
    unittest.main()
