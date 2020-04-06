import cy
import Global
import time
import FindLoop0406 as cj
import numpy as np


# COPYRIGHT@Duiduidui
# UPDATE@20200405

if __name__=='__main__':

    start1 = time.perf_counter()
    ######################################################################################################
    Global.dic = cy.READ_DATA("../dataset/test_data.txt")# 读取文件保存成字典

    while (len(Global.dic) != 0):
        for ID in Global.dic:
            net,eye=cy.FIND_NET(Global.dic,ID)
            if (len(net)!=1):
                print(eye,'|',net)
                NET_ARRAY=np.array(net)

                LEN,CIRCLE=cj.main(ds=NET_ARRAY)
                cy.WRITE_TXT(CIRCLE,"net.txt",'a')
            break
    ######################################################################################################
    end1 = time.perf_counter()
    print("final is in : %s Seconds " % (end1 - start1))