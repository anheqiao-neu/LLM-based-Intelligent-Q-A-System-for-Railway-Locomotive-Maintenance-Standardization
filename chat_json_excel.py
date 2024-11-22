import json
import pandas as pd
# import jsonpath

# obj = json.load(open("test.json","r",encoding="utf-8"))
# obj1=jsonpath.jsonpath(obj,"$..sentence")
file = "tes256-256/generated_predictions.json"
filen = "index_test.txt"
filee = "视频安防故障_行修更换.xlsx"
# df=pd.read_excel('视频安防故障_行修更换.xlsx')
# doccano_data = {}
# for index, row in df.iterrows():
#     year = row['年份']
#     carnum = row['车号']
#     chanjia = row['厂家']
#     time = row['检测时间']
#     clo = row['故障模块']
#     didian = row['检测地点']
#     human = row['检测人']
#     err_time = row['故障报出时间']
#     t_sys = row['子系统']
#     guzhan = row['故障内容']  # 假设文本内容在Excel表格的'text'列中
#     chuli = row['处理方法']
line_11=[]
line_12=[]
line_bujian1_11 = []
line_peijian_11 =[]
line_bujian_1_11 = []
line_bujian_2_11 =[]
line_peijiannum_11 = []
line_error_11=[]

linn=[]

carnum = []
year = []
chanjia = []
time = []
clo = []
didian = []
human = []
err_time = []
t_sys = []
with open(file, 'r', encoding="utf-8") as f:
    for line in f.readlines():
        # print(line)
        line1 = line.split('", "predict"')[0]

        line11 = line1.split(': "')[1]
        # print(line1)
        #故障描述
        line_1 = line11.split('&&')[0]
        line_11.append(line_1)
        # print(line_1)
        #处理办法
        line_2 = line11.split('&&')[1]
        # print(line_2)
        line_12.append(line_2)

        #部件名称
        line_bujian = line.split("']，一级")[0]
        line_bujian1 = line_bujian.split("：['")[1]
        line_bujian1_11.append(line_bujian1)
        # print(line_bujian1)
        #一级配件名称
        line_peijian = line.split("一级配件名称")[1]
        line_peijian = line_peijian.split("['")[1]
        line_peijian = line_peijian.split("']")[0]
        line_peijian_11.append(line_peijian)

        #部件一级编号
        if "部件一级编号" in line:
            line_bujian_1 = line.split("部件一级编号")[1]
            # print(line)
            line_bujian_1 = line_bujian_1.split("['")[1]
            line_bujian_1 = line_bujian_1.split("']")[0]
            line_bujian_1_11.append(line_bujian_1)
        else:
            line_bujian_1="/"
            line_bujian_1_11.append(line_bujian_1)

        #部件二级编号
        if "部件二级编号" in line:
            line_bujian_2 = line.split("部件二级编号")[1]
            line_bujian_2 = line_bujian_2.split("['")[1]
            line_bujian_2 = line_bujian_2.split("']")[0]
            line_bujian_2_11.append(line_bujian_2)
        else:
            line_bujian_2="/"
            line_bujian_2_11.append(line_bujian_2)

        #配件编号
        if "配件编号" in line:
            line_peijiannum = line.split("配件编号")[1]
            line_peijiannum = line_peijiannum.split("['")[1]
            line_peijiannum = line_peijiannum.split("']")[0]
            line_peijiannum_11.append(line_peijiannum)
        else:
            line_peijiannum="/"
            line_peijiannum_11.append(line_peijiannum)

        # 故障标签
        line_error = line.split("故障标签")[1]
        # print(line_error)
        line_error = line_error.split("['")[1]
        line_error = line_error.split("']")[0]
        line_error_11.append(line_error)
        # print(line_error)

    with open(filen, 'r', encoding="utf-8") as fn:
        df = pd.read_excel(filee)
        for linen in fn.readlines():
            linens=linen.replace('\n','')
            # print(type(linens))
            for index, row in df.iterrows():
                if linens==str(index):
                    carnum.append(row['车号'])
                    year.append(row['年份'])
                    chanjia.append(row['厂家'])
                    time.append(row['检测时间'])
                    clo.append(row['故障模块'])
                    didian.append(row['检测地点'])
                    human.append(row['检测人'])
                    err_time.append(row['故障报出时间'])
                    t_sys.append(row['子系统'])
                    #     carnum = row['车号']
                    #     chanjia = row['厂家']
                    #     time = row['检测时间']
                    #     clo = row['故障模块']
                    #     didian = row['检测地点']
                    #     human = row['检测人']
                    #     err_time = row['故障报出时间']
                    #     t_sys = row['子系统']



    wData={
        '车号':carnum,
        '年份':year,
        '厂家':chanjia,
        '检测时间':time,
        '故障模块':clo,
        '故障内容':line_11,
        '处理方法':line_12,
        '检测地点':didian,
        '检测人':human,
        '故障报出时间':err_time,
        '子系统':t_sys,
        '部件名称':line_bujian1_11,
        '一级配件名称':line_peijian_11,
        '部件一级编号':line_bujian_1_11,
        '部件二级编号':line_bujian_2_11,
        '配件编号':line_peijiannum_11,
        '故障标签':line_error_11,
        }

    # print(len(wData['故障内容']))
    # print(len(wData['处理方法']))
    # print(len(wData['部件名称']))
    # print(len(wData['一级配件名称']))
    # print(len(wData['部件一级编号']))
    # print(len(wData['部件二级编号']))
    # print(len(wData['配件编号']))
    # print(len(wData['故障标签']))

    fwrite=pd.DataFrame(wData)
    print(fwrite)
    #
    # fnwrite = pd.DataFrame(wDatan)
    # fend=fnwrite.append(fwrite)
    # print(fend)
    fwrite.to_excel('result.xlsx',index=False)
