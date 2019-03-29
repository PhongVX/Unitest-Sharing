import unittest
tests = unittest.TestLoader().discover('.', pattern='test*.py')
result = unittest.TextTestRunner(verbosity=2).run(tests)



