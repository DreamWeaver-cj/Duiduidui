import numpy as np

#列表转字典(lst:被转换数据，dic:输出字典，n:数据总行数)
def Lst2Dic(lst:[],dic:{},n:int):
    for i in range(n):
        if lst[i][0] not in dic:
            dic[lst[i][0]] = [lst[i][1]]
        else:
            dic[lst[i][0]] += [lst[i][1]]


#查找链(dic:要查找的字典,ID:查找字典中的ID，tmp:传入一个空列表贮存链)
def Find_chain(dic:{},ID:int,tmp:[]):
    n=len(dic[ID])#ID1发送的用户有多少
    for ID0 in dic[ID]:#遍历ID1发送的用户
        if ID0 in dic:#如果此用户作为发送人在字典中存在
            tmp+=[ID0]#把输入的文件
            if ID0 == tmp[0] and len(tmp)!=1:#如果~（链没闭合或者只有一个元素）
                return tmp
            Find_chain(dic,ID0,tmp)#递归

    return tmp[:-1]#最后一个打印重了


if __name__=='__main__':
    dic = {}  # 存储字典（ID1:ID2）
    crash = []  # 碰撞[ID2,ID3,ID4]（一个ID对多个ID）
    tmp = []  # 存储链（链：结果的一条）

    # 读取文件保存成数组
    dataset = np.array(np.genfromtxt('test_data.txt', delimiter=',', dtype=int))

    print(dataset.shape)
    ##############
    # 测试用例
    ds = np.array([[1, 3],
                   [1, 4],
                   [5, 6],
                   [4, 5],
                   [6, 1],
                   [5, 7]])
    # ds=dataset

    print(ds[:, 0])
    #############
    n = ds.shape[0]#这里就尝试了第一个元素，应该遍历一下还是什么策略没想好
    Lst2Dic(ds,dic,n)#把列表转化成字典
    print(dic)#就这样格式
    tmp=Find_chain(dic,1,tmp)#查找链
    print(tmp)#打印链


