# plot the chart from google sheet
import pandas as pd 
import plotly.graph_objects as go



def get_sheet(id,name):
    sheet= "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(id, name)
    global df
    df= pd.read_csv(sheet)
    return df.columns.values


def plot_chart(x_axis, y_axis):
    fig = go.Figure([go.Bar(x=df[x_axis] ,y=df[y_axis])])
    fig.update_traces(marker_color='lightslategray', marker_line_color='black',marker_line_width=1, opacity=0.5)
    fig.update_layout(xaxis=dict(  title=x_axis, titlefont_size=16, tickfont_size=14 ), yaxis=dict(  title=y_axis, titlefont_size=16, tickfont_size=14 ))


    return fig
