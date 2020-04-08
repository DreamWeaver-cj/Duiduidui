import numpy as np

def Contrast(path_answer:str,path_result:str):
    answer = np.array(np.genfromtxt(path_answer, delimiter=',', dtype=int))
    result = np.array(np.genfromtxt(path_result, delimiter=',', dtype=int))
    n=len(answer)
