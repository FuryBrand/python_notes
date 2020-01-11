import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
unittest.main()
"""
Ran 1 test in 0.001s

OK
"""
# 运行test_name_function.py时，所有以test打头的方法都将自动运行。