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

def loop(road, res, index, node, dic):
    # 如果路径超过7，不再递归
    if index > 7:
        return

        # 循环查找
    if node in dic:
        for sub_node in dic[node]:
            if sub_node in road:
                if sub_node == road[0] and index == 2:
                    continue
                elif sub_node == road[0] and index != 2:
                    loop_road = road[:]
                    while loop_road[0] != min(loop_road):
                        loop_road.insert(0, loop_road[-1])
                        loop_road.pop()

                    res.append(','.join(str(num) for num in loop_road))
                    continue
                else:
                    # road.pop()
                    continue
            else:
                road.append(sub_node)
                # append_flag[index + 1] = True
                loop(road, res, index + 1, sub_node, dic)
                # if append_flag[index + 1]:
                road.pop()
                #    append_flag[index + 1] = False

    else:
        return


# 输入：储存数据的二维np.array
# 输出：多个环的长度，多个环组成的数组array
def main(path='../dataset/test_data.txt'):
    print('start...')
    # 代表存所有路径的数组
    dic = read_data.read_data(path)
    res = []
    road = []  # 代表资金流动路径，A->B->C公司转账则为[A,B,C]
    # append_flag = [False] * 9
    # 程序从这里开始执行，遍历整个数组，如果第二个值的ID1==第一个值的ID2，进入递归函数
    for key, index in enumerate(dic):

        del road[:]
        road.append(index)
        for node in dic[index]:
            road.append(node)
            loop(road, res, 2, node, dic)
            road.pop()
        road.pop()
    return len(set(res)), set(res)


if __name__ == '__main__':
    l_time = time.time()
    a, b = main(path=f'../dataset/test_data.txt')
    print(a)
    print(b)
    print('总运行时长是：'+str(time.time() - l_time))
