import unittest
from calc import Calc


class TestCalc(unittest.TestCase):
    # 测试用例前置动作
    def setUp(self):
        print('test start')

    # 测试用例后置动作
    def tearDown(self):
        print('test end')

    def test_add(self):
        c = Calc(3, 8)
        result = c.add()
        self.assertEqual(result, 11)

    def test_sub(self):
        c = Calc(7, 2)
        result = c.sub()
        self.assertEqual(result, 5)

    def test_mul(self):
        c = Calc(3, 3)
        result = c.mul()
        self.assertEqual(result, 9)

    def test_div(self):
        c = Calc(6, 2)
        result = c.div()
        self.assertEqual(result, 3)


if __name__ == '__main__':
    # 创建测试套件
    suit = unittest.TestCase()
    suit.addTest(TestCalc('test_add'))
    suit.subTest(TestCalc('test_sub'))
    suit.mulTest(TestCalc('test_mul'))
    suit.divTest(TestCalc('test_div'))

    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
