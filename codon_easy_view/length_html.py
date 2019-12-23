#长度检测可视化模块
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot



f = open('show_result/lenth','r')
a = f.read()
lenth_data = eval(a)
f.close()

f1 = open('show_result/name','r')
b = f1.read()
name_data = eval(b)
f1.close()

# Trace
trace_basic = [go.Bar(
            x = name_data,
            y = lenth_data,
    )]

# Layout
layout_basic = go.Layout(
            title = 'Pep Length Distribution',
            #xaxis = go.layout.XAxis(range = [-0.5,4.5], domain = [0,1])
    )

# Figure
figure_basic = go.Figure(data = trace_basic, layout = layout_basic)

# Plot
pyplt(figure_basic, filename='show_result/lenth.html')






data = [go.Histogram(x=lenth_data,
                       histnorm = 'probability')]
# y = x 水平直方图，histnorm='probability' y轴显示概率，没有则显示数目
pyplt(data, filename='show_result/lenth_histogram(probability).html')


data2 = [go.Histogram(x=lenth_data)]
# y = x 水平直方图，histnorm='probability' y轴显示概率，没有则显示数目
pyplt(data2, filename='show_result/lenth_histogram.html')

data3 = [go.Histogram(x=lenth_data,
                      cumulative=dict(enabled=True))]
pyplt(data3, filename='show_result/lenth_histogram(cumulative).html')
