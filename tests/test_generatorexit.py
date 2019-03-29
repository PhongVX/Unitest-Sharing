import unittest
import mock
import context


class TestSomeGeneratorExit(unittest.TestCase):

    @mock.patch("application.some_generatorexit.list", GeneratorExit)
    @mock.patch("application.some_generatorexit.MyException", Exception)
    def test_function_for_generate_exit_sample(self):
        # Arrange
        my_list = list()
        #Act
        from application.some_generatorexit import function_for_generate_exit_sample
        with self.assertRaises(Exception) as context:
            function_for_generate_exit_sample(my_list)
        #Assert
        self.assertTrue('It is not a instance of list' in str(context.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)





