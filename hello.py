from flask import Flask, render_template, request
from pyecharts.charts import Bar, Line, Radar, Page
from pyecharts import options as opts
import random
from jinja2 import Markup
from load_profile import load_profile
from cal_EEI import cal_eei
from cal_her import her
from cal_PCC import pcc
from cal_GCC import gcc
from data_process import bv, cbv, not_number
from pyecharts.render import make_snapshot


import inspect

app = Flask(__name__)

'''@app.route('/')
def hello_world():
    return 'Hello!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')'''
file = "breeding.xlsx"


# file = "data_enrichment.xls"

@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/dsp_her', methods=["POST"])
# def dsp_her():  # 显示遗传力
#     # page = Page(layout=Page.DraggablePageLayout)
#     import xlrd
#     # file = "breeding.xlsx"
#     f1 = xlrd.open_workbook(file)
#     sheet1 = f1.sheet_by_name('Sheet1')
#     lst = her(file)  # 接收计算的遗传力
#     y = []
#     colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
#     for i in range(len(lst)):
#         color = "#"
#         for j in range(6):
#             color += colorArr[random.randint(0, 14)]
#
#         y.append(
#             opts.BarItem(
#                 value=lst[i],
#                 itemstyle_opts=opts.ItemStyleOpts(color=str(color)),
#                 # itemstyle_opts=opts.ItemStyleOpts(color=color[i])
#             )
#         )
#     x_ax = []
#     y_ax = []
#     start = load_profile()[0]
#     end = load_profile()[1]
#     for i in range(start, end + 1):
#         x_ax.append(sheet1.cell_value(0, i))
#     bar = Bar(init_opts=opts.InitOpts(bg_color='rgba(155,250,205,0.2)',
#                                       width="1800px",
#                                       height="800px"))
#     bar.set_colors(["#FF6347", "black"])  # FF6347
#     bar.add_xaxis(x_ax)
#     bar.add_yaxis("遗传力", y, category_gap="60%")
#     bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
#                         markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值")]))
#     # bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#     bar.set_global_opts(title_opts=opts.TitleOpts(title="显示已有数据遗传力"))
#     for i in range(sheet1.nrows - 1):
#         y_ax.append(i)
#     line = Line(init_opts=opts.InitOpts(width="1800px", height="800px"))
#     line.add_xaxis(y_ax)
#     line.add_yaxis(series_name="", y_axis=lst, label_opts=opts.LabelOpts(is_show=True))
#     # page.add(bar.overlap(line).render_embed())
#     # page.render("display.html")
#     return Markup(bar.overlap(line).render_embed())
#     #return
#     #return render_template("display.html",bar_data=bar.dump_options())
#
#     # eturn render_template(
#     #     "display.html",
#     #     bar_data=bar.dump_options()
#     # )



@app.route('/dsp_her', methods=["POST"])
def dsp_her():  # 显示遗传力
    # page = Page(layout=Page.DraggablePageLayout)
    import xlrd
    # file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    lst = her(file)  # 接收计算的遗传力
    y = []
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(lst)):
        color = "#"
        for j in range(6):
            color += colorArr[random.randint(0, 14)]

        y.append(
            opts.BarItem(
                value=lst[i],
                itemstyle_opts=opts.ItemStyleOpts(color=str(color)),
                # itemstyle_opts=opts.ItemStyleOpts(color=color[i])
            )
        )
    x_ax = []
    y_ax = []
    start = load_profile()[0]
    end = load_profile()[1]
    for i in range(start, end + 1):
        x_ax.append(sheet1.cell_value(0, i))
    bar = Bar(init_opts=opts.InitOpts(#bg_color='rgba(155,250,205,0.2)',
                                      width="1800px",
                                      height="800px"))
    bar.set_colors(["#FF6347", "black"])  # FF6347
    bar.add_xaxis(x_ax)
    bar.add_yaxis("遗传力", y, category_gap="60%")
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值")]))
    # bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="显示已有数据遗传力"))
    for i in range(sheet1.nrows - 1):
        y_ax.append(i)
    line = Line(init_opts=opts.InitOpts(width="1800px", height="800px"))
    line.add_xaxis(y_ax)
    line.add_yaxis(series_name="", y_axis=lst, label_opts=opts.LabelOpts(is_show=True))
    picture = bar.overlap(line)
    return render_template("display.html",
                           picture_options=picture.dump_options()
                           )

#mkdir /usr/local/python3





@app.route('/dsp_pcc', methods=["POST"])
def dsp_pcc():  # 显示表型相关

    import xlrd
    # file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    lst = pcc(file)[0]  # 接收计算的表型相关
    y = []
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(lst)):
        color = "#"
        for j in range(6):
            color += colorArr[random.randint(0, 14)]

        y.append(
            opts.BarItem(
                value=lst[i],
                itemstyle_opts=opts.ItemStyleOpts(color=str(color)),
                # itemstyle_opts=opts.ItemStyleOpts(color=color[i])
            )
        )
    x_ax = pcc(file)[1]
    # x_ax = [1,2,3,4,5,6,7,8,9,10]
    y_ax = []

    bar = Bar(init_opts=opts.InitOpts(#bg_color='rgba(255,250,205,0.2)',
                                      width="1800px",
                                      height="800px"))
    bar.set_colors(["#FF6347", "black"])
    bar.add_xaxis(x_ax)
    bar.add_yaxis("表型相关", y, category_gap="6    0%")
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值")]))
    # bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="显示已有数据表型相关"))
    for i in range(sheet1.nrows - 1):
        y_ax.append(i)
    line = Line(init_opts=opts.InitOpts(width="1800px", height="800px"))
    line.add_xaxis(y_ax)
    line.add_yaxis(series_name="", y_axis=lst, label_opts=opts.LabelOpts(is_show=True))
    picture = bar.overlap(line)
    return render_template("display.html",
                           picture_options=picture.dump_options()
                           )
    #return Markup(bar.overlap(line).render_embed())
    # return render_template("display.html", lst=lst)


@app.route('/dsp_gcc', methods=["POST"])
def dsp_gcc():  # 显示遗传相关

    import xlrd
    # file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    lst = gcc(file)[0]  # 接收计算的早选指数
    y = []
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(lst)):
        color = "#"
        for j in range(6):
            color += colorArr[random.randint(0, 14)]

        y.append(
            opts.BarItem(
                value=lst[i],
                itemstyle_opts=opts.ItemStyleOpts(color=str(color)),
                # itemstyle_opts=opts.ItemStyleOpts(color=color[i])
            )
        )
    x_ax = gcc(file)[1]
    y_ax = []

    bar = Bar(init_opts=opts.InitOpts(#bg_color='rgba(255,250,205,0.2)',
                                      width="1800px",
                                      height="800px"))
    bar.set_colors(["#FF6347", "black"])
    bar.add_xaxis(x_ax)
    bar.add_yaxis("遗传相关", y, category_gap="60%")
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值")]))
    # bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="显示已有数据遗传相关"))
    for i in range(sheet1.nrows - 1):
        y_ax.append(i)
    line = Line(init_opts=opts.InitOpts(width="1800px", height="800px"))
    line.add_xaxis(y_ax)
    line.add_yaxis(series_name="", y_axis=lst, label_opts=opts.LabelOpts(is_show=True))
    picture = bar.overlap(line)
    return render_template("display.html",
                           picture_options=picture.dump_options()
                           )
    #return Markup(bar.overlap(line).render_embed())
    # return render_template("display.html", lst=lst)


@app.route('/dsp_bv', methods=["POST"])
def dsp_bv():  # 显示育种值

    import xlrd
    prepare = locals()
    # file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    radar = Radar(init_opts=opts.InitOpts(width="1280px",
                                          height="720px",
                                          #bg_color='rgba(255,250,205,0.2)'
                                          )
                  )

    lst1 = bv(file)[0]  # 接收计算的给性状各公牛的育种值
    lst2 = bv(file)[1]  # 公牛编号
    lst3 = bv(file)[2]  # 性状名
    for i in range(len(lst1[0])):  # 初始化各公牛的个性状育种值列表（每个列表代表一头公牛个性状的育种值）
        prepare["blupscore" + str(i)] = []

    for i in range(len(lst2)):  # 公牛编号
        for j in range(len(lst3)):  # 性状
            prepare["blupscore" + str(i)].append(round(lst1[j][i], 4))
    scoreprint = [[] for i in range(3)]
    for i in range(len(lst2)):
        scoreprint[i].append(prepare["blupscore" + str(i)])
    # for i in range(len(lst2)):
    #     print(scoreprint[i])
    # lst3 = cbv(file)[2]
    radar.add_schema(
        schema=[
            opts.RadarIndicatorItem(name="体重", max_=10, min_=-10),
            opts.RadarIndicatorItem(name="体高", max_=10, min_=-10),
            opts.RadarIndicatorItem(name="体长", max_=10, min_=-10),
            opts.RadarIndicatorItem(name="胸围", max_=10, min_=-10),
            opts.RadarIndicatorItem(name="眼肌面积", max_=10, min_=-10)
        ],
        splitarea_opt=opts.SplitAreaOpts(
            is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
        ),
        textstyle_opts=opts.TextStyleOpts(color="black")
    )
    color = ["red", "blue", "green", "black", "purple"]
    for i in range(len(lst2)):
        radar.add(series_name=str(int(lst2[i])), data=scoreprint[i],
                  color=color[i])  # series_name的value要为str类型，否则不会显示opts.LegendOpts()效果
    # radar.add(series_name=str(lst2[0]), data=scoreprint[0], color=color[0])
    # radar.add(series_name=str(lst2[1]), data=scoreprint[1], color=color[1])
    radar.set_global_opts(title_opts=opts.TitleOpts(title="显示已有数据的各公牛的性状育种值"),
                          legend_opts=opts.LegendOpts())

    # v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    # v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    # c = (
    #     Radar()
    #         .add_schema(
    #         schema=[
    #             opts.RadarIndicatorItem(name="销售", max_=6500),
    #             opts.RadarIndicatorItem(name="管理", max_=16000),
    #             opts.RadarIndicatorItem(name="信息技术", max_=30000),
    #             opts.RadarIndicatorItem(name="客服", max_=38000),
    #             opts.RadarIndicatorItem(name="研发", max_=52000),
    #             opts.RadarIndicatorItem(name="市场", max_=25000),
    #         ]
    #     )
    #         .add("预算分配", v1)
    #         .add("实际开销", v2)
    #         .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #         .set_global_opts(
    #         legend_opts=opts.LegendOpts(selected_mode="single"),
    #         title_opts=opts.TitleOpts(title="Radar-单例模式"),
    #     ))
    # radar.render("display.html")
    picture = radar
    return render_template("display.html",
                           picture_options=picture.dump_options()
                           )
    #return Markup(radar.render_embed())


@app.route('/dsp_cbv', methods=["POST"])
def dsp_cbv():  # 显示综合育种值

    import xlrd
    # file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    lst = cbv(file)[0]  # 接收计算的早选指数
    y = []
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(lst)):
        color = "#"
        for j in range(6):
            color += colorArr[random.randint(0, 14)]

        y.append(
            opts.BarItem(
                value=lst[i],
                itemstyle_opts=opts.ItemStyleOpts(color=str(color)),
                # itemstyle_opts=opts.ItemStyleOpts(color=color[i])
            )
        )
    x_ax = cbv(file)[1]
    # y_ax = []

    bar = Bar(init_opts=opts.InitOpts(#bg_color='rgba(255,250,205,0.2)',
                                      width="1800px",
                                      height="800px"))
    bar.set_colors(["#FF6347", "black"])
    bar.add_xaxis(x_ax)
    bar.add_yaxis("综合育种值", y, category_gap="80%")
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值")]))
    # bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="显示已有数据综合育种值"))
    # for i in range(sheet1.nrows-1):
    #     y_ax.append(i)
    # line = Line(init_opts=opts.InitOpts(width="1800px", height="800px"))
    # line.add_xaxis(y_ax)
    # line.add_yaxis(series_name="", y_axis=lst, label_opts=opts.LabelOpts(is_show=True))
    picture = bar
    return render_template("display.html",
                           picture_options=picture.dump_options()
                           )
    # return Markup(bar.overlap(line).render_embed())
    #return Markup(bar.render_embed())
    # return render_template("display.html", lst=lst)


@app.route('/dsp_eei', methods=["POST"])
def dsp_eei():  # 显示早选指数

    import xlrd
    # file = "breeding.xlsx"
    f1 = xlrd.open_workbook(file)
    sheet1 = f1.sheet_by_name('Sheet1')
    lst = cal_eei(file)  # 接收计算的早选指数
    y = []
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(lst)):
        color = "#"
        for j in range(6):
            color += colorArr[random.randint(0, 14)]

        y.append(
            opts.BarItem(
                value=lst[i],
                itemstyle_opts=opts.ItemStyleOpts(color=str(color)),
                # itemstyle_opts=opts.ItemStyleOpts(color=color[i])
            )
        )
    x_ax = []
    y_ax = []
    for i in range(sheet1.nrows - 1):
        x_ax.append(i + 1)

    bar = Bar(init_opts=opts.InitOpts(#bg_color='rgba(255,250,205,0.2)',
                                      width="1800px",
                                      height="800px"))
    bar.set_colors(["#FF6347", "black"])
    bar.add_xaxis(x_ax)
    bar.add_yaxis("早选指数", y)
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                        markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="最大值")]))
    # bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="显示已有数据早选指数"))
    for i in range(sheet1.nrows - 1):
        y_ax.append(i)
    line = Line(init_opts=opts.InitOpts(width="1800px", height="800px"))
    line.add_xaxis(y_ax)
    line.add_yaxis(series_name="", y_axis=lst, label_opts=opts.LabelOpts(is_show=True))
    picture = bar.overlap(line)
    return render_template("display.html",
                           picture_options=picture.dump_options()
                           )
    #return Markup(bar.overlap(line).render_embed())
    # return render_template("display.html", lst=lst)


@app.route('/wbp', methods=["POST"])
def wbp():
    # print("loading wbp()")
    return render_template("webpage.html")


@app.route("/cal", methods=['POST'])  # 计算早选指数
def cal():
    score = 0
    denominator_gzl = 14.3
    denominator_zz = 17.1
    farm = request.form.get("farm")
    #print(farm)
    if farm != "公主岭" and farm != "肇州":
        return render_template("webpage.html",msg="请根据提示输入的合适的场次信息！")
    bw = request.form.get("bw")
    print("bw",bw)
    if bw =="" or not_number(bw):
        return render_template("webpage.html", msg="请正确输入体重信息！")
    bl = request.values.get("bl")
    if bl == "" or not_number(bl):
        return render_template("webpage.html", msg="请正确输入体长信息！")
    cw = request.values.get("cw")
    if cw == "" or not_number(cw):
        return render_template("webpage.html", msg="请正确输入胸围信息！")
    bt = request.form.get("bt")
    print("bt", bt)
    if bt == "" or not_number(bt):
        return render_template("webpage.html", msg="请正确输入体长或胸围信息！")
    ema = request.form.get("ema")
    if ema =="" and not_number(ema):
        return render_template("webpage.html", msg="请输入眼肌面积信息！")
    gene = request.form.get("gene")
    if gene != "AA" and gene != "AB" and farm != "BB":
        return render_template("webpage.html",msg="请根据提示输入的合适的基因型信息！")
    outlook = request.form.get("outlook")
    if outlook =="" and not_number(outlook):
        return render_template("webpage.html", msg="请正确输入外貌评分信息！")

    count_bw = float(bw)
    count_ema = float(ema)
    count_outlook = float(outlook)
    count_bt = float(bt)

    if farm == "公主岭":
        # if gene is "AA":
        if gene == "AA":
            score = (0.25 + (0.35 * 0.621 * count_ema) + (0.20 * 0.614 * count_bw) + (
                    0.15 * 0.423 * count_bt) + (
                             0.05 * 0.206 * count_outlook)) * 10 / denominator_gzl
        elif gene is "AB":
            score = ((0.25 * 0.5) + (0.35 * 0.621 * count_ema) + (
                    0.20 * 0.614 * count_bw) + (
                             0.15 * 0.423 * count_bt) + (
                             0.05 * 0.206 * count_outlook)) * 10 / denominator_gzl
        else:
            score = ((0.35 * count_ema) + (0.20 * 0.614 * count_bw) + (
                    0.15 * 0.423 * count_bt) + (
                             0.05 * 0.206 * count_outlook)) * 10 / denominator_gzl
    else:  # 肇州
        if gene is "AA":
            score = (0.25 + (0.35 * 0.621 * count_ema) + (0.20 * 0.614 * count_bw) + (
                    0.15 * 0.423 * count_bt) + (
                             0.05 * 0.206 * count_outlook)) * 10 / denominator_zz
        elif gene is "AB":
            score = ((0.25 * 0.5) + (0.35 * 0.621 * count_ema) + (
                    0.20 * 0.614 * count_bw) + (
                             0.15 * 0.423 * count_bt) + (
                             0.05 * 0.206 * count_outlook)) * 10 / denominator_zz
        else:
            score = ((0.35 * count_ema) + (0.20 * 0.614 * count_bw) + (
                    0.15 * 0.423 * count_bt) + (
                             0.05 * 0.206 * count_outlook)) * 10 / denominator_zz

    return render_template("webpage.html", msg="早选指数为" + str(score))


if __name__ == '__main__':
    app.run(host='0.0.0.0'
            #,debug=True
            )
