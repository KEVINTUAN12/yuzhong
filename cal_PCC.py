# 遗传相关系数（Genetic correlation coefficient）
# 表型相关系数（Phenotypic correlation coefficient）
# 体重bw、体高hg、体长bl、胸围cw、眼肌面积ema 4+3+2+1
# ***性状个数写死问题，性状数量，性状位置（在excel表格中）***
import numpy as np
import pandas as pd
import xlrd
from load_profile import load_profile
import inspect
def get_variable_name(variable):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is variable]

start = load_profile()[0]
end = load_profile()[1]
def cal_pcc_bw_hg(index1,index2,file):
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    sum_xy = 0

    sum_x = 0
    sum_y = 0
    square_sum_x = 0
    square_sum_y = 0
    for i in range(1, sheet1.nrows):
        sum_xy += (sheet1.cell_value(i,index1) * sheet1.cell_value(i,index2))
        sum_x += sheet1.cell_value(i,index1)
        square_sum_x += np.square(sheet1.cell_value(i,index1))
        sum_y += sheet1.cell_value(i,index2)
        square_sum_y += np.square(sheet1.cell_value(i,index2))
    sum_x_sum_y = (sum_x * sum_y) / sheet1.nrows
    prepare = locals()
    for i in range(end - start + 1):#五种性状的均值和标准差
        prepare["avg" + str(i)] = 0
        prepare["stdev" + str(i)] = []

    for i in range(1, sheet1.nrows):
        for j in range(end - start + 1):
            prepare["avg" + str(j)] += sheet1.cell_value(i, j + start)
            prepare["stdev" + str(j)].append(sheet1.cell_value(i, j + start))

    # 5个性状的均值
    for i in range(end - start + 1):
        prepare["avg" + str(i)] /= sheet1.nrows
    # for i in range(end-start +1):
    #     print(prepare["avg" + str(i)])
    #     77.000999000999
    #     73.30969030969031
    #     79.12787212787212
    #     104.32167832167832
    #     23.081918081918083
    # for i in range(end - start + 1):
    #     print(np.std(prepare["stdev" + str(i)],ddof=1))
    #     12.299642157282348
    #     4.572660081420903
    #     6.53933589242164
    #     5.016741142583668
    #     4.902857637440946
    sum = 0


    for i in range (1,sheet1.nrows):
        for j in range(1,sheet1.nrows):

            sum += (sheet1.cell_value(i, index1) * sheet1.cell_value(j, index2))
    sum = sum/np.square(sheet1.nrows)
    #print(sum)
    #性状从excel下表为8处开始
    # for i in range(end - start + 1):
    #     print("avg:",prepare["avg" + str(i)])
    # for i in range(end - start + 1):
    #     print("stdev",np.std(prepare["stdev" + str(i)],ddof=1))
    # print("sum",sum)
    # print("prepare",prepare["avg" + str(index1-start)] * prepare["avg" + str(index2-start)])
    # print("分子")
    # print(sum - (prepare["avg" + str(index1-start)] * prepare["avg" + str(index2-start)]))
    # print("分母")
    # print((np.std(prepare["stdev" + str(index1-start)],ddof=1) * np.std(prepare["stdev" + str(index2-start)],ddof=1)))

    #pcc_bw_hg = (sum - (prepare["avg" + str(index1-start)] * prepare["avg" + str(index2-start)])) / (np.std(prepare["stdev" + str(index1-start)],ddof=1) * np.std(prepare["stdev" + str(index2-start)],ddof=1))
    pcc_bw_hg = (sum_xy - sum_x_sum_y) / np.sqrt((square_sum_x - (np.square(sum_x) / sheet1.nrows)) * (square_sum_y - (np.square(sum_y) / sheet1.nrows)))
    #print(pcc_bw_hg)
    return pcc_bw_hg

def pcc(file):
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    start = load_profile()[0]
    end = load_profile()[1]
    lst = []
    index_pare = []
    for i in range(start,end):
        for j in range(i+1,end +1):
            lst .append(round(cal_pcc_bw_hg(i, j, file), 4))
            para1 = sheet1.cell_value(0, i)
            para2 = sheet1.cell_value(0, j)
            index_pare .append([para1,para2])
    return lst, index_pare


#show_pcc("data_enrichment.xls")
#print(pcc("breeding.xlsx"))