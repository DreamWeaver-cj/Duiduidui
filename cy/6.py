# NAME：ChengYu
# DATE：20200402-2
# FUNC：字典查找网络全部元素
# QSTN：加了记忆节点，结果更慢了

import numpy as np
import time


#列表转字典(lst:被转换数据，dic:输出字典，n:数据总行数)
def Lst2Dic(lst:[]):
    dic={}
    n = lst.shape[0]
    for i in range(n):
        if lst[i][0] not in dic:
            dic[lst[i][0]] = [lst[i][1]]
        else:
            dic[lst[i][0]] += [lst[i][1]]
    return dic

#查找网络（dic：要查找的字典，ID，开始查询的位置）
def Find_Net(dic:{},ID:int):
    # 查找链(dic:要查找的字典,ID:查找字典中的ID，tmp:传入一个含ID的列表贮存链,RES：保存网络用于迭代的传入，eye:网孔数量)
    def Find_chain(dic: {}, ID: int, tmp: [], RES: [], eye: int):
        if (ID in dic):         #判断传进来的字典里有没有
            n = len(dic[ID])  # ID1发送的用户有多少
            # 递归结束条件：ID不在字典中，链超过7
            for ID0 in dic[ID]:  # 遍历ID1发送的用户
                if len(tmp)-1 <= 100:  # 如果链的长度不超标（不起限制作用）
                    if ID0 in dic:  # 如果此用户作为发送人在字典中存在

                        if (ID0 not in tmp[:-1] and ID0 not in RES):  # 如果没闭合成环
                            tmp += [ID0]  # 存在缓存里
                            RES, tmp, eye = Find_chain(dic, ID0, tmp, RES,eye)  # 递归

                        else: #闭合成环了
                            if len(RES) == 0:  # 如果还没找到环
                                del tmp[:tmp.index(ID0)]  # 截断环前面的链

                            RES += tmp  # 把这个数组接到后面
                            eye += 1  # 网孔加一
                            tmp = []  # 删除tmp保存的环，就是转移到RES里面，然后存新环了

                    else:  # 链断了
                        continue
                else:  # 超出n个了
                    continue

            if len(tmp)!=0:#全遍子树历完了还没有就删除这个父节点
                del tmp[-1]
            return RES, tmp, eye

        else:
            return RES, tmp, 0
####################################################
    net,drop,flag=Find_chain(dic, ID, [ID], [],0)
    return net,flag

#求网络总和（net:网络）
def Net_Sum(net:[]):
    return [sum(net)]

#判断是否合法（net:网络，find：已经找到的网络和）[P.S.这个判断方式十分粗暴，就是判断网络节点总和相等就判定查找过]
def IsIllegal(net:[],find:[],eye:int):
    a=sum(net)
    b=len(net)
    if (a in find) or (b<=2) or (eye==1 and b>7) :
        return 1#不合法
    else:
        return 0#合法

#读取数据（path:路径）
def Read_Data(path:str):

    dataset = np.array(np.genfromtxt(path, delimiter=',', dtype=int))
    dic=Lst2Dic(dataset[:, :-1])
    # print(dic)
    return dic

#由于网络相互不接触，删掉也没关系(dic：所有测试数据，net：查找出的网络）
def Delet(dic:{},net:[]):
    for ID in net:
        del dic[ID]
    return dic



if __name__=='__main__':

    start1 = time.perf_counter()

    dic = {}  # 存储字典（ID1:[ID2]）
    Find_sum = []#保存各个网络的和用于判定是否查找过
    Find=[]#保存各个网络的和用于判定是否查找过
    aaa=0#求网眼的和

    dic = Read_Data(".//ds//test_data.txt")# 读取文件保存成字典

    # net, flag = Find_Net(dic, 2250)  # 查找链
    # print(net, '|', flag)  # 打印网

    for ID in dic:
        if ID not in Find:
            net,eye=Find_Net(dic,ID)#查找网

            if not IsIllegal(net,Find_sum,eye):#如果合法
                Find+=net
                Find_sum+=Net_Sum(net)#查找是否查找过这个网
                aaa+=eye#网眼求和
                print(eye,net)  # 打印网
            else:
                continue
            net=[]
        else:
            continue
    print('eye=',aaa)


    end1 = time.perf_counter()

    print("final is in : %s Seconds " % (end1 - start1))




