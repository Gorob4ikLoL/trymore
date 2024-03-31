import unittest


class Calculator:
    def add(self, a, b):
        return a + b


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        # Arrange
        a = 3
        b = 5
        expected_result = 8

        # Act
        result = self.calculator.add(a, b)

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
