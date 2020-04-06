# NAME：ChenJing
# DATE：202004041121
# FUNC：查找环
# QSTN：暂无

import numpy as np

'''
# 寻找循环路径
# index 代表流动到第index家公司了，index最大为7，也就是最多流动7家公司
# road 为未添加转账记录的路径
# res 为存储环的集合
# road_end 为未添加转账记录的最后一个记录的ID1

# 输入二维数组
# 输出环的个数，并将环存在txt中
'''


class FindLoop():
    def run(self, ds=np.genfromtxt('../dataset/test_data.txt', delimiter=',', dtype=int)[:, :-1]):
        print('run.')
        self.ds = ds
        res = []  # 代表存所有路径的数组
        road = []
        loop_road = []  # 代表资金流动成环了A->B->C->A,也就是洗钱了

        # 程序从这里开始执行循环，遍历整个数组，如果第二个值的ID1==第一个值的ID2，进入递归函数
        for loop_start in range(ds.shape[0]):
            for loop_second in range(ds.shape[0]):
                if ds[loop_second][0] == ds[loop_start][1]:
                    del road[:]  # 代表资金流动路径，A->B->C公司转账则为[A,B,C]
                    road.append(ds[loop_start][0])
                    road.append(ds[loop_start][1])

                    # print('第一层循环' + str(i), str(j))

                    self.loop(road, res, 3, loop_second)
                    road.pop()
        print('finished.')
        fh = open('../res/result_backtrack04051001.txt', 'a', encoding='utf-8')  # a 是追加的意思
        for i in set(res):
            fh.write(i + '\n')
        fh.close()
        return str(len(set(res)))

    def loop(self, road, res, index, i):
        # 如果路径超过7，不再递归
        if index > 7:
            road.append(-1)
            return

            # 循环查找
        for j in range(self.ds.shape[0]):
            # 如果找到转账的下一家公司
            if self.ds[j][0] == self.ds[i][1] and self.ds[j][0] not in road:
                road.append(self.ds[j][0])

                if self.ds[j][1] == road[0] and len(road) < 8:
                    loop_road = road
                    while loop_road[0] != min(loop_road):
                        loop_road.insert(0, loop_road[-1])
                        loop_road.pop()

                    res.append(','.join(str(num) for num in loop_road))
                    return

                # 继续寻找钱款流向的下一家公司
                self.loop(road, res, index + 1, j)
                road.pop()


if __name__ == '__main__':
    obj = FindLoop()
    obj.run()
