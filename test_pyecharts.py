from pyecharts.charts import Bar
from pyecharts import options as opts
'''
# V1 版本开始支持链式调用
bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render()'''
'''
# 不习惯链式调用的开发者依旧可以单独调用方法
bar = Bar()
bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
bar.render()'''
columns = ["1","2","3","4","5","6","7","8","9","10"]
data1 = ["10","20","30","40","50","60","70","80","90","100"]

bar = Bar()
bar.add_xaxis(columns)
bar.add_yaxis("育种指数",data1)
bar.set_global_opts(title_opts=opts.TitleOpts("排名前十早选指数"))
#bar.add("早选指数",columns,data1,mark_line=["average"],mark_point=["max","min"])
bar.render()