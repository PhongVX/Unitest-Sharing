class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_full_string_info(self):
        return "My name is {}, i am {} years old and my gender is {}".format(self.name, self.age, self.gender)

    def __private_method(self):
        print('This is private method!')
        return 'private_method'

    def call_private_method(self):
        result = self.__private_method()
        return result



