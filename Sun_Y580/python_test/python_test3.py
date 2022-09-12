def out_(func):
    print('---out_------')
    def in_():
        func()
    return in_

@out_
def test():
    print('----test-----')



test()