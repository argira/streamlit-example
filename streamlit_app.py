from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import openpyxl

@st.cache
def app():
    st.header("Analysis of SAIF Corporation Positioning in the Northern Private Ownership Market")
    df = pd.read_excel('Marketing Analyst- Interview exercise.xlsx')
    #filter data to only consider private ownership
    df = df[df['Ownership']==50]

    def market_research(df):
        colA,colB,colC = st.columns(3)
        with colA:
            market_share = df.groupby(['SAIF'])['Employer Number'].count().reset_index()
            market_share = market_share['Employer Number'][0]/market_share['Employer Number'].sum()*100
            
