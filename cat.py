import streamlit as st
st.set_page_config(page_title='cats')
st.header("Types of cats")

col1,col2=st.columns(2)
with col1:
st.subheader("persian cat")
st.image("./cat1.jpg",caption="persian cat",width=300,use_column_width=True)
st.write("Persian cats are cute")
with col2:
st.subheader("Ragdoll cat")
st.image("./cat2.jpg",caption="Regdoll cat",width=300,use_column_width=True)
st.write("Regdolls cats are proud")
