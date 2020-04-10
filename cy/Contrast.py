import numpy as np

def Contrast(path_answer:str,path_result:str):
    answer = np.genfromtxt(path_answer, delimiter=',', dtype=int)
    result = np.genfromtxt(path_result, delimiter=',', dtype=int)
    # la=len(answer)
    # lr=len(result)
    # if la!=lr:
    #     print('个数不对')
    # # for i in result:
    print(answer)

if __name__=='__main__':
    # Contrast("../res/result_backtrack04061413.txt","../dataset/result.txt")
    answer = np.genfromtxt('../res/result_backtrack04061413.txt', delimiter=',', dtype=int)
    print (answer)

