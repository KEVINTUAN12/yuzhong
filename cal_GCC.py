import xlrd
import inspect
import numpy as np
from load_profile import load_profile
from math import factorial
# file = "breeding.xlsx"
# f1 = xlrd.open_workbook(file)
# sheet1 = f1.sheet_by_name('Sheet1')
# #确定重复r和品种n的值
# r = 0
# r_list = []#厂
# n = 0
# n_list = []#公牛
def get_variable_name(variable):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is variable]


#获取场数和种牛数（父辈公牛数）
# for i in range(1,sheet1.nrows):
#     if sheet1.cell_value(i, 4) not in n_list:
#         n_list.append(sheet1.cell_value(i, 4))
#     if sheet1.cell_value(i, 6) not in r_list:
#         r_list.append(sheet1.cell_value(i, 6))
# r = len(r_list)
# n = len(n_list)

def GCC_bw_para(index,file):
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    # 确定重复r和品种n的值
    r = 0
    r_list = []  # 厂
    n = 0
    n_list = []  # 公牛
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i, 4) not in n_list:
            n_list.append(sheet1.cell_value(i, 4))
        if sheet1.cell_value(i, 6) not in r_list:
            r_list.append(sheet1.cell_value(i, 6))
    r = len(r_list)
    n = len(n_list)

    prepare1 = locals()
    prepare2 = locals()
    #生成变量
    for i in range(r):
        for j in range(n):
            prepare1['r' + str(i) + 'n' + str(j)] = 0
            prepare2["count" + str(i) + str(j)] = 0
    #输出变量
    # for i in range(r):
    #     for j in range(n):
    #         print("r{a}n{b} = {value}".format(a = str(i),b = str(j),value = prepare1.get("r" + str(i) + "n" +str(j))))
    #         print("count{a}{b} = {value}".format(a = str(i),b=str(j),value = prepare2.get("count" + str(i) + str(j))))
    for k in range(1, sheet1.nrows):
        for i in range(r):#r 厂
            for j in range(n):#n 牛

                if sheet1.cell_value(k, 4) == n_list[j]:#牛0

                    if sheet1.cell_value(k, 6) == r_list[i]:#牛0厂0
                        prepare1["r" + str(i) + 'n' + str(j)] += sheet1.cell_value(k, index)
                        prepare2["count" + str(i) + str(j)] += 1
    C = 0
    for i in range(r):
        for j in range(n):
            C += prepare1["r" + str(i) + 'n' + str(j)] / prepare2["count" + str(i) + str(j)]
    C = np.square(C)

    #para2 = (np.square(r0n0 / count00) + np.square(r0n1 / count01) + np.square(r1n0 / count10) + np.square(r1n1 / count11)) - C
    para2 = 0
    for i in range(r):
        for j in range(n):
            para2 += np.square(prepare1["r" + str(i) + 'n' + str(j)] / prepare2["count" + str(i) + str(j)])
    #para3 = ((np.square((r0n0 / count00) + (r1n0 / count10)) + np.square((r0n1 / count01) + (r1n1 / count11))) / r) - C
    para3 = 0
    for i in range(n):
        temp = 0
        for j in range(r):
            temp += prepare1["r" + str(j) + 'n' + str(i)] / prepare2["count" + str(j) + str(i)]
        para3 += np.square(temp)
    para3 = para3 / r - C
    #para4 = ((np.square((r0n1 / count01) + (r0n0 / count00)) + np.square((r1n0 / count10) + (r1n1 / count11))) / n) - C
    para4 = 0
    for i in range(r):
        temp = 0
        for j in range(n):
            temp += prepare1["r" + str(i) + 'n' + str(j)] / prepare2["count" + str(i) + str(j)]
        para4 += np.square(temp)
    para4 = para4 / n - C
    para5 = para2 - para3 - para4
    return round(para3 / (n - 1), 2), round(para4 / (r - 1), 2), round(para5 / ((r - 1) * (n - 1)), 2)#,num_list,count_list

def GCC_bw_hg_cov_para(index1,index2,file):
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    # 确定重复r和品种n的值
    r = 0
    r_list = []  # 厂
    n = 0
    n_list = []  # 公牛
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i, 4) not in n_list:
            n_list.append(sheet1.cell_value(i, 4))
        if sheet1.cell_value(i, 6) not in r_list:
            r_list.append(sheet1.cell_value(i, 6))
    r = len(r_list)
    n = len(n_list)
    #生成bw参数rinj_bw和countij
    prepare1 = locals()
    prepare2 = locals()
    prepare3 = locals()
    # 生成变量
    for i in range(r):
        for j in range(n):
            prepare1['r' + str(i) + 'n' + str(j) + "_bw"] = 0
            prepare2["count" + str(i) + str(j)] = 0
            prepare3['r' + str(i) + 'n' + str(j) + "_hg"] = 0
    # 输出变量
    # for i in range(r):
    #     for j in range(n):
    #         print("r{a}n{b}_bw = {value}".format(a = str(i),b = str(j),value = prepare1.get("r" + str(i) + "n" +str(j) + "_bw")))
    #         print("r{a}n{b}_hg = {value}".format(a=str(i), b=str(j), value=prepare3.get("r" + str(i) + "n" + str(j) + "_hg")))
    #         print("count{a}{b} = {value}".format(a = str(i),b=str(j),value = prepare2.get("count" + str(i) + str(j))))
    #给rinj_bw countij rinj_hg赋值
    for i in range(1,sheet1.nrows):#数据的行
        for j in range(n):#牛
            for k in range(r):#厂
                if sheet1.cell_value(i, 4) == n_list[j]:  # 牛0
                      if sheet1.cell_value(i, 6) == r_list[k]:#牛0厂0
                          prepare1["r" + str(k) + "n" + str(j) + "_bw"]+= sheet1.cell_value(i, index1)
                          prepare2["count" + str(k) + str(j)] += 1
                          prepare3["r" + str(k) + "n" + str(j) + "_hg"]+= sheet1.cell_value(i, index2)
    #计算C
    C_bw = 0
    C_hg = 0
    for i in range(r):
        for j in range(n):
            C_bw = prepare1["r" + str(i) + "n" + str(j) + "_bw"] / prepare2["count" + str(i) + str(j)]
    for i in range(r):
        for j in range(n):
            C_hg = prepare3["r" + str(i) + "n" + str(j) + "_hg"] / prepare2["count" + str(i) + str(j)]
    C = C_bw * C_hg /(r * n)
    #print("C = ",C)
    #参数2（总乘积和）
    #para2 = (((r0n0_bw / count00) * (r0n0_hg / count00)) + ((r1n0_bw / count10) * (r1n0_hg / count10)) + ((r0n1_bw / count01) * (r0n1_hg / count01)) + ((r1n1_bw / count11) * (r1n1_hg / count11))) - C
    para2 = 0
    for i in range(n):#牛
        for j in range(r):#厂
            para2 += (prepare1["r" + str(j)+ "n" + str(i) + "_bw"] / prepare2["count" + str(j) + str(i)]) * (prepare3["r" + str(j) + "n" + str(i) + "_hg"] / prepare2["count" + str(j) + str(i)])
    para2 = para2 - C
    #参数3（品种间乘积和）
    para3 = 0
    for i in range(n):#牛
        temp1 = 0
        temp2 = 0
        for j in range(r):#厂
            temp1 += prepare1["r" + str(j)+ "n" + str(i) + "_bw"] / prepare2["count" + str(j) + str(i)]
            temp2 += prepare3["r" + str(j)+ "n" + str(i) + "_hg"] / prepare2["count" + str(j) + str(i)]
        para3 += temp1 * temp2
    para3 = (para3 / r) - C
    #参数4（重复乘积和）
    para4 = 0
    for i in range(r):
        temp1 = 0
        temp2 = 0
        for j in range(n):
            temp1 += prepare1["r" + str(i)+ "n" + str(j) + "_bw"] / prepare2["count" + str(i) + str(j)]
            temp2 += prepare3["r" + str(i)+ "n" + str(j) + "_hg"] / prepare2["count" + str(i) + str(j)]
        para3 += temp1 * temp2
    para4 = (para4 / n) - C
    #参数5（机误乘积和）
    para5 = para2 - para3 - para4
    #各项协方差（品种间协方差0，重复间协方差1，机误协方差2）
    return round(para3 / (n - 1), 2), round(para4 / (r - 1), 2), round(para5 / ((r - 1) * (n - 1)), 2)

def gcc(file):
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    start = load_profile()[0]
    end = load_profile()[1]
    lst = []
    index_pare = []
    for j in range(start,end):
        for k in range(j+1, end + 1):
            lst.append(round((GCC_bw_hg_cov_para(j,k,file)[0] - GCC_bw_hg_cov_para(j,k,file)[2]) / np.sqrt((GCC_bw_para(j,file)[0] - GCC_bw_para(j,file)[2]) * (GCC_bw_para(k,file)[0] - GCC_bw_para(k,file)[2])),4))
            #print((GCC_bw_hg_cov_para(j,k,file)[0] - GCC_bw_hg_cov_para(j,k,file)[2]) / np.sqrt((GCC_bw_para(j,file)[0] - GCC_bw_para(j,file)[2]) * (GCC_bw_para(k,file)[0] - GCC_bw_para(k,file)[2])))
            para1 = sheet1.cell_value(0, j)
            para2 = sheet1.cell_value(0, k)
            index_pare.append([para1, para2])
    return lst, index_pare
#print(gcc("breeding.xlsx"))