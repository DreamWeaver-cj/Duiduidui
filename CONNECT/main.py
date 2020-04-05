import cy
import Global
import time

if __name__=='__main__':
    start1 = time.perf_counter()
    ########################################################################
    # FUN:提取网络保存成文件
    # COPYRIGHT@CY
    ########################################################################
    Global.dic = cy.READ_DATA(".//ds//test_data.txt")# 读取文件保存成字典

    while (len(Global.dic) != 0):
        for ID in Global.dic:
            net,eye=cy.FIND_NET(Global.dic,ID)
            if (len(net)!=1):
                print(eye,'|',net)
                cy.WRITE_TXT(net,'res_cy.txt')

            break
    #########################################################################
    # FUN:
    # COPYRIGHT@
    #########################################################################



    end1 = time.perf_counter()
    print("final is in : %s Seconds " % (end1 - start1))