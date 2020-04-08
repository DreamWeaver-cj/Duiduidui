import numpy as np

#列表转字典(lst:被转换数据，dic:输出字典，n:数据总行数)
def Lst2Dic(lst:[],dic:{},n:int):
    for i in range(n):
        if lst[i][0] not in dic:
            dic[lst[i][0]] = [lst[i][1]]
        else:
            dic[lst[i][0]] += [lst[i][1]]


#查找链(dic:要查找的字典,ID:查找字典中的ID，tmp:传入一个含ID的列表贮存链)

def Find_Net(dic:{},ID:int):
    def Find_chain(dic: {}, ID: int, tmp: [], RES: []):
        if (ID in dic):
            n = len(dic[ID])  # ID1发送的用户有多少
            flag = 0  # 循环条件界定标志
            # 递归结束条件：ID不在字典中，链超过7
            for ID0 in dic[ID]:  # 遍历ID1发送的用户
                if len(tmp)-1 <= 8:  # 如果链的长度不超标
                    if ID0 in dic:  # 如果此用户作为发送人在字典中存在
                        if (ID0 in RES):#如果这个链和查找的环闭合了，那么也会生成环
                            RES += tmp#把这个数组接到后面
                            flag += 1
                            tmp = []
                            break
                        else:
                            if (ID0 not in tmp[:-1]):  # 如果没闭合成环
                                tmp += [ID0]  # 存在缓存里
                                drop, tmp, flag = Find_chain(dic, ID0, tmp, RES)  # 递归
                                # RES += drop
                            else:  # 如果闭合成环
                                del tmp[:tmp.index(ID0)]  # 截断环前面的链
                                RES += tmp
                                tmp = []
                                flag += 1
                    else:  # 链断了
                        continue;
                else:  # 超出7个
                    continue;
            if flag == 0:
                return RES, [], flag
            else:
                return RES, tmp, flag  # 最后一个打印重了
        else:
            return RES, [], 0
####################################################
    net,drop,flag=Find_chain(dic, ID, [ID], [])
    return net,flag

if __name__=='__main__':
    dic = {}  # 存储字典（ID1:ID2）
    crash = []  # 碰撞[ID2,ID3,ID4]（一个ID对多个ID）
    tmp = []  # 存储链（链：结果的一条）

    # 读取文件保存成数组
    dataset = np.array(np.genfromtxt("../dataset/test_data.txt", delimiter=',', dtype=int))

    print(dataset.shape)
    ##############
    # 测试用例
    ds = np.array([[17,18],
                  [18,5],
                  [5,4],
                  [5,6],
                  [5,7],
                   [8,5],
                   [9,8],
                   [7,1],
                   [4,3],
                   [1,9],
                   [2,1],
                   [3,2],
                   [1,15],
                   [3,55],
                   [55,10],
                   [10,11],
                   [6,44],
                   [44,2],
                   [12,10],
                   [11,12]])

    # ds=np.array([[1,2],
    #              [2,3],
    #              [3,6],
    #              [3,4],
    #              [4,5],
    #              [5,3],
    #              [6,7],
    #              [7,8],
    #              [8,6]])

    # ds = np.array([[1, 2],
    #                [2, 3],
    #                [9, 1],
    #                [3, 4],
    #                [4, 1],
    #                [4, 6],
    #                [6, 7],
    #                [7, 8],
    #                [8, 10]])

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

    # ds=dataset

    # print(ds[:, 0])
    #############
    n = ds.shape[0]#这里就尝试了第一个元素，应该遍历一下还是什么策略没想好
    Lst2Dic(ds,dic,n)#把列表转化成字典
    print(dic)#就这样格式
    num=5
    net,flag=Find_Net(dic,num)#查找链
    # print(net,'|',flag)#打印链





