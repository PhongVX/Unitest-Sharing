import unittest
import mock
import context


class TestSomeExceptions(unittest.TestCase):
    @mock.patch("application.some_exceptions.nonexistent_function")
    def test_try_and_except_function(self, mock_nonexistent_function):
        # Arrange
        mock_nonexistent_function.side_effect = Exception('except')
        #Act
        from application.some_exceptions import try_and_except_function
        with self.assertRaises(Exception) as context:
            try_and_except_function()
        #Assert
        self.assertTrue('except' in str(context.exception))

    @mock.patch("application.some_exceptions.MyException", Exception)
    @mock.patch("application.some_exceptions.nonexistent_function")
    def test_try_and_except_function_nonexistent_exception(self, mock_nonexistent_function):
        # Arrange
        mock_nonexistent_function.side_effect = Exception('except')
        # Act
        from application.some_exceptions import try_and_except_function_nonexistent_exception
        with self.assertRaises(Exception) as context:
            try_and_except_function_nonexistent_exception()
        # Assert
        self.assertTrue('my exception' in str(context.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)