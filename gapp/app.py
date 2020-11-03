import streamlit as st
import plot
import SessionState


# text inputs to get sheet id and sheet name from user
# default values of sheet_id and sheet name is provided  for demo
id = st.text_input(label='Google Sheet id', value='1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc')
name = st.text_input(label='Sheet Name', value='Sheet1')



#session state varible to save session state 
#as streamlit reloads the app when button is placed inside button so not to reload on every input sessionstate is used
# official issue : https://discuss.streamlit.io/t/the-button-inside-a-button-seems-to-reset-the-whole-app-why/1051/10
session_state = SessionState.get(name="", columns=False)
columns = st.button('columns')

# if columns button is pressed session state is true
if columns:
        session_state.columns = True

if session_state.columns:
        '''
        column_names: returns column names of sheet from plot function
        col1 & col2 : align x_axis and y_axis selection list side by side
        plt : button to plot the chart
        if plt pressed calls fun from plot.py which returns chart
        and plot it with st.plotly_chart_fn
        '''
        column_names = plot.get_sheet(id, name)
        col1, col2 = st.beta_columns([0.5,0.5])
        with col1:
                x_axis = st.selectbox('X axis:', column_names)
        with col2:
                y_axis =st.selectbox('Y axis:', column_names)

        plt = st.button('Plot')

        if plt:
                chart = plot.plot_chart(x_axis, y_axis)
                st.plotly_chart(chart, use_container_width=True)







