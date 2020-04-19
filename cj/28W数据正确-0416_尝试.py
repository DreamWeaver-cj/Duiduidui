# NAME：CJ
# DATE：202004061210
# FUNC：查找环子程序


import time
import read_data
import lyx


# 寻找循环路径
# index 代表流动到第index家公司了，index最大为7，也就是最多流动7家公司
# road 为未添加转账记录的路径
# res 为存储环的集合
# node 为未添加转账记录的最后一个记录的ID1
# loop_road  # 代表资金流动成环了A->B->C->A,也就是洗钱了

class Cycle:
    def __init__(self):
        self.marked = set()
        self.on_stack = set()
        self.dic = {}
        self.cycle = []
        self.road = {}

    # 输入：储存数据的二维np.array
    # 输出：多个环的长度，多个环组成的数组array
    def main(self, path='../dataset/test_data.txt'):
        print('start...')
        # 代表存所有路径的数组
        self.dic = read_data.read_data(path)

        for v in self.dic:
            if v not in self.marked:
                self.dfs(self.dic, v)

    def dfs(self, dic, v):
        self.on_stack.add(v)
        self.marked.add(v)
        if v not in dic:
            return
        for w in self.dic[v]:
            if self.cycle:
                return
            if w not in self.marked:
                self.road[w] = v
                self.dfs(dic, w)
            elif w in self.on_stack:
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.road[x]
                self.cycle.append(w)
                self.cycle.append(v)
            print(self.cycle)
            self.cycle.clear()
        self.on_stack.remove(v)


if __name__ == '__main__':
    l_time = time.time()
    ob = Cycle()
    ob.main()
    print('总运行时长是：'+str(time.time() - l_time))
