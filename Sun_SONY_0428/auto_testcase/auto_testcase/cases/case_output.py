from do_jointdata import joint_data_json,joint_funcdata
from do_excel import Do_Excel


def output_testdata():
    pass


def output_jointdata():
    """ 执行后，表格填写“拼接报文”列
    :param  无
    :returns: 无
    """
    joint_data_list = joint_data_json()  # 获得“拼接报文”列表
    for i in range(len(joint_data_list)):  # 每行写入拼接列表的数据
        Do_Excel().write_excel(i + 1, 8, joint_data_list[i])


def output_joint_funcdatas():
    """ 执行后，表格填写“功能报文”列
    :param  无
    :returns: 无
    """
    joint_funcdata_dic = joint_funcdata()  # 得到“功能报文”字典
    xls_dic = Do_Excel().read_excel()  # 获取表格自定义字段
    func_list = xls_dic["功能"]  # “功能列表”的所有值
    for i in range(xls_dic["行数"] - 1):  # 每行根据功能名称的key，写入“功能报文”字典的值
        Do_Excel().write_excel(i + 1, 9, joint_funcdata_dic[func_list[i]])


if __name__ == '__main__':
    output_jointdata()
    output_joint_funcdatas()
