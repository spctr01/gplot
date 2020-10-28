import streamlit as st
import plot
import SessionState



id = st.text_input(label='Google Sheet id', value='1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc')
name = st.text_input(label='Sheet Name', value='Sheet1')




session_state = SessionState.get(name="", columns=False)
columns = st.button('columns')
 
if columns:
        session_state.columns = True

if session_state.columns:

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







