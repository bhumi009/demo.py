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
  st.image("./dubai.jpg",caption="Dubai",width=300,use_column_width=True)
  st.write("dubai is a desert place")
col3=st.columns(1)  
with col3:
  st.subheader("Doreamon")
  st.video("https://www.youtube.com/watch?v=Ve_Sq9j2VZU&pp=ygUXZG9yZWFtb24gdmlkZW9zIGluIHNub3c%3D",width=300,use_column_width=True)
  st.write("Doraemon is a Japanese manga series written and illustrated by Fujiko F. Fujio.")
  
