#   DATE:20200408
#   EDTN:1
#

import numpy as np
import time

global eye
global chain
global net
global dic
global NET_ARRAY

global num

global dic3
global dic4
global dic5
global dic6
global dic7

eye=0
chain=[]
net=[]
dic={}
NET_ARRAY=[[]]
num = 0
dic3={}
dic4={}
dic5={}
dic6={}
dic7={}



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
    global eye
    global net
    global chain
    # 查找链(dic:要查找的字典,ID:查找字典中的ID，tmp:传入一个含ID的列表贮存链,RES：保存网络用于迭代的传入，eye:网孔数量)
    def Find_chain(dic: {}, ID: int):
        global eye
        global net
        global chain
        if (ID in dic):         #判断传进来的字典里有没有
            n = len(dic[ID])  # ID1发送的用户有多少
            # 递归结束条件：ID不在字典中，链超过7
            for ID0 in dic[ID]:  # 遍历ID1发送的用户
                if len(chain)-1 <= 100:  # 如果链的长度不超标（不起限制作用）
                    if ID0 in dic:  # 如果此用户作为发送人在字典中存在
                        if (ID0 not in chain[:-1] and ID0 not in net):  # 如果没闭合成环
                            chain += [ID0]  # 存在缓存里
                            Find_chain(dic, ID0)  # 递归

                        else: #闭合成环了

                            net += chain  # 把这个数组接到后面
                            eye += 1  # 网孔加一
                            chain = []  # 删除tmp保存的环，就是转移到RES里面，然后存新环了

                    else:  # 链断了
                        continue
                else:  # 超出n个了
                    continue

            if len(chain)!=0:#全遍子树历完了还没有就删除这个父节点
                del chain[-1]
            return

        else:
            return

    eye=0
    net=[]
    chain=[ID]
    Find_chain(dic, ID)
    return net,eye

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
def READ_DATA(path:str):
    global dic
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
def FIND_NET(dic:{},ID:int):
    res=[[]]
    net, eye = Find_Net(dic, ID)  # 查找网
    if len(net) != 0:  # 如果成网络了
        res = Connect(dic, net)
    else:  # 节点没有网络连接
        del dic[ID]  # 删掉节点
    for ID0 in net:  #删掉网络节点
        del dic[ID0]
    return res,eye

def WRITE_TXT(ls:[[]],path:str,mod:str):
    fh = open(path, mod, encoding='utf-8')
    for STREAM in ls:
        fh.write(str(STREAM[0]) + ',' + str(STREAM[1]) + ',' + '0' + '\n')
    fh.close()

def loop(road, res, index, i, ds):
    # 如果路径超过7，不再递归
    global num
    if index > 7:
        return

        # 循环查找
    for j in range(ds.shape[0]):
        # 如果找到转账的下一家公司
        if ds[j][0] == ds[i][1] and ds[j][0] not in road:
            road.append(ds[j][0])
            if ds[j][1] == road[0] and len(road) < 8:
                loop_road = road

                while loop_road[0] != min(loop_road):
                    loop_road.insert(0, loop_road[-1])
                    loop_road.pop()

                choice(loop_road)  #将循环路径保存在不同的字典中

                res.append(','.join(str(num) for num in loop_road))
                #for num in loop_road:
                    #res.append(num)
                #res.append(loop_road)
                return

            # 继续寻找钱款流向的下一家公司
            loop(road, res, index + 1, j, ds)
            road.pop()

# 输入：储存数据的二维np.array
# 输出：多个环的长度，多个环组成的数组array


def main(ds=np.genfromtxt('../dataset/test_data.txt', delimiter=',', dtype=int)[:, :-1]):
    res = []  # 代表存所有路径的数组
    road = []  # 代表资金流动路径，A->B->C公司转账则为[A,B,C]
    loop_road = []  # 代表资金流动成环了A->B->C->A,也就是洗钱了

    # 程序从这里开始执行，遍历整个数组，如果第二个值的ID1==第一个值的ID2，进入递归函数
    for loop_start in range(ds.shape[0]):
        for loop_second in range(ds.shape[0]):
            if ds[loop_second][0] == ds[loop_start][1]:
                del road[:]
                road.append(ds[loop_start][0])
                road.append(ds[loop_start][1])

                loop(road, res, 3, loop_second, ds)
                road.pop()

    return len(set(res)), set(res)


res_tmp = [] #

#保存不同长度的环到不同字典中
#没找到一个环就判断环的长度并存入字典中，字典key为环的起始ID，然后value用集合保存，这样可以保证相同的环不会重复出现

def choice(loop_road):
    global num
    global dic3
    global dic4
    global dic5
    global dic6
    global dic7
    if len(loop_road) == 3:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in dic3:
            dic3[loop_road[0]] = set(res_tmp)
        else:
            dic3[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

    elif len(loop_road) == 4:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in dic4:
            dic4[loop_road[0]] = set(res_tmp)
        else:
            dic4[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

    elif len(loop_road) == 5:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in dic5:
            dic5[loop_road[0]] = set(res_tmp)
        else:
            dic5[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

    elif len(loop_road) == 6:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in dic6:
            dic6[loop_road[0]] = set(res_tmp)
        else:
            dic6[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

    elif len(loop_road) == 7:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in dic7:
            dic7[loop_road[0]] = set(res_tmp)
        else:
            dic7[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

#保存循环转账路径
#分别对不同长度的字典按key值排序，然后按序保存在文件中

def mysort():
    global dic3
    global dic4
    global dic5
    global dic6
    global dic7
    global num

    fh = open('../res/result_backtrack04061413.txt', 'a', encoding='utf-8')  # a 是追加的意思

    #num = len(dic3) + len(dic4) + len(dic5) + len(dic6) + len(dic7)
    for i in dic3:
        num += len(dic3[i])

    for i in dic4:
        num += len(dic4[i])

    for i in dic5:
        num += len(dic5[i])

    for i in dic6:
        num += len(dic6[i])

    for i in dic7:
        num += len(dic7[i])

    fh.write(str(num) + '\n')

    for i in sorted (dic3):
        for j in dic3[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    for i in sorted(dic4):
        for j in dic4[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    for i in sorted(dic5):
        for j in dic5[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    for i in sorted(dic6):
        for j in dic6[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    for i in sorted(dic7):
        for j in dic7[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    fh.close()


if __name__=='__main__':

    start1 = time.perf_counter()
    ######################################################################################################
    dic = READ_DATA("../dataset/test_data.txt")# 读取文件保存成字典
    while (len(dic) != 0):
        for ID in dic:
            net,eye=FIND_NET(dic,ID)
            if (len(net)!=1):
                NET_ARRAY=np.array(net)
                LEN,CIRCLE=main(ds=NET_ARRAY)
            break

    mysort()  #对循环路径排序并保存到文件
    ######################################################################################################
    end1 = time.perf_counter()
    print("final is in : %s Seconds " % (end1 - start1))


