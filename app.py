import streamlit as st
import pandas as pd
import altair as alt

# Function to plot and compare histograms for two subjects from two datasets
def plot_comparison_histograms(df1, df2):
    subjects1 = df1['구   분'].dropna().unique()
    subjects2 = df2['구   분'].dropna().unique()
    
    # Ensure both datasets have the same subjects to compare
    common_subjects = set(subjects1).intersection(subjects2)
    
    # Define a list of colors for different subjects
    colors = ['#4e79a7', '#f28e2c', '#e15759', '#76b7b2', '#59a14f', '#edc949', '#af7aa1', '#ff9da7', '#9c755f']
    
    # Create columns to hold 2 charts per row for comparison
    cols = st.columns(2)
    
    for idx, subject in enumerate(common_subjects):
        # Filter the data for the current subject in both datasets
        subject_data1 = df1[df1['구   분'] == subject].iloc[0, 3:12]
        subject_data2 = df2[df2['구   분'] == subject].iloc[0, 3:12]
        
        grades1 = subject_data1.index
        students1 = subject_data1.values
        
        grades2 = subject_data2.index
        students2 = subject_data2.values

        # Prepare data for the bar chart
        chart_data1 = pd.DataFrame({
            'Grades': grades1,
            'Number of Students': students1
        })

        chart_data2 = pd.DataFrame({
            'Grades': grades2,
            'Number of Students': students2
        })

        # Create Altair bar charts for both datasets
        chart1 = alt.Chart(chart_data1).mark_bar().encode(
            x=alt.X('Grades', sort=None),
            y='Number of Students',
            color=alt.value(colors[idx % len(colors)])  # Custom color for each subject
        ).properties(
            width=300,  # Set chart width
            height=300  # Set chart height
        )

        chart2 = alt.Chart(chart_data2).mark_bar().encode(
            x=alt.X('Grades', sort=None),
            y='Number of Students',
            color=alt.value(colors[(idx+1) % len(colors)])  # Custom color for each subject
        ).properties(
            width=300,  # Set chart width
            height=300  # Set chart height
        )

        # Display the charts side by side for comparison
        cols[0].subheader(f'{subject} - File 1')
        cols[0].altair_chart(chart1)
        
        cols[1].subheader(f'{subject} - File 2')
        cols[1].altair_chart(chart2)

        # Start a new row every 2 subjects
        if (idx + 1) % 2 == 0:
            cols = st.columns(2)

# Streamlit app
st.title("두 파일의 모의고사 등급별 인원수 분포 비교")

# Display the instruction message
st.markdown("**UNIV 데이터를 다운 받고 csv 확장자로 파일을 변환해주세요. 두 개의 파일을 업로드하고 비교하세요.**")

# File uploader for two files
uploaded_file1 = st.file_uploader("CSV 파일 1을 업로드하세요", type=["csv"], key='file1')
uploaded_file2 = st.file_uploader("CSV 파일 2을 업로드하세요", type=["csv"], key='file2')

if uploaded_file1 and uploaded_file2:
    # Load the uploaded CSV files
    df1 = pd.read_csv(uploaded_file1)
    df2 = pd.read_csv(uploaded_file2)
    
    # Plot and compare histograms for each subject
    plot_comparison_histograms(df1, df2)
