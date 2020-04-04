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
                if len(tmp)-1 <= 1000:  # 如果链的长度不超标（不起限制作用）
                    if ID0 in dic:  # 如果此用户作为发送人在字典中存在
                        if (ID0 in RES):#如果这个链和查找的环闭合了，那么也会生成环
                            RES += tmp#把这个数组接到后面
                            eye += 1#网孔加一
                            tmp = []#删除tmp保存的环，就是转移到RES里面，然后存新环了
                            break
                        else:
                            if (ID0 not in tmp[:-1]):  # 如果没闭合成环
                                tmp += [ID0]  # 存在缓存里
                                drop, tmp, eye = Find_chain(dic, ID0, tmp, RES,eye)  # 递归
                            else:  # 如果闭合成环
                                del tmp[:tmp.index(ID0)]  # 截断环前面的链
                                RES += tmp #把环存起来
                                tmp = []#删除tmp保存的环，就是转移到RES里面，然后存新环了
                                eye += 1#网孔加一
                    else:  # 链断了
                        continue
                else:  # 超出7个
                    continue
            if eye == 0:
                return RES, [], eye
            else:
                return RES, tmp, eye  # 最后一个打印重了
        else:
            return RES, [], 0
####################################################
    net,drop,flag=Find_chain(dic, ID, [ID], [],0)
    return net,flag

#求网络总和（net:网络）
def Net_Sum(net:[]):
    return [sum(net)]

#判断是否合法（net:网络，find：已经找到的网络和）[P.S.这个判断方式十分粗暴，就是判断网络节点总和相等就判定查找过]
def IsIllegal(net:[],find:[]):
    a=sum(net)
    b=len(net)
    if (a in find) or (b<=2):
        return 1
    else:
        return 0



if __name__=='__main__':

    start1 = time.perf_counter()


    dic = {}  # 存储字典（ID1:[ID2]）
    Find = []#保存各个网络的和用于判定是否查找过
    aaa=0#求网眼的和
    # 读取文件保存成数组
    dataset = np.array(np.genfromtxt('test_data.txt', delimiter=',', dtype=int))
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
    #                [2, 1]])



    #############

    dic=Lst2Dic(ds)#把列表转化成字典
    # print(dic)#就这样格式

    # net, flag = Find_Net(dic, 94)  # 查找链
    # print(net, '|', flag)  # 打印网

    for i in dic:
        net,eye=Find_Net(dic,i)#查找链
        if not IsIllegal(net,Find):#如果合法
            Find+=Net_Sum(net)#查找是否查找过这个网
            aaa+=eye#网眼求和
            print(eye,net)  # 打印网
        else:
            continue
    print(aaa)


    end1 = time.perf_counter()

    print("final is in : %s Seconds " % (end1 - start1))




