
import streamlit as st
import pandas as pd
data = pd.read_csv(r"C:\Users\KonaSowjanya\Desktop\Python\data_sets\GDP_Data.csv")
st.title("GDP analysis of the country")
#st.write("e-commerce data analysis")
st.markdown("GDP_Data analysis of country using streamlit,pandas")
name = st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name
if name != '':
    st.write("Your name is ",name)
if st.button("click me to show visualization"):
    st.bar_chart(data,x='BirthRate',y='IncomeGroup')
date = st.date_input("Pick a date",value=None)
if date != None:
    st.write("You have selected the",date)
x = st.slider('x')  #  this is a widget
st.write(x, 'squared is', x * x)
cat  = st.radio('Select which attribute you want see',data.columns,index=2)
if cat !='':
    st.line_chart(data[cat])
