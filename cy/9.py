# NAME：ChengYu
# DATE：20200404-2
# FUNC：字典查找网络全部元素
# QSTN：网络个数不能过大，否则会爆内存；
#       更改了“网”的定义：包含所有互通元素的集合，未检测bug，官方用例pass
#       eye是网眼个数估计值，不准确，但能确定网络是否只有一个环

import numpy as np
import time
import Global

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
    def Find_chain(dic: {}, ID: int):
        if (ID in dic):         #判断传进来的字典里有没有
            n = len(dic[ID])  # ID1发送的用户有多少
            # 递归结束条件：ID不在字典中，链超过7
            for ID0 in dic[ID]:  # 遍历ID1发送的用户
                if len(Global.chain)-1 <= 100:  # 如果链的长度不超标（不起限制作用）
                    if ID0 in dic:  # 如果此用户作为发送人在字典中存在

                        if (ID0 not in Global.chain[:-1] and ID0 not in Global.net):  # 如果没闭合成环
                            Global.chain += [ID0]  # 存在缓存里
                            Find_chain(dic, ID0)  # 递归

                        else: #闭合成环了

                            Global.net += Global.chain  # 把这个数组接到后面
                            Global.eye += 1  # 网孔加一
                            Global.chain = []  # 删除tmp保存的环，就是转移到RES里面，然后存新环了

                    else:  # 链断了
                        continue
                else:  # 超出n个了
                    continue

            if len(Global.chain)!=0:#全遍子树历完了还没有就删除这个父节点
                del Global.chain[-1]
            return

        else:
            return
####################################################

    Global.eye=0
    Global.net=[]
    Global.chain=[]
    Find_chain(dic, ID)
    return Global.net,Global.eye

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

#对接函数（dic:查找的字典,ls：网络列表）
def Connect(dic:{},ls:[]):
    res=[]
    for ID0 in ls:
        for ID1 in dic[ID0]:
            if ID1 in ls:
                res.append([ID0,ID1])
    return res

#网络查找接口函数（dic：查找的字典）
def FIND_NET(dic:{}):
    res=[[]]
    net, eye = Find_Net(dic, ID)  # 查找网
    if len(net) != 0:  # 如果成网络了
        res = Connect(dic, net)
    else:  # 节点没有网络连接
        del dic[ID]  # 删掉节点
    for ID0 in net:  #
        del dic[ID0]

    return res,eye

if __name__=='__main__':

    start1 = time.perf_counter()
    Global.dic = Read_Data(".//ds//test_data.txt")# 读取文件保存成字典

    while (len(Global.dic) != 0):
        for ID in Global.dic:
            net,eye=FIND_NET(Global.dic)
            if (len(net[0])!=0):
                print(eye,net)
            break
    end1 = time.perf_counter()
    print("final is in : %s Seconds " % (end1 - start1))




