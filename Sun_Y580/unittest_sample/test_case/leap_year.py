class Leap_Year:
    """"计算某年是否为闰年"""

    def __init__(self, year):
        self.year = int(year)

    def answer(self):
        year = self.year
        if year % 100 == 0:
            if year % 400 == 0:
                # 能被400整除的是世纪闰年
                return "{0}是闰年".format(year)
            else:
                return "{0}不是闰年".format(year)
        else:
            if year % 4 == 0:
                # 非整百能被4整除的闰年
                return "{0}是闰年".format(year)
            else:
                return "{0}不是闰年".format(year)
