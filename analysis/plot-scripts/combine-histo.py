import pandas as pd
from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.layouts import row
from bokeh.io import output_notebook
from bokeh.io import export_png
from bokeh.models import NumeralTickFormatter
from bokeh.models.tickers import SingleIntervalTicker
import numpy as np

# Read the CSV files
cores = ['111233', '111234', '112344', '123']
payload = ['128B', '1KB', '10KB', '100KB', '500KB']
base_path = '/home/lucian/simple-chain-ws/graphs'
base_name = ['1-ste', '1-mte', 'n-ste', 'n-mte-per-1-node', 'n-mte-per-2-node']
pl = payload[3]

# for pl in payload:
df1 = pd.read_csv(f'{base_path}/{base_name[0]}-{pl}/resp-time-{base_name[0]}-{pl}.csv')
df2 = pd.read_csv(f'{base_path}/{base_name[1]}-{pl}/resp-time-{base_name[1]}-{pl}.csv')
df3 = pd.read_csv(f'{base_path}/{base_name[2]}-{pl}-{cores[0]}/resp-time-{base_name[2]}-{pl}-{cores[0]}.csv')
df4 = pd.read_csv(f'{base_path}/{base_name[2]}-{pl}-{cores[1]}/resp-time-{base_name[2]}-{pl}-{cores[1]}.csv')
df5 = pd.read_csv(f'{base_path}/{base_name[2]}-{pl}-{cores[2]}/resp-time-{base_name[2]}-{pl}-{cores[2]}.csv')
df6 = pd.read_csv(f'{base_path}/{base_name[3]}-{pl}-{cores[0]}/resp-time-{base_name[3]}-{pl}-{cores[0]}.csv')
df7 = pd.read_csv(f'{base_path}/{base_name[3]}-{pl}-{cores[1]}/resp-time-{base_name[3]}-{pl}-{cores[1]}.csv')
df8 = pd.read_csv(f'{base_path}/{base_name[3]}-{pl}-{cores[2]}/resp-time-{base_name[3]}-{pl}-{cores[2]}.csv')
df9 = pd.read_csv(f'{base_path}/{base_name[4]}-{pl}-{cores[3]}/resp-time-{base_name[4]}-{pl}-{cores[3]}.csv')

# Assume the response time columns are named 'response_time' in each CSV
data1 = df1['response_time'] / 1_000_000
data2 = df2['response_time'] / 1_000_000
data3 = df3['response_time'] / 1_000_000
data4 = df4['response_time'] / 1_000_000
data5 = df5['response_time'] / 1_000_000
data6 = df6['response_time'] / 1_000_000
data7 = df7['response_time'] / 1_000_000
data8 = df8['response_time'] / 1_000_000
data9 = df9['response_time'] / 1_000_000

# Create a new figure
p = figure(title=f"Response times: payload size {pl}, different executors and cores", \
            sizing_mode="stretch_width", max_width=800, height=400)

# Create a histogram for each set of data
hist, edges = np.histogram(data1, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="red", line_color="white", alpha=0.5, legend_label=f"{base_name[0]}")

hist, edges = np.histogram(data2, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="green", line_color="white", alpha=0.5, legend_label=f"{base_name[1]}")

hist, edges = np.histogram(data3, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="blue", line_color="white", alpha=0.5, legend_label=f"{base_name[2]}-{cores[0]}")

hist, edges = np.histogram(data4, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="brown", line_color="white", alpha=0.5, legend_label=f"{base_name[2]}-{cores[1]}")

hist, edges = np.histogram(data5, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="black", line_color="white", alpha=0.5, legend_label=f"{base_name[2]}-{cores[2]}")

hist, edges = np.histogram(data6, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="gray", line_color="white", alpha=0.5, legend_label=f"{base_name[3]}-{cores[0]}")

hist, edges = np.histogram(data7, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="pink", line_color="white", alpha=0.5, legend_label=f"{base_name[3]}-{cores[1]}")

hist, edges = np.histogram(data8, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="purple", line_color="white", alpha=0.5, legend_label=f"{base_name[3]}-{cores[2]}")

hist, edges = np.histogram(data9, bins=20)
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color="orange", line_color="white", alpha=0.5, legend_label=f"{base_name[4]}")

# Customize the plot
p.legend.location = "top_right"
p.legend.title = "Settings"
p.xaxis.axis_label = 'Response Time'
p.yaxis.axis_label = 'Number of samples'
p.xaxis[0].formatter = NumeralTickFormatter(format="0,0.00")
ticker = SingleIntervalTicker(interval=0.5)
p.xaxis.ticker = ticker

export_png(p, filename = f"comb-histo-{pl}-alt-execs-cores.png")