import streamlit as st
import pandas as pd
import altair as alt

# Function to plot histograms for each subject using Altair for better customization
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

        # Create an Altair bar chart
        chart = alt.Chart(chart_data).mark_bar().encode(
            x=alt.X('Grades', sort=None),
            y='Number of Students',
            color=alt.value('#4e79a7')  # Custom color
        ).properties(
            width=400,  # Set chart width
            height=400  # Set chart height
        )
        
        st.altair_chart(chart)

# Streamlit app
st.title("모의고사 등급별 인원수 분포")

# File uploader
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file:
    # Load the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    
    # Plot histograms for each subject
    plot_histograms(df)
