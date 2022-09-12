from base.do_excel import Do_Excel


def joint_data_json():
    """ 拼接json数据,得到“拼接报文”列表
    :param  无
    :returns: joint_data_list：“拼接报文”列表，列表类型
    """
    joint_data_list = []
    xls_dic = Do_Excel().read_excel()  # 获取表格自定义字段
    rows = xls_dic["行数"]  # 获取表格行数
    for i in range(rows - 1):  # 循环得到“拼接报文”列表
        joint_data = '"' + xls_dic["字段"][i] + '":"' + xls_dic["测试数据"][i] + '"'
        joint_data_list.append(joint_data)
    return joint_data_list


def joint_funcdata():
    """ 拼接单功能的所有报文,得到“功能报文”字典
    :param  无
    :returns: joint_funcdata_dic：“拼接报文”列表，字典类型，key为各功能名称
    """
    xls_dic = Do_Excel().read_excel()  # 获取表格自定义字段
    func_list = xls_dic["功能"]  # “功能列表”的所有值
    new_func_list = set(func_list)  # 去重  [增加班级,测试1,测试2]
    test_datas_list = []  # 功能相同的“拼接报文”
    func_datas_dic = {}  # “功能报文”（以功能为key），未拼接
    joint_funcdata_dic = {}  # “功能报文”（以功能为key），拼接

    # 将功能相同的“拼接报文”分类成一个字典，如{'测试1': ['"":""', '"":""'], '增加班级': ['"dep_name":"test1"', '"master_name":"test1"',
    # '"slogan":"test1"']
    for item in new_func_list:
        for i in range(len(func_list)):
            while (item in func_list):  # [增加班级，增加班级,增加班级,增加班级,测试1,测试1,测试2,测试2]
                row = func_list.index(item)
                test_datas = Do_Excel().sheet.cell(row + 1, 8).value  # 寻找功能相同的“测试数据”数据
                test_datas_list.append(str(test_datas))
                func_list[row] = ''  # 找到元素后占位置空
                i += 1
            else:
                func_datas_dic[item] = test_datas_list  # 将功能相同的“拼接报文”都放在功能报文字典中
                test_datas_list = []
                break
    # 拼接各功能报文，变成功能报文，若功能拼接方式不同，可修改此处
    for keys in new_func_list:
        str1 = ','.join(func_datas_dic[keys])  # 将字典中的值组合成字符串，已逗号分隔
        joint_func_datas = '{"data": [{' + str1 + '}]}'
        joint_funcdata_dic[keys] = joint_func_datas
    return joint_funcdata_dic


if __name__ == '__main__':
    joint_data_json()
    joint_funcdata()
