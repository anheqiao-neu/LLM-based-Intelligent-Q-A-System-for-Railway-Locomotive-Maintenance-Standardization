# train/val/test = 8/1/1

# encoding: utf-8
import os
import random
import  numpy as np

# def ran_split(full_list, shuffle=False, ratio1=0.6, ratio2=0.2):
#     sublists = []
#     n_total = len(full_list)
#     offset1 = int(n_total * ratio1)
#     offset2 = int(n_total * ratio2) + offset1
#     if n_total == 0 or offset1 < 1:
#         return [], full_list
#     if shuffle:
#         random.shuffle(full_list)  # 打乱排序
#     sublist_1 = full_list[:offset1]#前10%
#     sublist_2 = full_list[offset1:offset2]#前10%-20%
#     sublist_3 = full_list[offset2:]#前20-100%
#     sublists.append(sublist_1)
#     sublists.append(sublist_2)
#     sublists.append(sublist_3)
#     return sublists  # sublists=[sublist_1,sublist_2,sublist_3]
def ran_split(full_list, shuffle=False, ratio1=0.6, ratio2=0.2):
    sublists_1 = []
    sublists_2 = []
    sublists_3 = []
    sublists = []
    indexs_1 = []
    indexs_2 = []
    indexs_3 = []
    indexs = []
    n_total = len(full_list)
    print(full_list[7003])
    index=np.random.permutation(n_total)
    print(index)
    print(index[0])
    print(full_list[index[0]])
    for i in range(n_total):
        if i < n_total*ratio1:
            # print(index[i])
            sublist_1 = full_list[index[i]] # 前10%
            # print(sublist_1)
            indexs_1.append(index[i])
            sublists_1.append(sublist_1)
        if i >n_total * ratio1 and i<n_total*(ratio1+ratio2):
            sublist_2 = full_list[index[i]]  # 前10%
            indexs_2.append(index[i])
            sublists_2.append(sublist_2)
        if i>n_total*(ratio1+ratio2):
            sublist_3 = full_list[index[i]]  # 前10%
            indexs_3.append(index[i])
            sublists_3.append(sublist_3)
    sublists.append(sublists_1)
    sublists.append(sublists_2)
    sublists.append(sublists_3)
    # print(sublists[1])
    # print(len(sublists_1))
    indexs.append(indexs_1)
    indexs.append(indexs_2)
    indexs.append(indexs_3)
    # print(indexs[1])
            #     sublist_2 = full_list[offset1:offset2]#前10%-20%
            #     sublist_3 = full_list[offset2:]#前20-100%
            #     sublists.append(sublist_1)
            #     sublists.append(sublist_2)
            #     sublists.append(sublist_3)

    return sublists,indexs  # sublists=[sublist_1,sublist_2,sublist_3]

def read_file(filepath):
    file_list = []
    with open(filepath, 'r',encoding="utf-8") as fr:
        data = fr.readlines()
        data = ''.join(data).strip('\n').splitlines()
    # ''.join() list转为str
    # s.strip(rm) 删除s中开头结尾处的rm字符
    # .splitlines() 将字符串返回列表
    file_list = data
    return file_list


def write_file(dst1, txt):
    fo = open(dst1, 'w',encoding="utf-8")
    for item in txt:
        fo.write(str(item) + '\n')



if __name__ == "__main__":
    root_path = r'E:\llama2\t'
    from_txt = '视频安防故障_行修更换20240326.json'
    txts = ['train.json', 'val.json', 'test.json']
    from_path = os.path.join(root_path, from_txt)
    indes =['index_train.txt', 'index_val.txt', 'index_test.txt']
    txt_list = read_file(from_path)

    sublists,indexs = ran_split(txt_list, shuffle=True, ratio1=0.8, ratio2=0.1)
    # print(sublists[1])
    # print(indexs[1])
    # 注：生成的sublist数量与txts数量相同
    root_path1 = r'E:\llama2\chatdata\20240326'
    for txt_name,index_name, i in zip(txts,indes, range(len(txts))):
        to_path = os.path.join(root_path1, txt_name)
        write_file(to_path, sublists[i])
        to_path_in = os.path.join(root_path1, index_name)
        write_file(to_path_in, indexs[i])