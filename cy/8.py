# NAME：ChengYu
# DATE：20200404-2
# FUNC：字典查找网络全部元素
# QSTN：理论上应该是bug全没了，查出来的不多不少，不过可能还会有没考虑到的问题，测试都通过了
#         网眼没处理
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
    # 查找链(dic:要查找的字典,ID:查找字典中的ID，tmp:传入一个含ID的列表贮存链,RES：保存网络用于迭代的传入，eye:网孔数量, target:当前网孔)

    def Find(dic: {}, ID: int):
        s = 0
        if (ID in dic):  # 判断传进来的字典里有没有
            # 递归结束条件：ID不在字典中，链超过7
            for ID0 in dic[ID]:  # 遍历ID1发送的用户
                if ID0 in dic:  # 如果此用户作为发送人在字典中存在
                    if len(Global.net) == 0:  # 如果还没找到眼
                        if (ID0 not in Global.chain):  # ID0不在链里
                            Global.chain += [ID0]  # 存在缓存里
                            Find(dic, ID0)  # 递归
                        else:  # 闭合成环了
                            Global.middle.append([])
                            Global.middle[Global.target]=Global.chain[:Global.chain.index(ID0)]
                            del Global.chain[:Global.chain.index(ID0)]  # 截断环前面的链

                            Global.net.append([])
                            Global.net[Global.target] += Global.chain  # 把这个环接到后面
                            Global.eye += 1  # 网孔加一
                            Global.chain = []  # 删除chain保存的链，就是转移到net里面，然后存新链了
                    else:  # 如果已经找到第一个眼了
                        for MID in range(Global.target + 1):
                            if ID0 in Global.middle[MID]:#跟之前的断头接上了

                                for N in range(MID+1,Global.target+1):
                                    Global.net[MID] += Global.middle[N] + Global.net[N]
                                # Global.target += 1
                                Global.net[MID] += Global.chain+Global.middle[MID][Global.middle[MID].index(ID0):]
                                del Global.net[MID+1:]
                                del Global.middle[MID+1:]
                                del Global.middle[MID][Global.middle[MID].index(ID0):]
                                Global.eye += 1  # 网孔加一
                                Global.chain = []
                                Global.target = MID
                                break
                            else:
                                continue
                        for NET in range(Global.target + 1):
                            if (ID0 not in Global.net[NET]):  # ID0不在网络里
                                if NET == Global.target:
                                    if (ID0 not in Global.chain):  # IDO不在链里（没自己闭合成新环,也没和别的网成环）
                                        Global.chain += [ID0]  # 存在缓存里
                                        Find(dic, ID0)  # 递归
                                        break
                                    else:  # 自己闭合成新环的（可能会形成新的网）
                                        Global.target += 1  # 目标网络走完了，下一个网
                                        # if (len(Global.middle)-1)!=Global.target:
                                        Global.middle.append([])  # 另存一个中间链
                                        Global.middle[Global.target] += Global.chain[:Global.chain.index(ID0)]  # 存两个网中间的链
                                        del Global.chain[:Global.chain.index(ID0)]  # 截断环前面的链

                                        Global.net.append([])  # 另存一个网
                                        Global.net[Global.target] += Global.chain  # 把这个环接到后面
                                        Global.chain = []
                                        Global.eye += 1  # 网孔加一
                                        break

                            else:  # 和已知网闭合了
                                if NET == Global.target:  # 和当前网络闭合了
                                    Global.net[Global.target] += Global.chain  # 把这个数组接到后面
                                    Global.eye += 1  # 网孔加一
                                    Global.chain = []  # 删除chain保存的链，就是转移到net里面，然后存新链了
                                    break
                                else:  # 和之前的网络闭合了
                                    for N in range(NET, Global.target):
                                        Global.net[NET] += Global.middle[N+1] + Global.net[N + 1]
                                    Global.net[NET] += Global.chain

                                    del Global.net[NET + 1:Global.target + 1]
                                    del Global.middle[NET+1: Global.target + 1]
                                    Global.chain = []
                                    Global.target = NET
                                    Global.eye += 1  # 网孔加一
                                    break



                else:  # 链断了
                    continue

            if len(Global.chain) != 0:  # 全遍子树历完了还没有就删除这个父节点
                del Global.chain[-1]

            if len(Global.middle) != 0:
                if  (ID in Global.middle[-1]) :
                    s=1
                    if Global.target!=0:
                        del Global.net[Global.target]
                        Global.target-=1


                if (ID in Global.middle[-1]):
                    Global.middle[-1].pop()
                    if len(Global.middle[-1])==0:
                        del Global.middle[-1]
            return
        else:
            return
####################################################
    Global.chain = [ID]
    Global.net = []
    Global.target=0
    Global.middle = []
    Global.eye = 0

    Find(dic, ID)
    if len(Global.net)==0:
        return [],Global.eye
    else:
        return Global.net[0],Global.eye


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
    Find = []#保存各个网络的和用于判定是否查找过
    # test_data.txt
    dic = Read_Data(".//ds//5.txt")# 读取文件保存成字典

    # net,eye=Find_Net(dic, 4)  # 查找链
    # print(net)  # 打印网

    for ID in dic:
        net,eye=Find_Net(dic,ID)#查找链
        # print(ID, net)  # 打印网
        if not IsIllegal(net,Find,eye):#如果合法
            Find+=Net_Sum(net)#查找是否查找过这个网
            print(net)  # 打印网
        else:
            continue


    end1 = time.perf_counter()

    print("final is in : %s Seconds " % (end1 - start1))




