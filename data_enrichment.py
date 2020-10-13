import numpy as np
import xlrd
import xlwt
import random
from load_profile import load_profile
start = load_profile()[0]
end = load_profile()[1]
def data_enrichment(n):
    file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('Sheet1')
    #存放性状值
    prepare = locals()
    for i in range(end - start +2 ):#性状 + 外贸评分
        prepare["trait" + str(i)] = []
    for i in range(sheet1.ncols):
        # 参数对应 行, 列, 值
        worksheet.write(0, i, sheet1.cell_value(0, i))
    for i in range(end - start +2 ):
        max = 0
        min = 100000
        if i ==end-start+1:
            for k in range(1,sheet1.nrows):
                if sheet1.cell_value(k, sheet1.ncols-1) > max:
                    max = sheet1.cell_value(k, sheet1.ncols-1)
                if sheet1.cell_value(k, sheet1.ncols-1) < min:
                    min = sheet1.cell_value(k, sheet1.ncols-1)
            prepare["trail" + str(i)] = np.random.randint(min, max, n)
            break
        for j in range(1,sheet1.nrows):
            if sheet1.cell_value(j,i+start) > max:
                max = sheet1.cell_value(j,i+start)
            if sheet1.cell_value(j,i+start) <min:
                min = sheet1.cell_value(j,i+start)
        prepare["trail" + str(i)] = np.random.randint(min, max, n)
    for i in range(1,n+1):
        worksheet.write(i,0,i)
        #假设耳标没用为了生成数据，随机生成随机数
        worksheet.write(i,1,random.randint(0,1000))
        worksheet.write(i,2,random.choice(['公','母']))
        worksheet.write(i, 3, random.choice([18, 24]))
        worksheet.write(i, 4, random.choice([123, 456,789]))
        worksheet.write(i, 5, random.choice(['ZH44241', 'ZH42364','ZH42365','ZH42366','ZH42368','ZH42369','ZH44888']))
        worksheet.write(i, 6, random.choice(['公主岭', '肇州','长春']))
        worksheet.write(i, 7, random.choice([2, 3]))
        worksheet.write(i, 13, random.choice(['AA', 'BB','AB']))
        #暂定5个性状
        worksheet.write(i, 8, int(prepare["trail0"][i-1]))
        worksheet.write(i, 9, int(prepare["trail1"][i - 1]))
        worksheet.write(i, 10, int(prepare["trail2"][i-1]))
        worksheet.write(i, 11, int(prepare["trail3"][i - 1]))
        worksheet.write(i, 12, int(prepare["trail4"][i - 1]))
        worksheet.write(i, 14, int(prepare["trail5"][i - 1]))







    # 保存
    workbook.save('data_enrichment.xls')

    #for i in range()
data_enrichment(1000)