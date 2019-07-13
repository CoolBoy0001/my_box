#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd
#(pip install xlrd)

class ExcelUtils(object):
    def __init__(self, excel_path, sheet_name):
        # 打开 excel 文件
        self.data = xlrd.open_workbook(excel_path)
        # 获取指定的 sheet
        self.sheet = self.data.sheet_by_name(sheet_name)
        # 获取第一行的值
        self.row = self.sheet.row_values(0)
        # 获取第一列的值
        self.col = self.sheet.col_values(0)
        # excel 表的行数
        self.rowNum = self.sheet.nrows
        # excel 表的列数
        self.colNum = self.sheet.ncols
        # 当前行号
        self.curRowNo = 1

    def has_next(self):
        """
        当行数为0或者读取的行数小于行号时, 返回 False
        :return: True or False type: bool
        """
        if self.rowNum == 0 or self.rowNum <= self.curRowNo:
            return False
        else:
            return True

    def list_in_dict(self):
        """
        生成包含字典的列表数据, 第二行数据作为键, 第三行及之后的数据作为值
        :return: data_list type: list
        """
        data_list = []
        row_val = self.sheet.row_values(1)
        self.curRowNo += 1
        while self.has_next():
            data_dict = {}
            col = self.sheet.row_values(self.curRowNo)
            skip = 1
            for x in range(self.colNum):
                if row_val[x] == "Skip" and col[x] == "Yes":
                    skip = 0
                data_dict.setdefault(row_val[x], col[x])
            if skip == 1:
                data_list.append(data_dict)
            self.curRowNo += 1
        return data_list


# if __name__ == '__main__':
#     value = ExcelUtils("../data/testdata/gateway/ThreePay.xlsx", "PayPage").list_in_dict()
#     print(value)

