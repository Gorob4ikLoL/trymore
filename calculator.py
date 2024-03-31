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
import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


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

    def test_subtraction(self):
        # Arrange
        a = 10
        b = 4
        expected_result = 6

        # Act
        result = self.calculator.subtract(a, b)

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


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

    def test_subtraction(self):
        # Arrange
        a = 10
        b = 4
        expected_result = 6

        # Act
        result = self.calculator.subtract(a, b)

        # Assert
        self.assertEqual(result, expected_result)

    def test_multiplication(self):
        # Arrange
        a = 2
        b = 3
        expected_result = 6

        # Act
        result = self.calculator.multiply(a, b)

        # Assert
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
import unittest


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


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

    def test_subtraction(self):
        # Arrange
        a = 10
        b = 4
        expected_result = 6

        # Act
        result = self.calculator.subtract(a, b)

        # Assert
        self.assertEqual(result, expected_result)

    def test_multiplication(self):
        # Arrange
        a = 2
        b = 3
        expected_result = 6

        # Act
        result = self.calculator.multiply(a, b)

        # Assert
        self.assertEqual(result, expected_result)

    def test_division(self):
        # Arrange
        a = 10
        b = 2
        expected_result = 5

        # Act
        result = self.calculator.divide(a, b)

        # Assert
        self.assertEqual(result, expected_result)

        # Arrange for division by zero
        a = 5
        b = 0

        # Act & Assert
        with self.assertRaises(ValueError):
            self.calculator.divide(a, b)


if __name__ == '__main__':
    unittest.main()
