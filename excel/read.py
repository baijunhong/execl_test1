#-*- coding: utf-8 -*-
from datetime import date,datetime,time
import xlrd
# import sys,codecs
# reload(sys)
# sys.getdefaultencoding()
fname=raw_input('请输入本地文件（.Xls）：')       # fname = "/Users/baijunhong/Downloads/test_2004.xls"
bk = xlrd.open_workbook(fname)
sheet = bk.sheet_by_index(0)   #输出一个表中的标签（table）index用于寻址
#输出表的标名字
print(sheet.name)
#输出列表中的row和col
row_nu=sheet.nrows
col_nu=sheet.ncols
try:
    file_name = open('/Users/baijunhong/Downloads/test.txt','w')
except IOError:
    print('文件不存存在，请先创建一个新文件')
    exit()
row_list = []
for row_index in range(row_nu):
    for col_index in range(col_nu):
        pk = sheet.cell_value(row_index,col_index)
        if (sheet.cell(row_index,col_index).value==u"业务场景ID"):
            continue
        if (sheet.cell(row_index,col_index).value==u"业务场景名称"):
            continue
        if (sheet.cell(row_index,col_index).value==u"业务场景中文名称"):
            continue
        print pk
        row_list.append(pk)
        file_name.write(pk)
file_name.close()
__author__ = 'baijunhong'
