import xlrd
import xlwt
import xlutils
from xlutils.copy import copy


class Do_Excel():
    def __init__(self):
        self.file = '../test.xls'
        self.workbook = xlrd.open_workbook(filename=self.file, formatting_info=True)  # 打开文件
        self.sheet = self.workbook.sheet_by_index(0)  # 通过索引获取表格对象

    def read_excel(self):
        """ 读取表格数据
        :param  无
        :returns: xls_dic：自定义表格的数据内容，字典类型
        """
        # 获取sheet中的有效列数
        nrows = self.sheet.nrows
        fields_list = self.sheet.col_values(colx=3)  # “字段”列数据
        testdatas_list = self.sheet.col_values(colx=7)  # “测试数据”列数据
        func_list = self.sheet.col_values(colx=1)  # “功能”列数据
        funcdatas_list = self.sheet.col_values(colx=9)  # “功能报文”列数据
        url_list = self.sheet.col_values(colx=2)  # “测试地址”列数据

        xls_dic = {"行数": nrows,
                   "字段": fields_list[1:],
                   "测试数据": testdatas_list[1:],
                   "功能": func_list[1:],
                   "功能报文": funcdatas_list[1:],
                   "测试地址": url_list[1:]}
        return xls_dic

    def write_excel(self, row, col, joint_data):
        """ 数据写入表格
        :param  i: 第i行写入数据，整型类型
                joint_data：写入的数据内容，字符串类型
                testdatas_list：“测试数据”列数据，列表类型
        :returns: 无
        """
        # 创建样式
        borders = xlwt.Borders()  # 创建边框
        style = xlwt.XFStyle()  # Create Style
        style.borders = borders  # Add Borders to Style
        borders.left = xlwt.Borders.THIN  # 实线
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40
        workbook_copy = copy(self.workbook)
        sheet_copy = workbook_copy.get_sheet(0)

        sheet_copy.write(row, col, label=joint_data, style=style)  # 写入数据
        workbook_copy.save(self.file)  # 保存表格


if __name__ == '__main__':
    do = Do_Excel()
    do.read_excel()
    do.write_excel("22")
