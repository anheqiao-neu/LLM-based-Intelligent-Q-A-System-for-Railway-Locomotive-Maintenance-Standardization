from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import math
import datetime
# # #---------------取出未聚类这种文件中所有标注的excel---------------------#
file = open(r"E:\code\040807\未聚类.txt", 'r',encoding='gbk')
sum=[]
sum_1=[]
lines = file.readlines()
# print(lines)
num = len(lines)

xlsx_all=pd.read_excel(r"E:\code\040809\视频安防故障_行修更换.xlsx")
num_all=len(xlsx_all.values)
#
NUM_I=[]
for i in range(0,num):
    # print(lines[i])
    si=lines[i].split("&")
    sum.append(si)
    sum1 = pd.DataFrame(sum, columns=['故障现象描述', '处理情况'])
num_l=len(sum1.values)

for i in range(0,num_l):
    # print(sum1.values[i][0])
    j=0
    while j< num_all:
        if str(sum1.values[i][0]) == str(xlsx_all.values[j][6]) and str(sum1.values[i][1]) == str(xlsx_all.values[j][7])+'\n':
            sum_1.append(xlsx_all.values[j])
            s=pd.DataFrame(sum_1, columns=xlsx_all.columns)
                # print(s)
                # print("-----------------------------------")
            print(s)
            # i += 1
            file = r"E:\code\040807"
            s.to_excel(f'{file}/未聚类.xlsx', index=False)
            break
        else:
            j+=1
#-------------------------------取出所有标注的excel--------------------------------------------#

# #--------------------------按比例提取聚类文件----------------------------------------------#
# import os
# dfs=[]
# #os.walk(file_path) 深度遍历file_path下的所有子文件夹及文件
# for root_dir,sub_dir,files in os.walk(r"E:\code\data_0408_09"):
#     for file in files:
#         if file.endswith(".xlsx"):
#             #构造绝对路径
#             file_name = os.path.join(root_dir, file)
#             # print(file_name)
#             # dfs.append(pd.read_excel(file_name))
#             dfs1=pd.read_excel(file_name)
#             num=len(dfs1)*1
#             num1=math.ceil(num)
#             # print("$$$$$$$$$$$$$$")
#             # print(dfs1.sample(n=num1))
#             # print("**************")
#             dfs.append(dfs1.sample(n=num1))
# data_all = pd.concat(dfs)
# data_all.to_excel(r"E:\code\040809\聚类整合9.xlsx", index=False)
# #--------------------------按比例提取聚类文件----------------------------------------------#