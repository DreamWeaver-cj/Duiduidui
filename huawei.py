import numpy as np

dataset = np.genfromtxt('test_data.txt', delimiter=',', dtype=int)
dataset.shape

# ds = dataset[:10]
ds = dataset[:, :-1]
ds


# ds = np.array([[1, 2],
#                [1, 4],
#                [2, 3],
#                [3, 4],
#                [4, 5],
#                [4, 8],
#                [5, 6],
#                [6, 7],
#                [7, 8],
#                [8, 1]
#                ])
res = []  # 代表存所有路径的数组
road = []  # 代表资金流动路径，A->B->C公司转账则为[A,B,C]
loop_road = []  # 代表资金流动成环了A->B->C->A,也就是洗钱了


# 寻找循环路径
# index 代表流动到第index家公司了，index最大为7，也就是最多流动7家公司
def loop(road, res, index, i):
    # 如果路径超过7，不再递归
    if index > 6:
        return

        # 循环查找
    for j in range(i + 1, ds.shape[0]):

        # ，如果找到转账的下一家公司
        if ds[j][0] == ds[i][1]:
            # 打印出账公司
            # print(ds[j][0])
            # 打印不包括入账公司的钱款路径
            # print('前路径' + str(road))

            # 打印包括入账公司的钱款路径
            road.append(ds[j][0])
            # print('后路径' + str(road))
            # 如果已经找到循环，证明找到了循环路径，打印并结束
            if ds[j][1] in road:
                loop_road = road
                # print('循环路径----------------------------------------')
                # print(loop_road)
                # print(','.join(str(num) for num in loop_road))
                res.append(','.join(str(num) for num in loop_road))
                return

            # 继续寻找钱款流向的下一家公司
            loop(road, res, index + 1, j)
            road.pop()


# 程序从这里开始执行，遍历整个数组，如果第二个值的ID1==第一个值的ID2，进入递归函数
for i in range(ds.shape[0]):
    for j in range(i, ds.shape[0] - 1):
        if (ds[j][0] == ds[i][1]):
            road = []
            road.append(ds[i][0])
            road.append(ds[i][1])

            # print('第一层循环' + str(i), str(j))

            loop(road, res, 2, j)
print(len(res))
print(res)


fh = open('result_cj.txt', 'w', encoding='utf-8')
fh.write(str(len(res))+'\n')
for i in range(len(res)):
    print(res[i])
    fh.write(res[i]+'\n')
fh.close()


