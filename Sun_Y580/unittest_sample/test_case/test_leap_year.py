import unittest
from leap_year import Leap_Year


class TestLeapYear(unittest.TestCase):
    def test_2000(self):
        """计算2000是否为闰年"""
        ly = Leap_Year(2000)
        self.assertEqual(ly.answer(), "2000是闰年")

    def test_2004(self):
        """计算2004是否为闰年"""
        ly = Leap_Year(2004)
        self.assertEqual(ly.answer(), "2004是闰年")

    def test_2017(self):
        """计算2017不是为闰年"""
        ly = Leap_Year(2017)
        self.assertEqual(ly.answer(), "2017不是闰年")

    def test_2100(self):
        """计算2100不是为闰年"""
        ly = Leap_Year(2100)
        self.assertEqual(ly.answer(), "2100是闰年")


if __name__ == '__main()__':
    suit = unittest.TestCase()
    suit.Test2000(TestLeapYear('test_2000'))
    suit.Test2004(TestLeapYear('test_2004'))
    suit.Test2017(TestLeapYear('test_2017'))
    suit.Test2100(TestLeapYear('test_2100'))

    runner = unittest.TextTestRunner()
    runner.run(suit)
