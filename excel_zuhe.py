import pandas as pd
import numpy as np
import json
import xlwt


import pandas as pd
import re
from pprint import pprint
from paddlenlp import Taskflow


# def convert_excel_to_doccano(excel_file, doccano_file):
#     # 读取Excel文件
#     df = pd.read_excel(excel_file)
#     with open(doccano_file, 'w', encoding='utf-8') as f:
#     # 遍历Excel中的每一行
#         for index, row in df.iterrows():
#             guzhan = row['故障内容']  # 假设文本内容在Excel表格的'text'列中
#             chuli = row['处理方法']
#             juzi = guzhan + chuli
#             f.write(juzi+'\n')
# convert_excel_to_doccano(r'E:/code/行修更换、预防记录（待分析）_张笑瑞_20230412.xlsx', 'E:/code/out1.txt')
#
# file_path = 'E:/code/out1.txt'  # 替换成你的文本文件路径
#
# num_lines = 0
# with open(file_path, 'r',encoding='utf-8') as file:
#     for line in file:
#         num_lines += 1
#
# print("文本文件的行数:", num_lines)
#
work = xlwt.Workbook(encoding = 'utf-8')
wb = xlwt.Workbook('E:/code/zhuhe_result_09191.xls',)
ws = wb.add_sheet("sheet1")
file_name = "E:/code/out1.txt"  # 替换成你的txt文件名
file = open(file_name, 'r',encoding='utf-8')  # 打开文件，以只读模式
# work = xlwt.Workbook(encoding = 'utf-8')
#指定file以utf-8的格式打开
# table = work.add_sheet('data')
ldata=[]
with open('E:/code/zhuhe_result_09191.xls', 'r',encoding='utf-8') as f:
    ws.write(0, 0, '故障描述')
    ws.write(0, 1, '部件名称')
    ws.write(0, 2, '概率数值')
    ws.write(0, 3, '一级配件名称')
    ws.write(0, 4, '概率数值')
    ws.write(0, 5, '部件一级编号')
    ws.write(0, 6, '概率数值')
    ws.write(0, 7, '部件二级名称')
    ws.write(0, 8, '概率数值')
    ws.write(0, 9, '配件编号')
    ws.write(0, 10, '概率数值')
    ws.write(0, 11, '故障标签')
    ws.write(0, 12, '概率数值')
    row = 1  # 写入的起始行
    col = 0  # 写入的起始列
    # 通过row和col的变化实现指向单元格位置的变化
    k = 1
    for lines in file:
        ws.write(row, col, lines)#1行0列
    # 对每一行进行处理，可以在这里添加你的处理逻辑
        schema = ['部件名称', '一级配件名称', '部件一级编号', '部件二级编号', '配件编号', '故障标签']
        model = Taskflow("information_extraction", schema=schema, task_path='E:/code/uie-base/')
        out=model(lines)
        o1=out[0]

        # print(o1)
        # print(type(o1))
        for key, value in o1.items():
            # ws.write(row,col+1,key)#2行1列
            # col += 1
            # print(key,'----------',value)
            # ws.write(row,col+1,"")
            col += 1
            # ws.write(row,col+2,value)
            # print(type(value[0]))
        # for k1,v1 in value[0].items():
        #     print('*****************')
        #     ws.write(row+1,col+1,v1)
        #     col += 1

            # print(type(key))
            # print(type(value))
            value=sorted(value, key=lambda x: x['probability'], reverse=False)

            value1=value[len(value)-1]
            print(key,'+++++',value1)
            # print(type(value1))

            text=value1.pop('text')
            pro = value1.pop('probability')
            # print(text)
            if key==str('部件名称'):
                col=1
                ws.write(row, col, text)  # 2行1列
                col+=1
                ws.write(row , col, pro)
            elif key==str('一级配件名称'):
                col=3
                ws.write(row, col, text)  # 2行1列
                col += 1
                ws.write(row, col, pro)
            elif key==str('部件一级编号'):
                col=5
                ws.write(row, col, text)  # 2行1列
                col += 1
                ws.write(row, col, pro)
            elif key==str('部件二级编号'):
                col=7
                ws.write(row, col, text)  # 2行1列
                col += 1
                ws.write(row, col, pro)
            elif key==str('配件编号'):
                col=9
                ws.write(row, col, text)  # 2行1列
                col += 1
                ws.write(row, col, pro)
            elif key==str('故障标签'):
                col=11
                ws.write(row, col, text)  # 2行1列
                print(text)
                col += 1

                ws.write(row, col, pro)
            # for k1,v1 in value1.items():
            #     ws.write(row+1,col,v1)
            #     col += 1
        row += 1
        col=0
        # print(row)

            # print(a1)
    wb.save("E:/code/zhuhe_result_09191.xls")
# file.close()  # 关闭文件