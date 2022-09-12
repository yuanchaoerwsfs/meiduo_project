class Test:
    def __init__(self):
        self.first_name = "liu"
        self.last_name = 'jia'

    def get_formatted_name(self):
        """ 返回整洁的姓名 """
        full_name = self.first_name + ' ' + self.last_name
        print("\nHello, " + full_name + "!")
        #  这是一个无限循环 !

    def set_formatted_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    num = property(get_formatted_name, set_formatted_name)


t = Test()
t.get_formatted_name()
t.first_name = "sun"
t.last_name = "quanwei"
t.get_formatted_name()

t.num=
