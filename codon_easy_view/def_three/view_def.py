import numpy
import pygal
import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot
def view_single(dict):
    each_one = []
    each_one_name = []

    for key,value in dict.items():
        for K,V in value.items():
            each_one.append(V[1])
            each_one_name.append(K)

    trace_basic = [go.Bar(
        x=each_one_name,
        y=each_one,
    )]

    # Layout
    layout_basic = go.Layout(
        title='Single Codon Distribution')

    # Figure
    figure_basic = go.Figure(data=trace_basic, layout=layout_basic)

    # Plot
    pyplt(figure_basic, filename='picture/single.html')

    n = 'single'
    showtrend(each_one, n)


def view_double(dict):
    each_one_pair = []
    each_one_name_pair = []
    for key,value in dict.items():
        #print(key)
        for K,V in value.items():
            each_one_pair.append(V[0])
            each_one_name_pair.append(K)

    trace_basic = [go.Bar(
        x=each_one_name_pair,
        y=each_one_pair,
    )]

    # Layout
    layout_basic = go.Layout(
        title='Codon Pair Distribution')

    # Figure
    figure_basic = go.Figure(data=trace_basic, layout=layout_basic)

    # Plot
    pyplt(figure_basic, filename='picture/double.html')

    n = 'double'
    showtrend(each_one_pair, n)




def showtrend(x,n):
    data = [go.Histogram(x=x, histnorm='probability')]
    pyplt(data, filename='picture/'+n+'(probability).html')
    #
    data2 = [go.Histogram(x=x)]
    pyplt(data2, filename='picture/'+n+'_histogram.html')
    #
    data3 = [go.Histogram(x=x, cumulative=dict(enabled=True))]
    pyplt(data3, filename='picture/'+n+'_histogram(cumulative).html')





