import sys
import mock
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.modules['my_util'] = mock.Mock()
sys.modules['nonexistent_variable'] = mock.Mock()
sys.modules['nonexistent_library'] = mock.Mock()
sys.modules['nonexistent_function'] = mock.Mock()
sys.modules['nonexistent_exception'] = mock.Mock()



