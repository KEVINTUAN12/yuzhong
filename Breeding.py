import xlrd
file = "breeding.xlsx"
avg_weight_gzl = 71.1#公主岭平均体重
avg_weight_zz = 85.5#肇州平均体重
avg_height_gzl = 70.8#
avg_height_zz = 72.1
avg_bl_gzl = 77.6
avg_bl_zz = 83.2
avg_cw_gzl = 104.8
avg_cw_zz = 105.7
avg_ema_gzl =20.1
avg_ema_zz = 25.1
avg_bt_gzl = avg_cw_gzl/avg_bl_gzl
avg_bt_zz = avg_cw_zz/avg_bl_zz
avg_outlook_gzl = 93.4
avg_outlook_zz = 93.1
denominator_gzl = 14.3#avg_ema_gzl * 0.35 * 0.621 + 0.25 * 0.5 + 0.2 * 0.614 * avg_weight_gzl + 0.15 * 0.423 * avg_bt_gzl + avg_outlook_gzl * 0.206 * 0.05
denominator_zz = 17.1#avg_ema_zz * 0.35 * 0.621 + 0.25 * 0.5 + 0.2 * 0.614 * avg_weight_zz + 0.15 * 0.423 * avg_bt_zz + avg_outlook_zz * 0.206 * 0.05
#print(denominator_gzl)
#score = 0
#w = [0.35,0.25,0.2,0.15,0.05]
#h =
lst = []

def Evaluation1():
    count = 0
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    #print(type(sheet1.cell_value(1,6)))#str
    #print(sheet1.cell_value(1, 6))#"公主岭"
    #print(type(sheet1.cell_value(1, 13)))
    #print(sheet1.cell_value(7, 13))#"AA"
    for i in range(1,37):
        score = 0
        #value =

        if sheet1.cell_value(i,6) == "公主岭":
            if sheet1.cell_value(i,13) == "AA":
                #print(1)
                #print("abc")
                #print(i)
                #print(sheet1.cell_value(i,13))
                #print(sheet1.cell_value(i,13) is "AA")
                score = (0.25 + (0.35 * 0.621 * sheet1.cell_value(i,12)) + (0.20 * 0.614 * sheet1.cell_value(i,8)) + (0.15 * 0.423 * (sheet1.cell_value(i,11)/sheet1.cell_value(i,10))) + (0.05*0.206*sheet1.cell_value(i,14)))*10 / denominator_gzl
            elif sheet1.cell_value(i,13) == "AB":
                #print(2)
                score = ((0.25*0.5) + (0.35* 0.621 * sheet1.cell_value(i, 12)) + (0.20* 0.614 * sheet1.cell_value(i, 8)) + (0.15* 0.423 * (sheet1.cell_value(i, 11) / sheet1.cell_value(i, 10))) + (0.05 *0.206* sheet1.cell_value(i, 14)))*10 / denominator_gzl
            else:
                #print(3)
                score = ((0.35 * sheet1.cell_value(i,12)) + (0.20* 0.614 * sheet1.cell_value(i,8)) + (0.15* 0.423 * (sheet1.cell_value(i,11)/sheet1.cell_value(i,10))) + (0.05*0.206*sheet1.cell_value(i,14)))*10 / denominator_gzl
        #print(score)
        #print(sheet1.cell_value(i,6)== "公主岭")
        #print(sheet1.cell_value(i,14))
        else :
            if sheet1.cell_value(i,13) == "AA":
                #print(4)
                #print(i)
                #print(sheet1.cell_value(i,13))
                #print(sheet1.cell_value(i,13) is "AA")
                score = (0.25 + (0.35 * sheet1.cell_value(i,12)) + (0.20* 0.614 * sheet1.cell_value(i,8)) + (0.15* 0.423 * (sheet1.cell_value(i,11)/sheet1.cell_value(i,10))) + (0.05*0.206*sheet1.cell_value(i,14)))*10 / denominator_zz
            elif sheet1.cell_value(i,13) == "AB":
                #print(5)
                score = ((0.25*0.5) + (0.35 * sheet1.cell_value(i, 12)) + (0.20* 0.614 * sheet1.cell_value(i, 8)) + (0.15* 0.423 * (sheet1.cell_value(i, 11) / sheet1.cell_value(i, 10))) + (0.05*0.206 * sheet1.cell_value(i, 14)))*10 / denominator_zz
            else:
                #print(6)
                score = ((0.35 * sheet1.cell_value(i,12)) + (0.20* 0.614 * sheet1.cell_value(i,8)) + (0.15 * 0.423* (sheet1.cell_value(i,11)/sheet1.cell_value(i,10))) + (0.05*0.206*sheet1.cell_value(i,14)))*10 / denominator_zz
        print(score)
        count = count + 1
    print(count)
        #print(count + " " + score)
        #count = count + 1
        #lst.append(score)
    #print("content of list ：")
    #for i in lst:
        #print(i)

def Evaluation2():
    score = 0
    print("请输入场次信息：")
    farm = input()
    print("请输入体重信息：")
    bw = float(input())
    print("请输入体长信息：")
    bl = float(input())
    print("请输入胸围：")
    cw = float(input())
    print("请输入眼肌面积：")
    ema = float(input())
    print("请输入基因型：")
    gene = input()
    print("请输入外貌评分：")
    outlook = float(input())
    bt = cw / bl
    if farm == "公主岭":
        if gene is "AA":
            score = (0.25 + (0.35 * 0.621 * ema) + (0.20 * 0.614 * bw) + (
                        0.15 * 0.423 * bt) + (
                                 0.05 * 0.206 * outlook)) * 10 / denominator_gzl
        elif gene is "AB":
            score = ((0.25 * 0.5) + (0.35 * 0.621 * ema) + (
                        0.20 * 0.614 * bw) + (
                                 0.15 * 0.423 * bt) + (
                                 0.05 * 0.206 * outlook)) * 10 / denominator_gzl
        else:
            score = ((0.35 * ema) + (0.20 * 0.614 * bw) + (
                        0.15 * 0.423 * bt) + (
                                 0.05 * 0.206 * outlook)) * 10 / denominator_gzl
    else:#肇州
        if gene is "AA":
            score = (0.25 + (0.35 * 0.621 * ema) + (0.20 * 0.614 * bw) + (
                        0.15 * 0.423 * bt) + (
                                 0.05 * 0.206 * outlook)) * 10 / denominator_zz
        elif gene is "AB":
            score = ((0.25 * 0.5) + (0.35 * 0.621 * ema) + (
                        0.20 * 0.614 * bw) + (
                                 0.15 * 0.423 * bt) + (
                                 0.05 * 0.206 * outlook)) * 10 / denominator_zz
        else:
            score = ((0.35 * ema) + (0.20 * 0.614 * bw) + (
                        0.15 * 0.423 * bt) + (
                                 0.05 * 0.206 * outlook)) * 10 / denominator_zz

    print(score)
Evaluation1()
#Evaluation2()