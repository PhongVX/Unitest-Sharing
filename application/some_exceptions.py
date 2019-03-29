import nonexistent_function
from nonexistent_exception import MyException

def try_and_except_function():
    try:
        nonexistent_function()
        print('...Some Code...')
        return True
    except Exception:
        print('...Some Code...')
        raise ValueError('except')


def try_and_except_function_nonexistent_exception():
    try:
        nonexistent_function()
        print('...Some Code...')
        return True
    except Exception:
        print('...Some Code...')
        raise MyException('my exception')


