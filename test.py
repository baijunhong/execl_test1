#-*- coding: utf-8 -*-
from datetime import date,datetime,time
import xlrd
# import sys,codecs
# reload(sys)
# sys.getdefaultencoding()
fname = "/Users/baijunhong/Downloads/test_2004.xls"
bk = xlrd.open_workbook(fname)
sheet = bk.sheet_by_index(0)   #输出一个表中的标签（table）index用于寻址
#输出表的标名字
print(sheet.name)
#输出列表中的row和col
print sheet.nrows
# print sheet.ncols
# for row_index in range(sheet.nrows):
#     for col_index in range(sheet.ncols):
#         pk = sheet.cell_value(row_index,col_index)
#         print pk
cell = sheet.cell(1,0)
print cell
print cell.value
print cell.ctype

for i in range(sheet.ncols):
    print sheet.cell_type(1,i),sheet.cell_value(1,i)


__author__ = 'baijunhong'
