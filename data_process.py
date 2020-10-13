#可优化地方 使用end - start代替函数执行
#可优化地方 代码见名知意，修改变量函数命名
import xlrd
import numpy as np
import cal_her
import inspect
from load_profile import load_profile
def get_variable_name(variable):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is variable]

# file = "breeding.xlsx"
# f1 = xlrd.open_workbook(file)
# sheet1 = f1.sheet_by_name('Sheet1')


def data_process(file): #公牛数（len（bull）），畜群数（len（herd））
    #    return sheet1.nrows-1, herdoffspring, bulloffspring, bull1_herd, bull2_herd
          #       36             [18,18]         [18,18]         [11，7]      [7, 11]

    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    bull = []#公牛名
    herd = []#畜群名
    for i in range(1, sheet1.nrows):
        # 判断公牛数和种群数
        if sheet1.cell_value(i, 4) not in bull:
            bull.append(sheet1.cell_value(i, 4))
        if sheet1.cell_value(i, 6) not in herd:
            herd.append(sheet1.cell_value(i, 6))
    #每头公牛的后代数
    bulloffspring = [0 for index in range(len(bull))]  # 每头牛
    #每个厂的后代数
    herdoffspring = [0 for index in range(len(herd))]
    #i头公牛在j个厂的后代数
    prepare = locals()#eg:prepare[bull0_herd0]第一头牛在第一个厂的后代数
    for i in range(len(bull)):#牛
        for j in range(len(herd)):
            prepare["bull" + str(i) + "_herd" + str(j)] = 0

    #判断公牛i的后代数,和畜群j的后代数
    for i in range(1,sheet1.nrows):
        for j in range(len(bull)):
            if sheet1.cell_value(i,4) == bull[j]:#判断父亲为第i头公牛，第i头公牛后代+1
                bulloffspring[j] += + 1#40457牛
        #公牛数为2，直接else
        #else :
            #bulloffspring[1] += + 1#40004牛
        for j in range(len(herd)):

            if sheet1.cell_value(i,6) == herd[j]:#判断种群为第i头种群，第i厂后代+1
                herdoffspring[j] += 1 #畜群1


    for i in range(1,sheet1.nrows):
        for j in range(len(bull)):
            if sheet1.cell_value(i, 4) == bull[j]:
                for k in range(len(herd)):

                    if sheet1.cell_value(i,6) ==herd[k]:
                        prepare["bull" + str(j) + "_herd" + str(k)] += 1
    # for i in range(len(bull)):
    #     for j in range(len(herd)):
    #         print(prepare.get("bull" + str(i) + "_herd" + str(j)))
    return sheet1.nrows-1, herdoffspring, bulloffspring, prepare,bull,herd
#           0               1               2               3      4    5
#print(data_process())
#print(data_process("data_enrichment.xls"))
#print(data_process("breeding.xlsx"))
# def matrix1(file):
#     file = file
#     f1 = xlrd.open_workbook(file)
#     sheet1 = f1.sheet_by_name('Sheet1')
#     #初始化矩阵
#     matrix_1 = np.mat(np.zeros((1,len(data_process(file)[4]) + len(data_process(file)[5]) + 1)))
#     matrix_2 = np.mat(np.zeros((len(data_process(file)[5]),len(data_process(file)[4]) + len(data_process(file)[5]) + 1)))
#     matrix_3 = np.mat(np.zeros((len(data_process(file)[4]), len(data_process(file)[4]) + len(data_process(file)[5]) + 1)))
#
#     matrix_1[0,0] = sheet1.nrows -1
#     for i in range(len(data_process(file)[5])):#畜群数
#         matrix_1[0,i+1] = data_process(file)[1][i]
#     for i in range(len(data_process(file)[4])):
#         matrix_1[0,len(data_process(file)[5]) + 1 + i] = data_process(file)[2][i]
#     #print(matrix_1)
#     # for i in range(len(data_process()[4]) + len(data_process()[5]) + 1):
#     #     for j in range(len(data_process()[4]) + len(data_process()[5]) + 1):
#     #         matrix[i,j] =
#     # return matrix
#     for i in range(len(data_process(file)[5])):
#         matrix_2[i,0] = data_process(file)[1][i]
#
#     for i in range(len(data_process(file)[4])):
#         matrix_3[i,0] =data_process(file)[2][i]
#     for i in range(len(data_process(file)[5])):
#         for j in range(len(data_process(file)[5])):
#             if i != j:
#                 matrix_2[i,j+1] = 0
#             else:
#                 matrix_2[i,j+1] = data_process(file)[1][i]
#     for i in range(len(data_process(file)[4])):
#         for j in range(len(data_process(file)[5])):
#             matrix_2[i, j+1+len(data_process(file)[5])] = data_process(file)[3].get("bull"+str(i)+"_herd" +str(j))
#     for i in range(len(data_process(file)[4])):#牛
#         for j in range(len(data_process(file)[5])):#厂
#             matrix_3[i,j+1] = data_process(file)[3].get("bull"+str(i)+"_herd" +str(j))
#     for i in range(len(data_process(file)[4])):
#         for j in range(len(data_process(file)[4])):
#             if i != j:
#                 matrix_3[i,len(data_process(file)[5])+1+j] = 0
#             else:
#                 matrix_3[i,len(data_process(file)[5]) +1+j] = data_process(file)[2][i]
#     matrix = np.row_stack((matrix_1,matrix_2))
#     matrix = np.row_stack((matrix,matrix_3))
#
#     # print(matrix_1)
#     # print(matrix_2)
#     # print(matrix_3)
#     return matrix
def matrix1(file):
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    l1 = []
    for i in data_process(file):
        l1.append(i)
    #初始化矩阵
    matrix_1 = np.mat(np.zeros((1,len(l1[4]) + len(l1[5]) + 1)))
    matrix_2 = np.mat(np.zeros((len(l1[5]),len(l1[4]) + len(l1[5]) + 1)))
    matrix_3 = np.mat(np.zeros((len(l1[4]), len(l1[4]) + len(l1[5]) + 1)))

    matrix_1[0,0] = sheet1.nrows -1
    for i in range(len(l1[5])):#畜群数
        matrix_1[0,i+1] = l1[1][i]
    for i in range(len(l1[4])):
        matrix_1[0,len(l1[5]) + 1 + i] = l1[2][i]
    #print(matrix_1)
    # for i in range(len(data_process()[4]) + len(data_process()[5]) + 1):
    #     for j in range(len(data_process()[4]) + len(data_process()[5]) + 1):
    #         matrix[i,j] =
    # return matrix
    for i in range(len(l1[5])):
        matrix_2[i,0] = l1[1][i]

    for i in range(len(l1[4])):
        matrix_3[i,0] = l1[2][i]
    for i in range(len(l1[5])):
        for j in range(len(l1[5])):
            if i != j:
                matrix_2[i,j+1] = 0
            else:
                matrix_2[i,j+1] = l1[1][i]
    for i in range(len(l1[4])):
        for j in range(len(l1[5])):
            matrix_2[i, j+1+len(l1[5])] = l1[3].get("bull"+str(i)+"_herd" +str(j))
    for i in range(len(l1[4])):#牛
        for j in range(len(l1[5])):#厂
            matrix_3[i,j+1] = l1[3].get("bull"+str(i)+"_herd" +str(j))
    for i in range(len(l1[4])):
        for j in range(len(l1[4])):
            if i != j:
                matrix_3[i,len(l1[5])+1+j] = 0
            else:
                matrix_3[i,len(l1[5]) +1+j] = l1[2][i]
    matrix = np.row_stack((matrix_1,matrix_2))
    matrix = np.row_stack((matrix,matrix_3))

    # print(matrix_1)
    # print(matrix_2)
    # print(matrix_3)
    return matrix
#print(matrix1("data_enrichment.xls"))
#print(matrix1("breeding.xlsx"))
# [[1000.  300.  361.  339.  351.  335.  314.]
#  [ 300.  300.    0.    0.  103.  125.  123.]
#  [ 361.    0.  361.    0.  117.  118.  100.]
#  [ 339.    0.    0.  339.   80.  118.  116.]
#  [ 351.  103.  125.  123.  351.    0.    0.]
#  [ 335.  117.  118.  100.    0.  335.    0.]
#  [ 314.   80.  118.  116.    0.    0.  314.]]
def matrix_bw(n,file):
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    l1 = []
    for i in data_process(file):
        l1.append(i)
    matrix_bw = np.mat(np.zeros((len(l1[4]) + len(l1[5]) + 1, 1)))
    for i in range(1, sheet1.nrows):
        matrix_bw[0] += sheet1.cell_value(i, n)
        for j in range(len(l1[5])):
            if sheet1.cell_value(i,6) ==l1[5][j]:
                matrix_bw[1+j] += sheet1.cell_value(i, n)
                break
        for k in range(len(l1[4])):
            if sheet1.cell_value(i,4)==l1[4][k]:
                matrix_bw[1+len(l1[5])+k] +=sheet1.cell_value(i,n)
                break
    return matrix_bw
# matrix_bw(8,"data_enrichment.xls")
#print(matrix_bw(8,"breeding.xlsx"))
def BLUP_scor_bw(n,file):
    bw = cal_her.her_bw(n,file)
    k = round((4 - bw) / bw, 0)
    mat = matrix1(file)
    l1 = []
    for i in data_process(file):
        l1.append(i)
    for i in range(len(l1[4])):
        mat[1+len(l1[5])+i,1+len(l1[5])+i] += k
    #固定因子限制法
    mat = np.row_stack((mat, np.zeros((1,1+len(l1[4]) + len(l1[5])))))
    mat[1+len(l1[4]) + len(l1[5]),1] = 1
    mat = np.column_stack((mat,np.zeros(2+len(l1[4]) + len(l1[5]))))
    mat[1,1+len(l1[4]) + len(l1[5])] = 1
    mat = mat.I
    #使估计值第二项和最后一项为0
    for i in range(2+len(l1[4]) + len(l1[5])):
        mat[1,i] = 0
        mat[1+len(l1[4]) + len(l1[5])] = 0

    mat2 = matrix_bw(n, file)
    mat2 = np.row_stack((mat2, [0]))
    #print(mat * mat2)
    BLUP_scor_bw_temp = []
    for i in range(len(l1[4])):

        BLUP_scor_bw_temp.append((mat*mat2)[1+len(l1[5]) + i])
    BLUP_scor_bw = []
    for i in range(len(BLUP_scor_bw_temp)):
        BLUP_scor_bw.append(2*np.array(BLUP_scor_bw_temp[i])[0][0])
    return BLUP_scor_bw
    #return mat
#print(BLUP_scor_bw(8,"breeding.xlsx"))
#print(BLUP_scor_bw(8,"data_enrichment.xls"))
#
# [[1000.  300.  361.  339.  351.  335.  314.]
#  [ 300.  300.    0.    0.  103.  125.  123.]
#  [ 361.    0.  361.    0.  117.  118.  100.]
#  [ 339.    0.    0.  339.   80.  118.  116.]
#  [ 351.  103.  125.  123.  355.    0.    0.]
#  [ 335.  117.  118.  100.    0.  339.    0.]
#  [ 314.   80.  118.  116.    0.    0.  318.]]

def bv(file):
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    start = load_profile()[0]
    end = load_profile()[1]
    #print("各种性状的育种值为：")
    lst = []
    index1 = data_process(file)[4]#公牛编号
    index2 = []#性状名
    for i in range(end - start + 1):
        lst.append(BLUP_scor_bw(start+i, file))
        index2.append(sheet1.cell_value(0,start + i))
        #print(BLUP_scor_bw(start+i,file))

    return lst,index1,index2#0：个性状各公牛育种值 1：公牛编号 2：性状名
def cbv(file):
    start = load_profile()[0]
    end = load_profile()[1]
    lst = []
    index1 = data_process(file)[4]
    l1 = []#优化运行速度
    for i in data_process(file):
        l1.append(i)
    l2 = []
    for i in range(end - start + 1):
        l2.append(BLUP_scor_bw(start+i,file))

    prepare = locals()

    for i in range(len(l1[4])):
        prepare["BLUP"+str(i)] = []
    # for i in range(end-start + 1):
    #     for j in range(len(l1[4])):
    #         prepare["BLUP"+str(j)].append(BLUP_scor_bw(start+i,file)[j])

    for j in range(len(l1[4])):#公牛
        for i in range(end - start + 1):
            prepare["BLUP"+str(j)].append(l2[i][j])#list
    # for i in range(len(l1[4])):
    #     print(type(prepare["BLUP"+str(j)]))
    #CBV
    W = load_profile()[2]
    prepare2 = locals()
    for i in range(len(l1[4])):#牛
        prepare2["CBV" + str(i)] = 0
    # for i in range(end-start+1):#性状数
    #     for j in range(len(l1[4])):#公牛数
    #         #print(float(W[i]))
    #         #print(prepare["BLUP" + str(j)][i])
    #         prepare2["CBV" + str(j)] += float(W[i]) * prepare["BLUP"+str(j)][i]

    for j in range(len(l1[4])):#公牛数
        for i in range(end - start + 1):  # 性状数
            #print(float(W[i]))
            #print(prepare["BLUP" + str(j)][i])
            prepare2["CBV" + str(j)] += (float(W[i]) * prepare["BLUP"+str(j)][i])

    #print("综合育种值为：")
    for i in range(len(l1[4])):
        lst.append(round(prepare2["CBV" + str(i)], 4))
        #print(prepare2["CBV" + str(i)])
    return lst,index1
# blupscore("data_enrichment.xls")
# cbv("data_enrichment.xls")
#print(bv("breeding.xlsx"))
#print(cbv("breeding.xlsx"))



#不是数字返回true，是数字返回false
def not_number(s):
    try:
        float(s)
        return False
    except ValueError:
        pass

    return True
# print(not_number('foo'))
# print(not_number('1'))     # True
# print(not_number('1.3'))   # True
# print(not_number('-1.37')) # True
# print(not_number('1e3'))   # True