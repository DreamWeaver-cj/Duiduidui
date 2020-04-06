# NAME：ChenJing
# DATE：202004041121
# FUNC：查找环
# QSTN：暂无

import numpy as np
import time

dataset = np.genfromtxt('../dataset/test_data.txt', delimiter=',', dtype=int)
ds = dataset[:, :-1]

res = []  # 代表存所有路径的数组
road = []  # 代表资金流动路径，A->B->C公司转账则为[A,B,C]
loop_road = []  # 代表资金流动成环了A->B->C->A,也就是洗钱了


# 寻找循环路径
# index 代表流动到第index家公司了，index最大为7，也就是最多流动7家公司
# road 为未添加转账记录的路径
# res 为存储环的集合
# i 为未添加转账记录的最后一个记录的ID1
def loop(road, res, index, i):
    # 如果路径超过7，不再递归
    if index > 7:
        return

        # 循环查找
    for j in range(ds.shape[0]):
        # 如果找到转账的下一家公司
        if ds[j][0] == ds[i][1] and ds[j][0] not in road:
            # 打印出账公司
            # print(ds[j][0])
            # 打印不包括入账公司的钱款路径
            # print('前路径' + str(road))

            # 打印包括入账公司的钱款路径
            road.append(ds[j][0])
            # print('后路径' + str(road))
            # 如果已经找到循环，证明找到了循环路径，打印并结束

            if ds[j][1] == road[0] and len(road) < 8:
                loop_road = road
                # print('循环路径----------------------------------------')
                # print(loop_road)
                # print(','.join(str(num) for num in loop_road))
                while loop_road[0] != min(loop_road):
                    loop_road.insert(0, loop_road[-1])
                    loop_road.pop()

                res.append(','.join(str(num) for num in loop_road))
                return

            # 继续寻找钱款流向的下一家公司
            loop(road, res, index + 1, j)
            road.pop()


def main():
    print('start...')
    left_time = time.time()
    # 程序从这里开始执行，遍历整个数组，如果第二个值的ID1==第一个值的ID2，进入递归函数
    for loop_start in range(ds.shape[0]):
        for loop_second in range(ds.shape[0]):
            if ds[loop_second][0] == ds[loop_start][1]:
                road = []
                road.append(ds[loop_start][0])
                road.append(ds[loop_start][1])

                # print('第一层循环' + str(i), str(j))

                loop(road, res, 3, loop_second)
                road.pop()
    print('finished.')
    fh = open('result_cj_backtrack04041128.txt', 'w', encoding='utf-8')
    fh.write(str(len(set(res)))+'\n')
    for i in set(res):
        fh.write(i+'\n')
    fh.close()
    print('运行的总时长是：'+str(time.time()-left_time)+'秒')


if __name__ == '__main__':
    main()
