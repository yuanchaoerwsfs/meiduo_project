class ItCast():
    def __init__(self, subject):
        self.subject1 = subject
        self.subject2 = 'cpp'

    def show(self):
        print("this is ItCast")

    def __getattribute__(self, item):
        print("log1")
        if item == "subject1":
            print("log2")
            return "redirect python"
        else:
            print("log3")
            return object.__getattribute__(self, item)


s = ItCast("python")
print(s.subject1)
print(s.subject2)
print("*"*50)
s.show()