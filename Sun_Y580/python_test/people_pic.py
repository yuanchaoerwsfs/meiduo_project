card_infors = []


def print_menu():
    """完成打印功能菜单"""
    print("= " * 50)
    print("   名片管理系统 V0.01")
    print(" 1. 添加一个新的名片")
    print(" 2. 删除一个名片")
    print(" 3. 修改一个名片")
    print(" 4. 查询一个名片")
    print(" 5. 显示所有的名片")
    print(" 6. 保存信息")
    print(" 7. 退出系统")
    print("= " * 50)


def add_new_card_infor():
    name = input("请输入你的名字：")
    sex = input("请输入你的性别：")
    wechat = input("请输入你的微信：")
    site = input("请输入你的地址：")
    new_infor = {'name': name, 'sex': sex, 'wechat': wechat, 'site': site}


def find_card_infor():
    global  card_infors
    for temp in card_infors:
        print(temp['name'],temp['sex'],temp['wechat'],temp['site'])



def show_all_infor():
    pass


def save_2_file():
    pass


def load_infor():
    pass


def main():
    """完成对整个程序的控制"""

    # 恢复(加载)之前的数据到程序中
    load_infor()

    # 1. 打印功能提示
    print_menu()

    while True:

        # 2. 获取用户的输入
        num = int(input("请输入操作序号:"))

        # 3. 根据用户的数据执行相应的功能
        if num == 1:
            add_new_card_infor()
        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            find_card_infor()
        elif num == 5:
            show_all_infor()
        elif num == 6:
            save_2_file()
        elif num == 7:
            break
        else:
            print("输入有误,请重新输入")

        print("")


if __name__ == "__main__":
    # 调用主函数
    main()
