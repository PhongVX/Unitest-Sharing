import nonexistent_function
from nonexistent_exception import MyException

def function_for_generate_exit_sample(my_list):
    if not isinstance(my_list, list):
        raise MyException('It is not a instance of list')
    print ("Do something more")
    return True




