import streamlit as st
st.set_page_config(page_title='Places')
st.header("Tourism Places")

col1,col2=st.columns(2)
with col1:
  st.subheader("Simla")
  st.image("./simla.jpg",caption="Simla",width=300,use_column_width=True)
  st.write("simla is cool place")
with col2:
  st.subheader("Dubai")
  st.image("./dubai.jpg",caption="Dubai",width=300,use_column_width=True,height=400,use_column_height=True)
  st.write("dubai is a desert place")

