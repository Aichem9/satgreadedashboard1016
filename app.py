import streamlit as st
import pandas as pd

# Function to plot histograms for each subject using Streamlit's bar chart
def plot_histograms(df):
    subjects = df['구   분'].dropna().unique()
    
    for subject in subjects:
        # Filter the data for the current subject
        subject_data = df[df['구   분'] == subject].iloc[0, 3:12]
        grades = subject_data.index
        students = subject_data.values
        
        # Prepare data for the bar chart
        chart_data = pd.DataFrame({
            'Grades': grades,
            'Number of Students': students
        })

        st.subheader(f'{subject} - Grade Distribution')
        st.bar_chart(chart_data.set_index('Grades'))

# Streamlit app
st.title("모의고사 등급별 인원수 분포")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Load the uploaded file
    df = pd.read_excel(uploaded_file)
    
    # Plot histograms for each subject
    plot_histograms(df)
