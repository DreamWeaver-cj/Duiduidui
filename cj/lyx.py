# NAME：LiYingXian
# DATE：20200406-1
# FUNC：将循环转账路径按顺序保存到文件中
# QSTN：暂无

import Global
import time

res_tmp = [] #

#保存不同长度的环到不同字典中
#没找到一个环就判断环的长度并存入字典中，字典key为环的起始ID，然后value用集合保存，这样可以保证相同的环不会重复出现

def choice(loop_road):

    if len(loop_road) == 3:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in Global.dic3:
            Global.dic3[loop_road[0]] = set(res_tmp)
        else:
            Global.dic3[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

    elif len(loop_road) == 4:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in Global.dic4:
            Global.dic4[loop_road[0]] = set(res_tmp)
        else:
            Global.dic4[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

    elif len(loop_road) == 5:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in Global.dic5:
            Global.dic5[loop_road[0]] = set(res_tmp)
        else:
            Global.dic5[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

    elif len(loop_road) == 6:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in Global.dic6:
            Global.dic6[loop_road[0]] = set(res_tmp)
        else:
            Global.dic6[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

    elif len(loop_road) == 7:
        res_tmp.append(','.join(str(num) for num in loop_road))
        if loop_road[0] not in Global.dic7:
            Global.dic7[loop_road[0]] = set(res_tmp)
        else:
            Global.dic7[loop_road[0]].add(','.join(str(num) for num in loop_road))
        res_tmp.clear()

#保存循环转账路径
#分别对不同长度的字典按key值排序，然后按序保存在文件中


def mysort():
    fh = open('result.txt', 'a', encoding='utf-8')  # a 是追加的意思

    #num = len(Global.dic3) + len(Global.dic4) + len(Global.dic5) + len(Global.dic6) + len(Global.dic7)
    for i in Global.dic3:
        Global.num += len(Global.dic3[i])

    for i in Global.dic4:
        Global.num += len(Global.dic4[i])

    for i in Global.dic5:
        Global.num += len(Global.dic5[i])

    for i in Global.dic6:
        Global.num += len(Global.dic6[i])

    for i in Global.dic7:
        Global.num += len(Global.dic7[i])

    fh.write(str(Global.num) + '\n')

    for i in sorted (Global.dic3):
        for j in Global.dic3[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    for i in sorted(Global.dic4):
        for j in Global.dic4[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    for i in sorted(Global.dic5):
        for j in Global.dic5[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    for i in sorted(Global.dic6):
        for j in Global.dic6[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    for i in sorted(Global.dic7):
        for j in Global.dic7[i]:
            for k in j:
                fh.write(k)
            fh.write('\n')

    fh.close()


if __name__ == '__main__':
    l_time = time.time()
    mysort()
    print('run time is :'+str(time.time()-l_time))