import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
st.set_page_config(layout='wide')


df = pd.read_csv('startup_cleaned_dataset.csv')
def load_investors_detail(invertor):
    st.title(invertor)
    #Most recent investment
    st.subheader('Most recent investment')
    df1 = df[df.investors.str.contains(invertor)][['date','startup','vertical','amount']].head(5)
    st.dataframe(df1)
    col1,col2 = st.columns(2)
    with col1:
        df2 = df[df.investors.str.contains(invertor)].groupby('startup').amount.sum().sort_values(ascending=False).head(5)
        st.subheader('Biggest Investments')
        st.dataframe(df2)
        fig, ax = plt.subplots()
        ax.bar(df2.index, df2.values)
        st.pyplot(fig)
    with col2:
        df3 = df[df.investors.str.contains(invertor)].groupby('vertical')['amount'].sum()
        st.subheader('Sector invested in')
        fig1, ax1 = plt.subplots()
        ax1.pie(df3, labels=df3.index,autopct='%1.01f%%')
        st.pyplot(fig1)
    col3,col4 = st.columns(2)
    with col3:
        df4 = df[df.investors.str.contains(invertor)].groupby('round')['amount'].sum()
        st.subheader('Investment in witch round')
        fig2, ax2 = plt.subplots()
        ax2.pie(df4, labels=df4.index, autopct='%1.01f%%')
        st.pyplot(fig2)
    with col4:
        df5 = df[df.investors.str.contains(invertor)].groupby('city')['amount'].sum()
        st.subheader('Investment accoding to citys')
        fig3,ax3 = plt.subplots()
        ax3.pie(df5,labels=df5.index,autopct='%1.01f%%')
        st.pyplot(fig3)
    col5,col6 = st.columns(2)
    with col5:
        df.date = pd.to_datetime(df.date, errors='coerce')
        df['year'] = df['date'].dt.year
        df6 = df[df.investors.str.contains(invertor)].groupby('year')['amount'].sum()
        st.subheader('Investment year on year')
        fig4,ax4 = plt.subplots()
        ax4.plot(df6.index,df6.values)
        st.pyplot(fig4)



st.sidebar.title('Startup Funding Analysis')
option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    st.title('Startup Analysis')
    but1 = st.sidebar.button('Find Startup Detail')
else:
    select_investors = st.sidebar.selectbox('select Invester',sorted(set(df.investors.str.split().sum())))
    st.title('Invester Analysis')
    but2 = st.sidebar.button('Find Startup Detail')
    if but2:
        load_investors_detail(select_investors)


