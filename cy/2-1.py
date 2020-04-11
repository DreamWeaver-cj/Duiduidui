# NAME：ChengYu
# DATE：20200407-1
# FUNC：字典查找环全部元素
# QSTN：NULL

import numpy as np
import time

global chain
global nodedic
global node
global cir
global element
global dic
global loop

chain=[]
nodedic={}
cir=[]
element=[]
dic={}
node=np.array([])
loop=[]

#把读取的数据转换成字典邻接表（输入二维列表，输出字典）
def Lst2Dic(lst:[]):
    n = lst.shape[0]
    Dic={}
    for i in range(n):
        if lst[i][0] not in Dic:
            Dic[lst[i][0]] = [lst[i][1]]
        else:
            Dic[lst[i][0]] += [lst[i][1]]
    return Dic

#读取数据（输入读取路径，输出字典）
def READ_DATA(path):
    global dic
    dataset = np.array(np.genfromtxt(path, delimiter=',', dtype=int))
    dic=Lst2Dic(dataset[:, :-1])
    # print(dic)

#下一个元素是什么
def NEXT(ID0):
    global dic
    if not Is_NODE(ID0):
        return dic[ID0][0]
    else:
        # SAVE_NODE(ID0)
        return POP_NODE()

#保存element到全局
def SAVE_ELE(ID):
    global element
    element+=[ID]

#从字典里删除element
def DEL_ELE_frim_DIC(element):
    global dic
    for ID in element:
        if ID in dic:
            del dic[ID]

#判断是否是节点
def Is_NODE(ID):
    global dic
    if len(dic[ID])>1:
        return True
    else:
        return False

#保存节点
def SAVE_NODE(ID):
    global node
    global dic
    node.append([ID])
    node[-1]+=dic[ID]

#弹出尾节点
def POP_NODE():
    global node
    if len(node)!=0:
        DEL_EMPTY_NODE()
    if len(node)!=0:
        return node[-1].pop(-1)
    else:
        return -1

#删除空节点
def DEL_EMPTY_NODE():
    global node
    if len(node)!=0:
        if len(node[-1])==1:
            del node[-1]

#保存链
def SAVE_CHAIN(ID):
    global chain
    chain+=[ID]

#返回父节点
def DEL_CHAIN_To_NODE():
    global chain
    global node
    if len(node)!=0:
        del chain[chain.index(node[-1][0])+1:]

#判断是否是环
def Is_CIR():
    global chain
    if chain[-1] in chain[:-1]:
        return True
    else:
        return False

#判断环是否重复
def Is_REPEAT_CIR(CIR):
    global cir
    if CIR not in cir:
        return False
    else:
        return True

#长度限制
def Length_LIMIT(CIR):
    MIN=2
    MAX=7
    if len(CIR)>MIN and len(CIR)<=MAX:
        return True
    else:
        return False

#保存环
def SAVE_CIR():
    global cir
    global chain
    global loop
    LOOP=chain[chain.index(chain[-1]):-1]
    CIR=set(LOOP)
    if Length_LIMIT(CIR):
        if not Is_REPEAT_CIR(CIR):
            cir.append(CIR)
            loop.append(LOOP)
            SHOW_LOOP()###########################################
    else:
        return

#显示环
def SHOW_LOOP():
    print(len(loop), "|", loop[-1])

#判断是否子树结束
def Is_END(ID):
    global chain
    global dic
    if Is_CIR() or (ID not in dic):
        return True
    else:
        return False

#判断是否是重复元素
def Is_REPEAT_ELE(ID):
    global element
    if ID in element:
        return True
    else:
        return False

#查找链
def FIND_CHAIN(ID):
    global chain
    global element
    SAVE_CHAIN(ID)
    if not Is_REPEAT_ELE(ID):
        SAVE_ELE(ID)
    while not Is_END(ID):
        if Is_NODE(ID):
            SAVE_NODE(ID)
        ID=NEXT(ID)
        SAVE_CHAIN(ID)
        if not Is_REPEAT_ELE(ID):
            SAVE_ELE(ID)

def Is_EMPTY_NODE():
    if len(node)!=0:
        return False
    else:
        return True

# 查找环
def FIND_CIR(ID0):
    global chain
    global node
    global cir
    global dic
    global element
    chain=[]
    node=[]
    element=[]
    if ID0 not in dic :
        return False
    else:
        while True:
            DEL_EMPTY_NODE()
            FIND_CHAIN(ID0)
            if Is_CIR():
                SAVE_CIR()
            DEL_CHAIN_To_NODE()
            ID0=POP_NODE()
            if Is_EMPTY_NODE():
                break
    return True


if __name__=='__main__':
    start1 = time.perf_counter()
    READ_DATA(f"../dataset/test_cy/10.txt")#../dataset/test_cy/6.txt
        # end1 = time.perf_counter()
        # for ID in dic:
        #     print(ID)
        # end2 = time.perf_counter()
        # for ID in dic:
        #     print(ID)
        # end3 = time.perf_counter()
        # print('Time1:', end1 - start1)
        # print('Time2:', end2 - start1)
        # print('Time3:', end3 - start1)

    while len(dic)!=0:
        for ID in dic:
            FIND_CIR(ID)
            DEL_ELE_frim_DIC(element)
            break

    end1 = time.perf_counter()
    print('Time1:', end1 - start1)
















