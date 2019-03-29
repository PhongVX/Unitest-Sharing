import unittest
import mock
import context

from application.some_classes import Person


class TestSomeClasses(unittest.TestCase):

    @mock.patch.object(Person, '__init__', lambda self, name, age, gender: None)  # mock init
    def test_first_function(self):
        # Create class
        person_class = Person('Phong Vo', '24', 'male')
        # Arrage
        person_class.name = "Phong Vo"
        person_class.age = 24
        person_class.gender = "male"
        # Action
        result = person_class.get_full_string_info()
        # Assert
        self.assertEqual(result, "My name is Phong Vo, i am 24 years old and my gender is male")

    @mock.patch.object(Person, '__init__', lambda self, name, age, gender: None)  # mock init
    def test_call_private_method(self):
        # Create class
        person_class = Person('Phong Vo', '24', 'male')
        # Arrage
        person_class.name = "Phong Vo"
        person_class.age = 24
        person_class.gender = "male"
        with mock.patch.object(Person, '_Person__private_method', return_value='private_method') as mock_private_method:
            # Action
            result = person_class.call_private_method()
            # Assert
            self.assertEqual(result, 'private_method')
            mock_private_method.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
