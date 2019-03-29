import unittest
import mock
import context


class TestThingsDecorator(unittest.TestCase):
    @mock.patch('nonexistent_library.nonexistent_decorator')
    def test_unit_1(self, mock_nonexistent_decorator):
        # arrange
        mock_nonexistent_decorator.return_value = mock.Mock()
        # action
        from application.some_decorators import function_with_decorator
        result = function_with_decorator()
        # assert
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()







