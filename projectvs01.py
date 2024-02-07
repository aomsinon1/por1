import streamlit as st
import pandas as pd

st.image('https://www.tqm.co.th/articles/%E0%B8%AB%E0%B8%A1%E0%B8%B5%E0%B8%A3%E0%B8%AD%E0%B8%9A%E0%B8%A3%E0%B8%B9%E0%B9%89%E0%B9%80%E0%B8%A3%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%87%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%A3%E0%B8%96/%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B8%82%E0%B9%88%E0%B8%B2%E0%B8%A7%E0%B8%AD%E0%B8%B8%E0%B8%9A%E0%B8%B1%E0%B8%95%E0%B8%B4%E0%B9%80%E0%B8%AB%E0%B8%95%E0%B8%B8%E0%B8%A3%E0%B8%96%E0%B8%8A%E0%B8%99%E0%B8%9D%E0%B8%99%E0%B8%95%E0%B8%81%E0%B8%96%E0%B8%99%E0%B8%99%E0%B8%A5%E0%B8%B7%E0%B9%88%E0%B8%99')
st.header("การนําเสนอสถิติการเกิดอุบัติเหตุของประเทศไทย")

coll,col2=st.columns(2)

with coll:
    st.subheader("จํานวนผู้เสียชีวิต")
    st.write("2,5600")
with col2:
    st.subheader("จํานวนผู้เสียชีวิต")
    st.write("2, 5600")
