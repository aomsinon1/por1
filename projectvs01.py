import streamlit as st
import pandas as pd

st.image('./img/1.jpg')
st.header("การนําเสนอสถิติการเกิดอุบัติเหตุของประเทศไทย")

coll,col2=st.columns(2)

with coll:
    st.subheader("จํานวนผู้เสียชีวิต")
    st.write("2,5600")
with col2:
    st.subheader("จํานวนผู้เสียชีวิต")
    st.write("2, 5600")

dt=pd.read_excel('data//content/DT01.xlsx')

#st.write()

NumM=dt[dt['Sex']=='ชาย'].count()
NumF=dt[dt['Sex']=='หญิง'].count()

dtSex=[NumM, NumF]
dtSexd=pd.DataFrame(dtSex)
st.bar_chart(dtSexd)