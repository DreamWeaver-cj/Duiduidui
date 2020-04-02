# NAME：ChengYu
# DATE：20200402-2
# FUNC：字典查找网络全部元素
# QSTN：网络个数不能过大，否则会爆内存；
#       只能大致过滤网孔，网眼计算只是估算，可能会有多余的线（只多不少，少的情况还没出现过）

import numpy as np
import time


#列表转字典(lst:被转换数据，dic:输出字典，n:数据总行数)
def Lst2Dic(lst:[]):
    dic={}
    n = ds.shape[0]
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



if __name__=='__main__':

    start1 = time.perf_counter()


    dic = {}  # 存储字典（ID1:[ID2]）
    Find = []#保存各个网络的和用于判定是否查找过
    aaa=0#求网眼的和
    # 读取文件保存成数组
    dataset = np.array(np.genfromtxt('test_data0.txt', delimiter=',', dtype=int))
    ds = dataset[:, :-1]
    ##############
    # 测试用例
    # ds = np.array([[17,18],
    #               [18,5],
    #               [5,4],
    #               [5,6],
    #               [5,7],
    #                [8,5],
    #                [9,8],
    #                [7,1],
    #                [4,3],
    #                [1,9],
    #                [2,1],
    #                [3,2],
    #                [1,15],
    #                [3,55],
    #                [55,10],
    #                [10,11],
    #                [6,44],
    #                [44,2],
    #                [12,10],
    #                [11,12]])
    #
    # ds=np.array([[1,2],
    #              [2,3],
    #              [3,6],
    #              [3,4],
    #              [4,5],
    #              [5,3],
    #              [6,7],
    #              [7,8],
    #              [8,6]])
    #
    # ds = np.array([[1, 2],
    #                [2, 3],
    #                [9, 1],
    #                [3, 4],
    #                [4, 1],
    #                [4, 6],
    #                [6, 7],
    #                [7, 8],
    #                [8, 10]])
    #
    # ds = np.array([[1, 2],
    #                [2, 3],
    #                [3, 4],
    #                [4, 5],
    #                [5, 6],
    #                [6, 7],
    #                [7, 8],
    #                [8, 9],
    #                [9,10],
    #                [8,11],
    #                [10,7]])

    # ds = np.array([[1, 2],
    #                [2, 3],
    #                [3, 4],
    #                [4, 1],
    #                [2, 5],
    #                [5, 6],
    #                [6, 1],
    #                [7, 3],
    #                [8, 7],
    #                [4, 8]])

    # ds = np.array([[1, 2],
    #                [2, 3],
    #                [3,4],
    #                [4,5],
    #                [7,3],
    #                [3,6],
    #                [6,7],
    #                [5,8],
    #                [8,9],
    #                [9,5],
    #                [5,1],
    #                [1,10],
    #                [10,11],
    #                [11,1],
    #                [2,50],
    #                [50,51],
    #                [51,12],
    #                [12,13],
    #                [13,14],
    #                [14,12]])


    #############

    dic=Lst2Dic(ds)#把列表转化成字典
    # print(dic)#就这样格式

    # net, flag = Find_Net(dic, 2250)  # 查找链
    # print(net, '|', flag)  # 打印网

    for i in dic:
        net,eye=Find_Net(dic,i)#查找链
        if not IsIllegal(net,Find,eye):#如果合法
            Find+=Net_Sum(net)#查找是否查找过这个网
            aaa+=eye#网眼求和
            print(eye,net)  # 打印网
        else:
            continue
    print('eye=',aaa)


    end1 = time.perf_counter()

    print("final is in : %s Seconds " % (end1 - start1))




