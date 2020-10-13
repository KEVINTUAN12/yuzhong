#计算遗传力
import cal_her_para
import numpy as np
import xlrd
from load_profile import load_profile
from time import time
# def her_bw(n,file):
#     avg_bw = cal_her_para.cal_her_gene(file)[3] * cal_her_para.cal_her_bw(n, file)[0] +cal_her_para.cal_her_gene(file)[4] * cal_her_para.cal_her_bw(n,file)[1] +cal_her_para.cal_her_gene(file)[5] * cal_her_para.cal_her_bw(n,file)[2]
#     #体重性状遗传方差
#     vg_bw = cal_her_para.cal_her_gene(file)[3] * np.square(cal_her_para.cal_her_bw(n, file)[0]-avg_bw) + cal_her_para.cal_her_gene(file)[4] * np.square(cal_her_para.cal_her_bw(n,file)[1]-avg_bw) + cal_her_para.cal_her_gene(file)[5] * np.square(cal_her_para.cal_her_bw(n,file)[2]-avg_bw)
#     #体重性状加性方差
#     ve_bw = cal_her_para.cal_her_gene(file)[6] * np.square(cal_her_para.avg_effect_bw(n, file)[0]-avg_bw) + cal_her_para.cal_her_gene(file)[7] * np.square(cal_her_para.avg_effect_bw(n,file)[1] - avg_bw)
#     her_bw = round(vg_bw/(vg_bw+ve_bw), 4)
#     #print(her_bw)
#     return her_bw

def her_bw(n,file):
    aa = cal_her_para.cal_her_gene(file)[3]
    ab = cal_her_para.cal_her_gene(file)[4]
    bb = cal_her_para.cal_her_gene(file)[5]
    fre_a = cal_her_para.cal_her_gene(file)[6]
    fre_b = cal_her_para.cal_her_gene(file)[7]
    avg_aa = cal_her_para.cal_her_bw(n, file)[0]
    avg_ab = cal_her_para.cal_her_bw(n, file)[1]
    avg_bb = cal_her_para.cal_her_bw(n, file)[2]
    A_avg_effect = cal_her_para.avg_effect_bw(n, file)[0]
    B_avg_effect = cal_her_para.avg_effect_bw(n, file)[1]

    avg_bw = aa * avg_aa +ab * avg_ab + bb * avg_bb
    #体重性状遗传方差
    vg_bw = aa * np.square(avg_aa-avg_bw) + ab * np.square(avg_ab-avg_bw) + bb * np.square(avg_bb-avg_bw)
    #体重性状加性方差
    ve_bw = fre_a * np.square(A_avg_effect-avg_bw) + fre_b * np.square(B_avg_effect - avg_bw)
    her_bw = round(vg_bw/(vg_bw+ve_bw), 4)
    #print(her_bw)
    return her_bw
def her(file):
    start = load_profile()[0]
    end = load_profile()[1]
    lst = []
    for i in range(end - start +1):

        lst.append(her_bw(start + i, file))
        #print(her_bw(start + i, file))
    return lst
# start = time()
# print(her("breeding.xlsx"))
# end = time()
# print(end - start)