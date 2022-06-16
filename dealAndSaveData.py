# 引入Excel库的xlrd
import datetime
import readAllFile as raf
import xlrd
dir=raf.readDir("C:/Users/ren.cai\Desktop/0615")
print(dir[0])
pname=dir[0].split("/")[-1] #输出为 class1.py
print(pname)
pname1=pname.split('.')[0]
print(pname1)
# 导入需要读取Excel表格的路径

data = xlrd.open_workbook(r'C:\Users\ren.cai\Desktop\0615\ASDM GPILOT2 Active Safety Domain Master GPILOT2 (VDS) '
                          r'8889115097  J.xlsx')
table = data.sheet_by_name("DTC")

tables = []

# 将excel表格内容导入到tables列表中

def import_excel(excel):
    for rown in range(3,excel.nrows):
        strtemp= excel.cell_value(rown, 1) + '|' + excel.cell_value(rown, 3) + ';'
        tables.append([strtemp])

if __name__ == '__main__':

    # 将excel表格的内容导入到列表中

    import_excel(table)

    # 验证Excel文件存储到列表中的数据

    for i in tables:
        print(i)

import csv

with open(file='b.csv', mode='w', encoding='utf-8', newline='') as f:

    f_scv = csv.writer(f)
    for item in tables:
        f_scv.writerow(item)
