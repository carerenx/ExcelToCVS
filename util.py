# 引入Excel库的xlrd
import os

import xlrd
import csv

tables = []


# 将excel表格内容导入到tables列表中
def deal_sheet(excel):
    atable = []
    for rown in range(3, excel.nrows):
        if excel.cell_value(rown, 1) != '':
            strtemp1 = excel.cell_value(rown, 1) + '|' + excel.cell_value(rown, 3) + ';'
            atable.append([strtemp1])
    return atable


def getname(filepath):
    name_with_suffix = filepath.split('/')[-1];
    name = name_with_suffix.split('.')[0]
    return name


def print_table(table):
    # 将excel表格的内容导入到列表中

    deal_sheet(table)

    # 验证Excel文件存储到列表中的数据

    for i in tables:
        print(i)


def deal_and_save(filepath):
    # 导入需要读取Excel表格的路径
    data = xlrd.open_workbook(filepath)
    table = data.sheet_by_name("DTC")
    tables = deal_sheet(table)

    for i in tables:
        print(i)

    current_directory = os.path.dirname(os.path.abspath(__file__)) + '/output_csv/'
    print(current_directory + getname(filepath))

    # with open是python 中打开文件的命令，在使用完毕后会自动关闭。mode有w/r/a，w：删除后写入，a：尾部添加写入，r：读取
    with open(current_directory + getname(filepath) + '.csv', mode='w', encoding='utf-8', newline='') as f:
        f_scv = csv.writer(f)
        for item in tables:
            f_scv.writerow(item)
