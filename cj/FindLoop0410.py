# NAME：CJ
# DATE：202004061210
# FUNC：查找环子程序


import time
import read_data
chain = []


# 寻找循环路径
# index 代表流动到第index家公司了，index最大为7，也就是最多流动7家公司
# road 为未添加转账记录的路径
# res 为存储环的集合
# node 为未添加转账记录的最后一个记录的ID1
# loop_road  # 代表资金流动成环了A->B->C->A,也就是洗钱了
def loop(road, res, index, node, dic, chains,  marked):
    # 如果路径超过7，不再递归
    if index > 7:
        marked.add(road[0])
        print('marked:')
        print(marked)
        # chains.append(road[1:-1])
        return

        # 循环查找
    if node in dic and node not in marked:
        for sub_node in dic[node]:
            if sub_node in road:  # road 长度 = 2时，暂时没考虑
                if index == 2:
                    continue
                if sub_node in road[:index - 2]:
                    loop_road = road[road.index(sub_node):]
                    while loop_road[0] != min(loop_road):
                        loop_road.insert(0, loop_road[-1])
                        loop_road.pop()
                    # print(loop_road)
                    res.append(','.join(str(num) for num in loop_road))
                    continue
                else:
                    # road.pop()
                    continue
            else:
                road.append(sub_node)
                # append_flag[index + 1] = True
                loop(road, res, index + 1, sub_node, dic, chains, marked)
                # if append_flag[index + 1]:
                road.pop()
                marked.add(sub_node)
                #    append_flag[index + 1] = False

    else:
        return 0


# 输入：储存数据的二维np.array
# 输出：多个环的长度，多个环组成的数组array
def main(path='../dataset/28w/test_data.txt'):
    print('start...')
    # 代表存所有路径的数组
    dic = read_data.read_data(path)
    marked = set()
    res = []
    road = []  # 代表资金流动路径，A->B->C公司转账则为[A,B,C]
    chains = []
    dic_del = []  # 要删除的字典的节点暂存在这里
    count = 0  # 记录删除的顶点个数
    gen = 0  # 记录代数
    # 程序从这里开始执行，遍历整个数组，如果第二个值的ID1==第一个值的ID2，进入递归函数

    for key, index in enumerate(dic):
        if index in marked:
            continue
        road.clear()
        road.append(index)
        for node in dic[index]:
            road.append(node)
            loop(road, res, 2, node, dic, chains, marked)
            road.pop()
        road.pop()

        # marked.add(index)
        count += 1
        dic_del = []
        len_dic = len(dic)
        print(len_dic)
        print('key值是：   ' + str(index))
        while chains:
            gen += 1
            # next_loop(chains, dic, res)
            chains2 = chains.copy()
            chains.clear()
            chain_head = []
            for chain in chains2:
                loop(chain, res, 6, chain[-1], dic, chains, marked)
            print('第 {} 代删除了 {} 个节点'.format(gen, count))
            gen = 0
        print('res长度是：  ' + str(len(set(res))))
        len_dic = len(dic)
        print(len_dic)
        print('last_marked')
        print(marked)
    return len(set(res)), set(res)


if __name__ == '__main__':
    l_time = time.time()
    # for i in range(1, 11):
    res_len, res = main(path=f'../dataset/test_cy/10.txt')
    # res_len, res = main(path=f'../dataset/test_data.txt')
    # res_len, res = main(path=f'../dataset/28w/test_data.txt')
    print('res的长度是：')
    print(res_len)
    print('res是：')
    print(res)
    print('总运行时长是：'+str(time.time() - l_time))


