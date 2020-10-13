#Early Election Index（早选指数）
#性状为5个（8-12）
import xlrd
from load_profile import load_profile

def data_sepby_herd(file):
    start = load_profile()[0]
    end = load_profile()[1]
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name("Sheet1")
    herd = []
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i,6) not in herd:
            herd.append(sheet1.cell_value(i,6))
    count = locals()
    for i in range(len(herd)):
        count["count"+str(i)] = 0
    prepare = locals()#存储各个根据厂分的性状均值eg：公主岭的体重均值，肇州的体重均值
    for i in range(start, end + 1):#(8-12)
        for j in range(len(herd)):
            prepare["avg" + str(i) + "herd" + str(j)] = 0 #
    for j in range(start,end + 1):#性状

        for i in range(1,sheet1.nrows):#每条数据
            for k in range(len(herd)):#厂
                if sheet1.cell_value(i,6) == herd[k]:
                    prepare["avg" + str(j) + "herd" + str(k)] += sheet1.cell_value(i,j)
                    count["count" + str(k)] += 1
    for i in range(len(herd)):#每个性状加一遍，所以要除以性状数
        count["count" + str(i)] /= (end - start +1)
    for i in range(start, end +1):
        for j in range(len(herd)):
            prepare["avg" + str(i) + "herd" + str(j)] /= count["count"+str(j)]
    lst = []
    for i in range(start , end +1):
        for j in range(len(herd)):
            lst.append(prepare["avg" + str(i) + "herd" + str(j)])
    #print(herd)
    return lst, herd
#print(data_sepby_herd("breeding.xlsx")[0][1])


def data_process(file):
    start = load_profile()[0]
    end = load_profile()[1]
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name("Sheet1")
    avg = []#各性状的均值
    denominator = []#计算不同厂需要用到的分母
    herd_1 = []
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i,6) not in herd_1:
            herd_1.append(sheet1.cell_value(i,6))
    herd = locals()
    for i in range(len(herd_1)):
        herd["herd" + str(i)] = []
    for i in range(len(herd_1)):
        for j in range(0,len(data_sepby_herd(file)[0]), len(herd_1)):
            herd["herd" + str(i)].append(data_sepby_herd(file)[0][i+j])
    for i in range(len(herd_1)):
        herd["herd" + str(i)][2] = herd["herd" + str(i)][3]/herd["herd" + str(i)][2]
        herd["herd" + str(i)][3] = herd["herd" + str(i)][4]
        herd["herd" + str(i)].pop()
        del herd["herd" + str(i)][1]
    for j in range(start, end + 1):
        sum = 0
        for i in range(1, sheet1.nrows):

            sum += sheet1.cell_value(i, j)
        avg.append(sum/sheet1.nrows)
    del avg[1]
    outlook = locals()

    for i in range(len(herd_1)):
        outlook["outlook" + str(i)] = 0
        outlook["count" + str(i)] = 0
    for i in range(1,sheet1.nrows):
        for j in range(len(herd_1)):
            if sheet1.cell_value(i,6) == herd_1[j]:
                outlook["outlook" + str(j)] += sheet1.cell_value(i,14)
                outlook["count" + str(j)] += 1
    for j in range(len(herd_1)):
        outlook["outlook" + str(j)] /= outlook["count" + str(j)]
        herd["herd" + str(j)].append(outlook["outlook" + str(j)])
    w = [0.2,0.15,0.35,0.05]
    h = [0.614,0.423,0.621,0.206]
    for i in range(len(herd_1)):#厂数，有n个厂就有n个分母
        sum = 0
        for j in range(4):
            sum += w[j]*h[j]*herd["herd" + str(i)][j]
        denominator.append(sum + (0.25 * 0.5))

    # for i in range(len(herd_1)):
    #     print(herd["herd" + str(i)])
        #denominator.append(data_sepby_herd(file).prepare["avg12" + "herd" + str(i)]* 0.35 * 0.621 + 0.25 * 0.5 + 0.2 * 0.614 * data_sepby_herd(file).prepare["avg8" + "herd" + str(i)] + 0.15 * 0.423 * ())
    return avg,denominator
#print(data_process("breeding.xlsx"))
def cal_eei(file):

    file = file
    avg = data_process(file)[0]
    denominator = data_process(file)[1]
    herd = data_sepby_herd(file)[1]
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    lst = []
    for i in range(1, sheet1.nrows):
        score = 0
        # value =
        for j in range(len(herd)):
            if sheet1.cell_value(i, 6) == herd[j]:
                if sheet1.cell_value(i, 13) == "AA":
                    score = (0.25 + (0.35 * 0.621 * sheet1.cell_value(i, 12)) + (0.20 * 0.614 * sheet1.cell_value(i, 8)) + (
                                0.15 * 0.423 * (sheet1.cell_value(i, 11) / sheet1.cell_value(i, 10))) + (
                                         0.05 * 0.206 * sheet1.cell_value(i, 14))) * 10 / denominator[j]
                elif sheet1.cell_value(i, 13) == "AB":
                    # print(2)
                    score = ((0.25 * 0.5) + (0.35 * 0.621 * sheet1.cell_value(i, 12)) + (
                                0.20 * 0.614 * sheet1.cell_value(i, 8)) + (
                                         0.15 * 0.423 * (sheet1.cell_value(i, 11) / sheet1.cell_value(i, 10))) + (
                                         0.05 * 0.206 * sheet1.cell_value(i, 14))) * 10 / denominator[j]
                else:
                    # print(3)
                    score = ((0.35 * sheet1.cell_value(i, 12)) + (0.20 * 0.614 * sheet1.cell_value(i, 8)) + (
                                0.15 * 0.423 * (sheet1.cell_value(i, 11) / sheet1.cell_value(i, 10))) + (
                                         0.05 * 0.206 * sheet1.cell_value(i, 14))) * 10 / denominator[j]
        lst.append("%.2f" % score)
    return lst
# print(data_sepby_herd("breeding.xlsx"))
# print(data_process("breeding.xlsx"))
# print(cal_eei("breeding.xlsx"))
