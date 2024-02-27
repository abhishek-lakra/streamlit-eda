import os
import glob
import shutil
import configparser
import pandas as pd
import streamlit as st
from random import randint
import plotly.express as px
from utils.style import Style

config = configparser.ConfigParser()
config.read('/app/config.ini')

FILE_DIR = config.get('PATH', 'FILE_DIR')

Style()

def save_uploaded_file(uploaded_file, file_name):
    try:
        with open(os.path.join(FILE_DIR, file_name), "wb") as f:
            shutil.copyfileobj(uploaded_file, f)
        return True
    except:
        return False


if __name__ == "__main__":    
    with st.sidebar:
        file = st.file_uploader(label="Upload your file", type=['csv', 'xlsx'])
        
        if not file:
            file_list = glob.glob(os.path.join(FILE_DIR, "*"))
            for file_path in file_list:
                os.remove(file_path)
                st.session_state.clear()
        
        elif file and 'file' not in st.session_state:
            download_response = save_uploaded_file(uploaded_file=file, file_name=file.name)
            if download_response:
                st.toast(f"Files uploaded successfully!", icon="✅")
                st.session_state.file = True
            else:
                st.toast(f"Files upload failed! Please try again", icon="❌")
                
                
    
    file_list = glob.glob(os.path.join(FILE_DIR, "*"))  
    if len(file_list) == 0:
        st.error("🔒 Kindly upload file for EDA")
    else:
        tab1, tab2, tab3, tab4 = st.tabs(['Table', 'Bar Graph', 'Area Graph', 'Pie Chart'])
        
        if file_list[0].endswith('.csv'):
            df = pd.read_csv(file_list[0])
        else:
            df = pd.read_excel(file_list[0])
        
        
        with tab1:
            t1_df = df.copy()         
            st.dataframe(t1_df, use_container_width=True, hide_index=True)
        
        with tab2:
            t2_df = df.copy()
            
            t2_col1, t2_col2, t2_col3, t2_col4 = st.columns(4)
            
            t2_X = t2_col1.selectbox(label='X-axis', options=df.columns.tolist(), key='T2C1')
            t2_Y = t2_col2.selectbox(label='Y-axis', options=df.columns.tolist(), key='T2C2')
            t2_color = t2_col3.selectbox(label='Color', options=[None] + df.columns.tolist(), key='T2C3')
            t2_metric = t2_col4.selectbox(label='Metric', options=[None, 'Mean', 'Median', 'Sum', 'Min', 'Max', 'Count', 'Size', 'First', 'Last'], key='T2C4')
            
            if t2_metric:
                if t2_color:
                    t2_df = t2_df.groupby(t2_X, as_index=False).agg({t2_Y: str(t2_metric).lower(), t2_color: lambda x: x.value_counts().index[0]})
                else:
                    t2_df = t2_df.groupby(t2_X, as_index=False).agg({t2_Y: str(t2_metric).lower()})
                if t2_metric == 'Size':
                    t2_df.rename(columns={'size': t2_Y}, inplace=True)
            
            if t2_X and t2_Y:
                if t2_X and t2_Y and t2_color:
                    st.bar_chart(data=t2_df, x=t2_X, y=t2_Y, color=t2_color, use_container_width=True)
                else:
                    st.bar_chart(data=t2_df, x=t2_X, y=t2_Y, use_container_width=True)
            else:
                st.error('⚠️ Kindly select X-axis and Y-axis')
                    
        with tab3:
            t3_df = df.copy()
            
            t3_col1, t3_col2, t3_col3, t3_col4 = st.columns(4)
            
            t3_X = t3_col1.selectbox(label='X-axis', options=df.columns.tolist(), key='T3C1')
            t3_Y = t3_col2.selectbox(label='Y-axis', options=df.columns.tolist(), key='T3C2')
            t3_color = t3_col3.selectbox(label='Color', options=[None] + df.columns.tolist(), key='T3C3')
            t3_metric = t3_col4.selectbox(label='Metric', options=[None, 'Mean', 'Median', 'Sum', 'Min', 'Max', 'Count', 'Size', 'First', 'Last'], key='T3C4')
            
            if t3_metric:
                if t3_color:
                    t3_df = t3_df.groupby(t3_X, as_index=False).agg({t3_Y: str(t3_metric).lower(), t3_color: lambda x: x.value_counts().index[0]})
                else:
                    t3_df = t3_df.groupby(t3_X, as_index=False).agg({t3_Y: str(t3_metric).lower()})
                if t3_metric == 'Size':
                    t3_df.rename(columns={'size': t3_Y}, inplace=True)
            
            if t3_X and t3_Y:
                if t3_X and t3_Y and t3_color:
                    st.area_chart(data=t3_df, x=t3_X, y=t3_Y, color=t3_color, use_container_width=True)
                else:
                    st.area_chart(data=t3_df, x=t3_X, y=t3_Y, use_container_width=True)
            else:
                st.error('⚠️ Kindly select X-axis and Y-axis')
                
        with tab4:
            t4_df = df.copy()
            
            t4_col1, t4_col2, t4_col3, t4_col4 = st.columns(4)
            
            t4_value = t4_col1.selectbox(label='Value', options=df.columns.tolist(), key='T4C1')
            t4_name = t4_col2.selectbox(label='Name', options=df.columns.tolist(), key='T4C2')
            t4_metric = t4_col3.selectbox(label='Metric', options=[None, 'Mean', 'Median', 'Sum', 'Min', 'Max', 'Count', 'Size', 'First', 'Last'], key='T4C3')
            t4_hole = t4_col4.slider(label='Hole', min_value=0.0, max_value=1.0, value=0.0, key='T4C4')
            
            if t4_metric:
                t4_df = t4_df.groupby(t4_name, as_index=False).agg({t4_value: str(t4_metric).lower()})
                if t4_metric == 'Size':
                    t4_df.rename(columns={'size': t4_value}, inplace=True)
            
            if t4_name and t4_value:
                fig = px.pie(data_frame=t4_df, names=t4_name, values=t4_value, hole=t4_hole)
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            else:
                st.error('⚠️ Kindly select Name and Value')