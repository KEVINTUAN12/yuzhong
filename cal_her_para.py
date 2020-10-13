#计算遗传力需要的参数（各基因型各形状的平均表现值、基因型频度、基因频度）
from load_profile import load_profile
import xlrd
def cal_her_gene(file):#计算基因型频率 0:count_AA,1:count_AB,2:count_BB,3:fre_AA,4:fre_AB,5:fre_BB,6:fre_A,7:fre_B
    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    count_AA = 0
    count_AB = 0
    count_BB = 0

    for i in range(1,sheet1.nrows):
        if sheet1.cell_value(i,13)=="AA":
            count_AA=count_AA+1
        elif sheet1.cell_value(i,13) =="AB":
            count_AB = count_AB+1
        else:
            count_BB = count_BB + 1
    """print("count_AA=",count_AA)
    print("count_AB=",count_AB)
    print("count_BB=",count_BB)"""
    sum = (count_AA + count_AB + count_BB) * 2  # 总基因数
    fre_AA = round(count_AA/(count_AA + count_AB + count_BB), 2)
    fre_AB = round(count_AB / (count_AA + count_AB + count_BB), 2)
    fre_BB = round(count_BB / (count_AA + count_AB + count_BB), 2)
    fre_A = round ((count_AA * 2 +count_AB)/sum, 3)
    fre_B = round((count_AB + count_BB * 2)/sum, 3)
    """print(fre_A,fre_B)
    print(fre_A+fre_B)"""
    return count_AA,count_AB,count_BB,fre_AA,fre_AB,fre_BB,fre_A,fre_B#<class 'tuple'>

def cal_her_bw(n,file):#计算各基因型的各性状表现型值

    file = file
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    sum_bw_AA = 0
    sum_bw_AB = 0
    sum_bw_BB = 0
    #cal_her_gene()
    for i in range(1,sheet1.nrows):
        if sheet1.cell_value(i,13) =="AA":
            sum_bw_AA = sum_bw_AA + sheet1.cell_value(i,n)
        elif sheet1.cell_value(i,13) =="AB":
            sum_bw_AB = sum_bw_AB + sheet1.cell_value(i,n)
        else:
            sum_bw_BB = sum_bw_BB + sheet1.cell_value(i,n)
    avg_bw_AA = round(sum_bw_AA/cal_her_gene(file)[0], 2)#AA基因型平均体重
    avg_bw_AB = round(sum_bw_AB/cal_her_gene(file)[1], 2)
    avg_bw_BB = round(sum_bw_BB/cal_her_gene(file)[2], 2)
    """print("avg_bw_AA=",avg_bw_AA)
    print("avg_bw_AB=",avg_bw_AB)
    print("avg_bw_BB=", avg_bw_BB)"""
    return avg_bw_AA,avg_bw_AB,avg_bw_BB
def cal_her_hg():#计算各基因型的体高表现型值（早选指数中没用到的）
    file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    sum_hg_AA = 0
    sum_hg_AB = 0
    sum_hg_BB = 0
    #cal_her_gene()
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i, 13) == "AA":
            sum_hg_AA = sum_hg_AA + sheet1.cell_value(i, 9)
        elif sheet1.cell_value(i, 13) == "AB":
            sum_hg_AB = sum_hg_AB + sheet1.cell_value(i, 9)
        else:
            sum_hg_BB = sum_hg_BB + sheet1.cell_value(i, 9)
    avg_hg_AA = round(sum_hg_AA / cal_her_gene()[0], 2)# AA基因型平均体重
    avg_hg_AB = round(sum_hg_AB / cal_her_gene()[1], 2)
    avg_hg_BB = round(sum_hg_BB / cal_her_gene()[2], 2)
    """print("avg_hg_AA=", avg_hg_AA)
    print("avg_hg_AB=", avg_hg_AB)
    print("avg_hg_BB=", avg_hg_BB)"""
    return avg_hg_AA, avg_hg_AB, avg_hg_BB
def cal_her_bl():#计算各基因型的体长表现型值
    file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    sum_bl_AA = 0
    sum_bl_AB = 0
    sum_bl_BB = 0
    #cal_her_gene()
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i, 13) == "AA":
            sum_bl_AA = sum_bl_AA + sheet1.cell_value(i, 10)
        elif sheet1.cell_value(i, 13) == "AB":
            sum_bl_AB = sum_bl_AB + sheet1.cell_value(i, 10)
        else:
            sum_bl_BB = sum_bl_BB + sheet1.cell_value(i, 10)
    avg_bl_AA = round(sum_bl_AA / cal_her_gene()[0], 2)  # AA基因型平均体长
    avg_bl_AB = round(sum_bl_AB / cal_her_gene()[1], 2)
    avg_bl_BB = round(sum_bl_BB / cal_her_gene()[2], 2)
    """print("avg_bl_AA=", avg_bl_AA)
    print("avg_bl_AB=", avg_bl_AB)
    print("avg_bl_BB=", avg_bl_BB)"""
    return avg_bl_AA, avg_bl_AB, avg_bl_BB
def cal_her_cw():#计算各基因型的胸围表现型值
    file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    sum_cw_AA = 0
    sum_cw_AB = 0
    sum_cw_BB = 0
    #cal_her_gene()
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i, 13) == "AA":
            sum_cw_AA = sum_cw_AA + sheet1.cell_value(i, 11)
        elif sheet1.cell_value(i, 13) == "AB":
            sum_cw_AB = sum_cw_AB + sheet1.cell_value(i, 11)
        else:
            sum_cw_BB = sum_cw_BB + sheet1.cell_value(i, 11)
    avg_cw_AA = round(sum_cw_AA / cal_her_gene()[0], 2)  # AA基因型平均胸围
    avg_cw_AB = round(sum_cw_AB / cal_her_gene()[1], 2)
    avg_cw_BB = round(sum_cw_BB / cal_her_gene()[2], 2)
    """print("avg_cw_AA=", avg_cw_AA)
    print("avg_cw_AB=", avg_cw_AB)
    print("avg_cw_BB=", avg_cw_BB)"""
    return avg_cw_AA, avg_cw_AB, avg_cw_BB
def cal_her_ema():#计算各基因型的眼肌面积表现型值
    file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    sum_ema_AA = 0
    sum_ema_AB = 0
    sum_ema_BB = 0
    #cal_her_gene()
    for i in range(1, sheet1.nrows):
        if sheet1.cell_value(i, 13) == "AA":
            sum_ema_AA = sum_ema_AA + sheet1.cell_value(i, 12)
        elif sheet1.cell_value(i, 13) == "AB":
            sum_ema_AB = sum_ema_AB + sheet1.cell_value(i, 12)
        else:
            sum_ema_BB = sum_ema_BB + sheet1.cell_value(i, 12)
    avg_ema_AA = round(sum_ema_AA / cal_her_gene()[0], 2)  # AA基因型平均眼肌面积
    avg_ema_AB = round(sum_ema_AB / cal_her_gene()[1], 2)
    avg_ema_BB = round(sum_ema_BB / cal_her_gene()[2], 2)
    """print("avg_ema_AA=", avg_ema_AA)
    print("avg_ema_AB=", avg_ema_AB)
    print("avg_ema_BB=", avg_ema_BB)"""
    return avg_ema_AA, avg_ema_AB, avg_ema_BB

def avg_effect_bw(n,file):#计算体重性状中基因的平均效应
    A_avg_effect_bw = ((cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2 + (cal_her_gene(file)[6] - cal_her_gene(file)[7]) * (cal_her_bw(n,file)[2]-(cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2) +
                       2 * cal_her_gene(file)[6] * cal_her_gene(file)[7] *  (cal_her_bw(n,file)[1]-(cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2)) - cal_her_gene(file)[6] * ((cal_her_bw(n,file)[2] - (cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2)+(cal_her_gene(file)[7] - cal_her_gene(file)[6]) * (cal_her_bw(n,file)[1]-(cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2))
    B_avg_effect_bw = ((cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2 + (cal_her_gene(file)[6] - cal_her_gene(file)[7]) * (cal_her_bw(n,file)[2]-(cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2) +
                       2 * cal_her_gene(file)[6] * cal_her_gene(file)[7] *  (cal_her_bw(n,file)[1]-(cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2))+ cal_her_gene(file)[7] * ((cal_her_bw(n,file)[2] - (cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2)+(cal_her_gene(file)[7] - cal_her_gene(file)[6]) * (cal_her_bw(n,file)[1]-(cal_her_bw(n,file)[0] + cal_her_bw(n,file)[2])/2))

    return A_avg_effect_bw,B_avg_effect_bw

def avg_effect_hg():#计算体高性状中基因的平均效应
    A_avg_effect_hg = ((cal_her_hg()[0] + cal_her_hg()[2])/2 + (cal_her_gene()[6] - cal_her_gene()[7]) * (cal_her_hg()[2]-(cal_her_hg()[0] + cal_her_hg()[2])/2) +
                       2 * cal_her_gene()[6] * cal_her_gene()[7] *  (cal_her_hg()[1]-(cal_her_hg()[0] + cal_her_hg()[2])/2)) - cal_her_gene()[6] * ((cal_her_hg()[2] - (cal_her_hg()[0] + cal_her_hg()[2])/2)+(cal_her_gene()[7] - cal_her_gene()[6]) * (cal_her_hg()[1]-(cal_her_hg()[0] + cal_her_hg()[2])/2))
    B_avg_effect_hg = ((cal_her_hg()[0] + cal_her_hg()[2])/2 + (cal_her_gene()[6] - cal_her_gene()[7]) * (cal_her_hg()[2]-(cal_her_hg()[0] + cal_her_hg()[2])/2) +
                       2 * cal_her_gene()[6] * cal_her_gene()[7] *  (cal_her_hg()[1]-(cal_her_hg()[0] + cal_her_hg()[2])/2))+ cal_her_gene()[7] * ((cal_her_hg()[2] - (cal_her_hg()[0] + cal_her_hg()[2])/2)+(cal_her_gene()[7] - cal_her_gene()[6]) * (cal_her_hg()[1]-(cal_her_hg()[0] + cal_her_hg()[2])/2))

    return A_avg_effect_hg,B_avg_effect_hg

def avg_effect_bl():#计算体长性状中基因的平均效应
    A_avg_effect_bl = ((cal_her_bl()[0] + cal_her_bl()[2])/2 + (cal_her_gene()[6] - cal_her_gene()[7]) * (cal_her_bl()[2]-(cal_her_bl()[0] + cal_her_bl()[2])/2) +
                       2 * cal_her_gene()[6] * cal_her_gene()[7] *  (cal_her_bl()[1]-(cal_her_bl()[0] + cal_her_bl()[2])/2)) - cal_her_gene()[6] * ((cal_her_bl()[2] - (cal_her_bl()[0] + cal_her_bl()[2])/2)+(cal_her_gene()[7] - cal_her_gene()[6]) * (cal_her_bl()[1]-(cal_her_bl()[0] + cal_her_bl()[2])/2))
    B_avg_effect_bl = ((cal_her_bl()[0] + cal_her_bl()[2])/2 + (cal_her_gene()[6] - cal_her_gene()[7]) * (cal_her_bl()[2]-(cal_her_bl()[0] + cal_her_bl()[2])/2) +
                       2 * cal_her_gene()[6] * cal_her_gene()[7] *  (cal_her_bl()[1]-(cal_her_bl()[0] + cal_her_bl()[2])/2))+ cal_her_gene()[7] * ((cal_her_bl()[2] - (cal_her_bl()[0] + cal_her_bl()[2])/2)+(cal_her_gene()[7] - cal_her_gene()[6]) * (cal_her_bl()[1]-(cal_her_bl()[0] + cal_her_bl()[2])/2))

    return A_avg_effect_bl,B_avg_effect_bl

def avg_effect_cw():#计算胸围性状中基因的平均效应
    A_avg_effect_cw = ((cal_her_cw()[0] + cal_her_cw()[2])/2 + (cal_her_gene()[6] - cal_her_gene()[7]) * (cal_her_cw()[2]-(cal_her_cw()[0] + cal_her_cw()[2])/2) +
                       2 * cal_her_gene()[6] * cal_her_gene()[7] *  (cal_her_cw()[1]-(cal_her_cw()[0] + cal_her_cw()[2])/2)) - cal_her_gene()[6] * ((cal_her_cw()[2] - (cal_her_cw()[0] + cal_her_cw()[2])/2)+(cal_her_gene()[7] - cal_her_gene()[6]) * (cal_her_cw()[1]-(cal_her_cw()[0] + cal_her_cw()[2])/2))
    B_avg_effect_cw = ((cal_her_cw()[0] + cal_her_cw()[2])/2 + (cal_her_gene()[6] - cal_her_gene()[7]) * (cal_her_cw()[2]-(cal_her_cw()[0] + cal_her_cw()[2])/2) +
                       2 * cal_her_gene()[6] * cal_her_gene()[7] *  (cal_her_cw()[1]-(cal_her_cw()[0] + cal_her_cw()[2])/2))+ cal_her_gene()[7] * ((cal_her_cw()[2] - (cal_her_cw()[0] + cal_her_cw()[2])/2)+(cal_her_gene()[7] - cal_her_gene()[6]) * (cal_her_cw()[1]-(cal_her_cw()[0] + cal_her_cw()[2])/2))

    return A_avg_effect_cw,B_avg_effect_cw

def avg_effect_ema():#计算眼肌面积性状中基因的平均效应
    A_avg_effect_ema = ((cal_her_ema()[0] + cal_her_ema()[2])/2 + (cal_her_gene()[6] - cal_her_gene()[7]) * (cal_her_ema()[2]-(cal_her_ema()[0] + cal_her_ema()[2])/2) +
                       2 * cal_her_gene()[6] * cal_her_gene()[7] *  (cal_her_ema()[1]-(cal_her_ema()[0] + cal_her_ema()[2])/2)) - cal_her_gene()[6] * ((cal_her_ema()[2] - (cal_her_ema()[0] + cal_her_ema()[2])/2)+(cal_her_gene()[7] - cal_her_gene()[6]) * (cal_her_ema()[1]-(cal_her_ema()[0] + cal_her_ema()[2])/2))
    B_avg_effect_ema = ((cal_her_ema()[0] + cal_her_ema()[2])/2 + (cal_her_gene()[6] - cal_her_gene()[7]) * (cal_her_ema()[2]-(cal_her_ema()[0] + cal_her_ema()[2])/2) +
                       2 * cal_her_gene()[6] * cal_her_gene()[7] *  (cal_her_ema()[1]-(cal_her_ema()[0] + cal_her_ema()[2])/2))+ cal_her_gene()[7] * ((cal_her_ema()[2] - (cal_her_ema()[0] + cal_her_ema()[2])/2)+(cal_her_gene()[7] - cal_her_gene()[6]) * (cal_her_ema()[1]-(cal_her_ema()[0] + cal_her_ema()[2])/2))

    return A_avg_effect_ema,B_avg_effect_ema

#cal_her_hg()
#cal_her_bl()
#cal_her_cw()
#cal_her_ema()
#cal_her_gene()
#print(avg_effect_bw())
#print(avg_effect_bw())
#print(avg_effect_bl())
#print(avg_effect_cw())
#print(avg_effect_ema())
#print(avg_effect_hg())
# start = load_profile()[0]
# end = load_profile()[1]
# for i in range(end-start +1):
#     print(cal_her_bw(start + i))
#     print(avg_effect_bw(start + i))
