# NAME：ChenJing
# DATE：202004061210-1
# FUNC：查找环子程序
# QSTN：暂无

import numpy as np
import time

import lyx

# 寻找循环路径
# index 代表流动到第index家公司了，index最大为7，也就是最多流动7家公司
# road 为未添加转账记录的路径
# res 为存储环的集合
# i 为未添加转账记录的最后一个记录的ID1
def loop(road, res, index, i, ds):
    # 如果路径超过7，不再递归
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

                lyx.choice(loop_road)  #将循环路径保存在不同的字典中

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

if __name__ == '__main__':
    a, b = main()
    print(a)
    print(b)

