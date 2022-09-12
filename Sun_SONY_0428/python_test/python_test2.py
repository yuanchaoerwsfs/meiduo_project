def get_formatted_name(first_name, last_name):
    """ 返回整洁的姓名 """
    full_name = first_name + ' ' + last_name
    return full_name.title()
    #  这是一个无限循环 !

temp=True
while temp:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    if f_name!='Q' or f_name!='q':
        l_name = input("Last name: ")
        formatted_name = get_formatted_name(f_name, l_name)
        print("\nHello, " + formatted_name + "!")
