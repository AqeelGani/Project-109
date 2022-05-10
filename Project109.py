import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('StudentsPerformance (1).csv')
performance = df["math score"] + df["reading score"] + df["writing score"].tolist()

mean = statistics.mean(performance)
median = statistics.median(performance)
mode = statistics.mode(performance)
stdev = statistics.stdev(performance)

zone1_start, zone1_end = mean - stdev, mean + stdev
zone2_start, zone2_end = mean - 2*stdev, mean + 2*stdev
zone3_start, zone3_end = mean - 3*stdev, mean + 3*stdev

fig = ff.create_distplot([performance],["Students'Performance"],show_hist=False)
fig.add_trace(go.Scatter( x = [mean, mean], y = [0,0.17], mode = 'lines', name = "Mean"))
fig.add_trace(go.Scatter( x = [zone1_start, zone1_start], y = [0,0.16], mode = 'lines', name = "Zone - 1"))
fig.add_trace(go.Scatter( x = [zone1_end, zone1_end], y = [0,0.16], mode = 'lines', name = "Zone + 1"))
fig.add_trace(go.Scatter( x = [zone2_start, zone2_start], y = [0,0.16], mode = 'lines', name = "Zone - 2"))
fig.add_trace(go.Scatter( x = [zone2_end, zone2_end], y = [0,0.16], mode = 'lines', name = "Zone + 2"))
fig.add_trace(go.Scatter( x = [zone3_start, zone3_start], y = [0,0.16], mode = 'lines', name = "Zone - 3"))
fig.add_trace(go.Scatter( x = [zone3_end, zone3_end], y = [0,0.16], mode = 'lines', name = "Zone + 3"))
fig.show()

zone1_list = [result for result in performance if result > zone1_start and result < zone1_end]
zone2_list = [result for result in performance if result > zone2_start and result < zone2_end]
zone3_list = [result for result in performance if result > zone3_start and result < zone3_end]
print('{}% Of Data Lies In 1 Standard Deviation'.format(len(zone1_list)/len(performance)*100))
print('{}% Of Data Lies In 2 Standard Deviation'.format(len(zone2_list)/len(performance)*100))
print('{}% Of Data Lies In 3 Standard Deviation'.format(len(zone3_list)/len(performance)*100))
