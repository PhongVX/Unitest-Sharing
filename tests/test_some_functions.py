import unittest
import mock
import context


class TestSomeFunctions(unittest.TestCase):
    def test_add(self):
        # Arrange
        mock_num1 = 2
        mock_num2 = 3
        #Act
        from application.some_functions import sum
        result = sum(mock_num1, mock_num2)
        #Assert
        self.assertEqual(result, 5)

    def test_mul(self):
        #Arrange
        mock_num1 = 2
        mock_num2 = 3
        #Act
        from application.some_functions import mul
        result = mul(mock_num1, mock_num2)
        #Assert
        self.assertEqual(result, 6)

    @mock.patch("application.some_functions.sum")
    def test_perimeter_of_rectangle(self, mock_sum):
        #Arrange
        mock_num1 = 2
        mock_num2 = 3
        #Act
        mock_sum.return_value = 5
        from application.some_functions import perimeter_of_rectangle
        result = perimeter_of_rectangle(mock_num1, mock_num2)
        #Assert
        self.assertEqual(result, 10)

    @mock.patch("application.some_functions.max_func")
    @mock.patch("application.some_functions.min_func")
    def test_medium(self, mock_min_func, mock_max_func):
        #Arrange
        mock_min_func.return_value = 1
        mock_max_func.return_value = 4
        #Act
        from application.some_functions import medium
        result  = medium(2,3,1,4)
        expected_result = [2,3]
        #Assert
        self.assertEqual(result,expected_result)

    def test_function_return_multiple_value(self):
        # Act
        from application.some_functions import function_return_multiple_value
        result_sum, result_mul = function_return_multiple_value(2,3)
        # Assert
        self.assertEqual(result_sum, 5)
        self.assertEqual(result_mul, 6)

    @mock.patch("application.some_functions.utf8_encoding_function")
    def test_encode_utf8_and_to_lower_string(self, mock_utf8_encoding_function):
        # Arrange
        my_string = "Tôi Là Ai"
        mock_utf8_encoding_function.return_value = "Toi La Ai"
        # Act
        from application.some_functions import encode_utf8_and_to_lower_string
        result = encode_utf8_and_to_lower_string(my_string)
        expected_result = "_toi la ai_"
        # Assert
        self.assertEqual(result, expected_result)

    @mock.patch("application.some_functions.PI", 3.14)
    def test_area_circle(self):
        # Act
        from application.some_functions import area_circle
        result = area_circle(4)
        # Assert
        self.assertEqual(result, 50.24)


if __name__ == "__main__":
    unittest.main(verbosity=2)