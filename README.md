# ExcelToCVS
## 概述
批处理excel文件中的数据后生.cvs 文件。最终功能只用到main、readAllFile和util三个文件，main负责调用readAllFile和util中的工具类进行数据处理
## util
### getname
**功能：**
获取不带后缀的文件名

`name_with_suffix = filepath.split('/')[-1];`
把字符串通过'/'进行分割，获取分割后的最后一个元素

`name = name_with_suffix.split('.')[0]`
把字符串通过'.'进行分割，获取分割后的第一个元素
### deal_sheet
**功能**
处理excel中的表格，删去header，只保留数据部分
### deal_and_save
**功能**
选择excel中特定的表格，处理数据后加入cvs文件


## readAllFile
读取文件夹中的所有问，返回一个包含所有文件绝对路径的集合

## main
处理文件夹中每一个文件