import numpy as np
import own


# 把读取的数据转换成字典邻接表（输入二维列表，输出字典）
def list_dic(lst: []):
    n = lst.shape[0]
    dic = {}
    for i in range(n):
        if lst[i][0] not in dic:
            dic[lst[i][0]] = [lst[i][1]]
        else:
            dic[lst[i][0]] += [lst[i][1]]
    return dic


# 读取数据（输入读取路径，输出字典）
@own.run_time
def read_data(path='../dataset/test_data.txt'):
    dataset = np.array(np.genfromtxt(path, delimiter=',', dtype=int))
    dic = list_dic(dataset[:, :-1])
    return dic


if __name__ == '__main__':
    res = read_data(path='../dataset/28w/test_data.txt')
    print(res)
    print(res[0])
    print(len(res))
