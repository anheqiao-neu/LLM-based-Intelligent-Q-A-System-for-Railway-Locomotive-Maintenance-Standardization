#先导入数据
import pandas as pd
import numpy as np
import json

import pandas as pd
import re


def find_brute(text, pattern):
    """如果子串pattern存在text中，则返回pattern在text中起始位置索引，否则返回-1"""
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):  # 从索引0至n - m处依次尝试开始匹配
        k = 0
        while k < m and text[i + k] == pattern[k]:  # 第k个字符匹配
            k += 1
        if k == m:  # 判断此轮for循环是否成功匹配
            return i  # 子串text[i:i + m]和pattern匹配
    return -1

def convert_excel_to_doccano(excel_file, doccano_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file)

    # 创建doccano格式的列表
    doccano_data1 = {}
    doccano_data2 = {}
    doccano_data3 = {}
    doccano_data4 = {}
    doccano_data5 = {}
    doccano_data6 = {}

    err_num = 0
    with open(doccano_file, 'w', encoding='utf-8') as f:
    # 遍历Excel中的每一行
        for index, row in df.iterrows():
            guzhan = row['故障内容']  # 假设文本内容在Excel表格的'text'列中
            chuli = row['处理方法']
            bujianmc = row['部件名称']
            peijianmc = row['一级配件名称']
            bujian1 = row['部件一级编号']
            bujian2 = row['部件二级编号']
            peijianbh = row['配件编号']
            gzbiaoqian = row['故障标签']
            juzi = str(guzhan) + str(chuli)
            # 创建doccano格式的字典
            num1 = len(bujianmc)
#去重比如语音箱-语音箱
            name = bujianmc
            newname = ''
            for char in name:
                if char not in newname:
                    newname += char
            bujianmc = newname

            name1 = gzbiaoqian
            newname1 = ''
            for char in name1:
                if char not in newname1:
                    newname1 += char
            gzbiaoqian = newname1

            #print(bujianmc)
            start = juzi.find(bujianmc) #句子中有关键字
            start_1peijian = juzi.find(str(peijianmc))
            start_1bujian = juzi.find(str(bujian1))
            start_2bujian = juzi.find(str(bujian2))
            start_bh = juzi.find(str(peijianbh))
            start_gz = juzi.find(str(gzbiaoqian))
            s1=int()

            # ----------故障标签
            if start_gz != -1:
                s_gz = start_gz
                kg_gz = gzbiaoqian
            # else:
            #     s_gz=0
            else:
                c_gz = list(str(gzbiaoqian))
                count_gz = []
                for i in c_gz:
                    if juzi.find(i) != -1:
                        j_gz = i
                        count_gz.append(j_gz)
                print(count_gz)
                kg_gz = ''
                # 将列表中的字符串转为字符串
                for item in count_gz:
                    kg_gz = kg_gz + str(item)
                # print(kg)
                # if len(kg)==0:
                #     print('-1')
                s_gz = juzi.find(kg_gz)
            if s_gz != -1:
                s_gz = s_gz
            else:
                if str(kg_gz).islower() or str(kg_gz).isupper():  # 筛选出带英文的
                    kg_gz = ''.join(re.findall(r'[A-Za-z]', kg_gz))
                    s_gz = juzi.find(kg_gz)
                    print(s_gz)
                else:
                    s_gz = 99999

            # ----------配件编号
            if start_bh != -1:
                s_bh = start_bh
                kg_bh = peijianbh
            else:
                c_bh = list(str(peijianbh))
                count_bh = []
                for i in c_bh:
                    if juzi.find(i) != -1:
                        j_bh = i
                        count_bh.append(j_bh)
                kg_bh = ''
                # 将列表中的字符串转为字符串
                for item in count_bh:
                    kg_bh = kg_bh + str(item)
                # print(kg)
                # if len(kg)==0:
                #     print('-1')
                s_bh = juzi.find(kg_bh)
            if s_bh != -1:
                s_bh = s_bh
            else:
                if str(kg_bh).islower() or str(kg_bh).isupper():  # 筛选出带英文的
                    kg_bh = ''.join(re.findall(r'[A-Za-z]', kg_bh))
                    s_bh = juzi.find(kg_bh)
                else:
                    s_bh = 99999

            # ----------部件一级编号
            if start_1peijian != -1:
                s2_bj = start_2bujian
                kg2_bj = bujian2
            else:
                c2_bj = list(str(bujian2))
                count2_bj = []
                for i in c2_bj:
                    if juzi.find(i) != -1:
                        j2_bj = i
                        count2_bj.append(j2_bj)
                kg2_bj = ''
                # 将列表中的字符串转为字符串
                for item in count2_bj:
                    kg2_bj = kg2_bj + str(item)
                # print(kg)
                # if len(kg)==0:
                #     print('-1')
                s2_bj = juzi.find(kg2_bj)
            if s2_bj != -1:
                s2_bj = s2_bj
            else:
                if str(kg2_bj).islower() or str(kg2_bj).isupper():#筛选出带英文的
                    kg2_bj = ''.join(re.findall(r'[A-Za-z]', kg2_bj))
                    s2_bj = juzi.find(kg2_bj)
                else:
                    s2_bj = 99999

            #----------部件一级编号
            if start_1peijian != -1:
                s1_bj = start_1bujian
                kg1_bj = bujian1
            else:
                c1_bj = list(str(bujian1))
                count1_bj = []
                for i in c1_bj:
                    if juzi.find(i) != -1:
                        j1_bj = i
                        count1_bj.append(j1_bj)
                kg1_bj = ''
                # 将列表中的字符串转为字符串
                for item in count1_bj:
                    kg1_bj = kg1_bj + str(item)
                # print(kg)
                # if len(kg)==0:
                #     print('-1')
                s1_bj = juzi.find(kg1_bj)
            if s1_bj!=-1:
                s1_bj=s1_bj
            else:
                # if str(kg1_bj).islower() or str(kg1_bj).isupper():#筛选出带英文的
                #     kg1_bj = ''.join(re.findall(r'[A-Za-z]', kg))
                #     s1_bj = juzi.find(kg1_bj)
                # else:
                    s1_bj=99999

            #-----------一级配件名称
            if start_1peijian !=-1:
                # -----一级配件
                s1_pj = start_1peijian
                kg1_pj = peijianmc
            else:
                # -----一级配件
                c1_pj = list(str(peijianmc))
                count1_pj = []

                #-----一级配件
                for i in c1_pj:
                    if juzi.find(i) !=-1:
                        j1_pj=i
                        count1_pj.append(j1_pj)
                kg1_pj = ''
                #将列表中的字符串转为字符串
                for item in count1_pj:
                    kg1_pj=kg1_pj+str(item)
                #print(kg)
                # if len(kg)==0:
                #     print('-1')
                s1_pj = juzi.find(kg1_pj)
            if start != -1:
                #-----部件
                s1= start
                kg = bujianmc

                #print(s1)
            else:
                #-----部件
                c1=list(bujianmc) #将关键字拆成列表
                count1=[]

                # print(c1)
                for i in c1:
                    if juzi.find(i) != -1: #列表中的元素在句子中存在
                        j1=i
                        #print(i)
                        count1.append(j1)#将关键字拆成一个个字符，每个字符在句子中都存在，得到这些字符的列表
                kg = ''
                #------部件
                for item in count1:
                    kg=kg+str(item)
                #print(kg)
                # if len(kg)==0:
                #     print('-1')
                s1 = juzi.find(kg)
                # print(count1)



            # print(s1)

            #-----部件
            if s1!=-1:
                s1=s1
            else:
                if kg.islower() or kg.isupper():#筛选出带英文的
                    kg = ''.join(re.findall(r'[A-Za-z]', kg))
                    s1 = juzi.find(kg)
                else:
                    s1=99999
                    # res1 = re.search(kg[0],juzi).span()#寻找子串第一个字符在句子中位置
                    # res2 = re.search(kg[1],juzi).span()#寻找子串第二个字符在句子中位置
                    # print(res1,res2,res2[0],res1[0])
                    # res=abs(res2[0]-res1[0])#字串第二个字符是否连着第一个字符
                    # # print(res)
                    # if res!= 1 or res > len(kg) :
                    #     kg=kg[1:len(kg)]
                    #     s1=juzi.find(kg)
                    #print(kg)
                    # err_num += 1
                    # else:
                    #
                    #     s1=res1[0]
                    #     kg=kg[0]+kg[1]
                    #     print(kg)
            #-----一级配件
            if s1_pj!=-1:
                s1_pj=s1_pj
            else:
                if str(kg1_pj).islower() or str(kg1_pj).isupper():#筛选出带英文的
                    kg1_pj = ''.join(re.findall(r'[A-Za-z]', kg1_pj))
                    s1_pj = juzi.find(kg1_pj)
                else:
                    s1_pj=99999
            #print(s1)
            #句子中标注的结束下标
            # print(err_num)
            #``---------部件------------’‘
            e1 = s1 + len(kg)
            # if len(kg) == 0
            if len(kg) == 0 or s1 ==99999:#列表为空表明关键字在句子中没有出现过
                doccano_item1 = {
                    'content': juzi,
                    "result_list": [],
                    'prompt': '部件名称'  # 如果有标签信息，可以将其加入到labels列表中
                }
            else:
                doccano_item1 = {
                    'content': juzi,
                    "result_list": [{"text": name, "start": s1, "end": e1}],
                    'prompt': '部件名称'  # 如果有标签信息，可以将其加入到labels列表中
                }
            #’‘-------------一级配件----------------’‘
            e1_pj = s1_pj + len(kg1_pj)
            if len(kg1_pj) == 0 or s1_pj ==99999:#列表为空表明关键字在句子中没有出现过
                doccano_item2 = {
                    'content': juzi,
                    "result_list": [],
                    'prompt': '一级配件名称'  # 如果有标签信息，可以将其加入到labels列表中
                }
            else:
                doccano_item2 = {
                    'content': juzi,
                    "result_list": [{"text": peijianmc, "start": s1_pj, "end": e1_pj}],
                    'prompt': '一级配件名称'  # 如果有标签信息，可以将其加入到labels列表中
                }
            # doccano_item2 = {
            #     'content': guzhan + chuli,
            #     "result_list": [{"text": peijianmc, "start": 2, "end": 8}],
            #     'prompt': '一级配件名称'  # 如果有标签信息，可以将其加入到labels列表中
            # }

            #-----------部件一级编号
            e1_bj = s1_bj + len(kg1_bj)
            if len(kg1_bj) == 0 or s1_bj == 99999:  # 列表为空表明关键字在句子中没有出现过
                doccano_item3 = {
                    'content': juzi,
                    "result_list": [],
                    'prompt': '部件一级编号'  # 如果有标签信息，可以将其加入到labels列表中
                }
            else:
                doccano_item3 = {
                    'content': juzi,
                    "result_list": [{"text": bujian1, "start": s1_bj, "end": e1_bj}],
                    'prompt': '部件一级编号'  # 如果有标签信息，可以将其加入到labels列表中
                }
            # doccano_item3 = {
            #     'content': guzhan + chuli,
            #     "result_list": [{"text": bujian1, "start": 78, "end": 8}],
            #     'prompt': '部件一级编号'  # 如果有标签信息，可以将其加入到labels列表中
            # }
            #---------二级配件名称
            e2_bj = s2_bj + len(kg2_bj)
            if len(kg2_bj) == 0 or s2_bj == 99999:  # 列表为空表明关键字在句子中没有出现过
                doccano_item4 = {
                    'content': juzi,
                    "result_list": [],
                    'prompt': '部件二级名称'  # 如果有标签信息，可以将其加入到labels列表中
                }
            else:
                doccano_item4 = {
                    'content': juzi,
                    "result_list": [{"text": bujian2, "start": s2_bj, "end": e2_bj}],
                    'prompt': '部件二级名称'  # 如果有标签信息，可以将其加入到labels列表中
                }

            # doccano_item5 = {
            #     'content': guzhan + chuli,
            #     "result_list": [{"text": bujian1, "start": 78, "end": 8}],
            #     'prompt': '配件编号'  # 如果有标签信息，可以将其加入到labels列表中
            # }
            #----------配件编号
            e_bh = s_bh + len(kg_bh)
            if len(kg_bh) == 0 or s_bh == 99999:  # 列表为空表明关键字在句子中没有出现过
                doccano_item5 = {
                    'content': juzi,
                    "result_list": [],
                    'prompt': '配件编号'  # 如果有标签信息，可以将其加入到labels列表中
                }
            else:
                doccano_item5 = {
                    'content': juzi,
                    "result_list": [{"text": peijianbh, "start": s_bh, "end": e_bh}],
                    'prompt': '配件编号'  # 如果有标签信息，可以将其加入到labels列表中
                }
            # doccano_item6 = {
            #     'content': guzhan + chuli,
            #     "result_list": [{"text": gzbiaoqian, "start": 78, "end": 8}],
            #     'prompt': '故障标签'  # 如果有标签信息，可以将其加入到labels列表中
            # }
            e_gz = s_gz + len(kg_gz)
            if len(kg_gz) == 0 or s_gz == 99999:  # 列表为空表明关键字在句子中没有出现过
                doccano_item6 = {
                    'content': juzi,
                    "result_list": [],
                    'prompt': '故障标签'  # 如果有标签信息，可以将其加入到labels列表中
                }
            else:
                doccano_item6 = {
                    'content': juzi,
                    "result_list": [{"text": gzbiaoqian, "start": s_gz, "end": e_gz}],
                    'prompt': '故障标签'  # 如果有标签信息，可以将其加入到labels列表中
                }
            # doccano_item6 = {
            #     'content': guzhan + chuli,
            #     "result_list": [{"text": gzbiaoqian, "start": 78, "end": 8}],
            #     'prompt': '故障标签'  # 如果有标签信息，可以将其加入到labels列表中
            # }

        #print(doccano_item)
            doccano_data1.update(**doccano_item1)
            doccano_data2.update(**doccano_item2)
            doccano_data3.update(**doccano_item3)
            doccano_data4.update(**doccano_item4)
            doccano_data5.update(**doccano_item5)
            doccano_data6.update(**doccano_item6)


            #print(doccano_data)
            f.write(json.dumps(doccano_data1, ensure_ascii=False)+'\n')
            f.write(json.dumps(doccano_data2, ensure_ascii=False) + '\n')
            f.write(json.dumps(doccano_data3, ensure_ascii=False) + '\n')
            f.write(json.dumps(doccano_data4, ensure_ascii=False) + '\n')
            f.write(json.dumps(doccano_data5, ensure_ascii=False) + '\n')
            f.write(json.dumps(doccano_data6, ensure_ascii=False) + '\n')

            # f.write(str(doccano_data1) + '\n')
            # f.write(str(doccano_data2) + '\n')
            # f.write(str(doccano_data3) + '\n')
            # f.write(str(doccano_data4) + '\n')
            # f.write(str(doccano_data5) + '\n')
            # f.write(str(doccano_data6) + '\n')
        #with open(doccano_file, 'w', encoding='utf-8') as f:
        # 将dic dumps json 格式进行写入





    # 将doccano数据保存为JSON格式文件
    # pd.DataFrame(doccano_data).to_json(doccano_file, orient='records', force_ascii=False)


# 示例用法
convert_excel_to_doccano(r'E:\code\1114\data\组合_聚类按比例add未聚类.xlsx', r'E:\code\1114\data\out_组合_聚类按比例add未聚类.txt')




