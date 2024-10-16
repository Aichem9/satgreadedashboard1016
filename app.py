import streamlit as st
import pandas as pd
import altair as alt

# Function to plot histograms for each subject using Altair and display them in a 3-column layout
def plot_histograms(df):
    subjects = df['구   분'].dropna().unique()
    
    # Create columns to hold 3 charts per row
    cols = st.columns(3)
    col_index = 0

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

        # Create an Altair bar chart
        chart = alt.Chart(chart_data).mark_bar().encode(
            x=alt.X('Grades', sort=None),
            y='Number of Students',
            color=alt.value('#4e79a7')  # Custom color
        ).properties(
            width=150,  # Set chart width
            height=150  # Set chart height
        )

        # Display the chart in the respective column
        cols[col_index].subheader(f'{subject}')
        cols[col_index].altair_chart(chart)
        
        # Move to the next column
        col_index += 1
        
        # Reset columns after every 3 subjects
        if col_index >= 3:
            col_index = 0
            cols = st.columns(3)

# Streamlit app
st.title("모의고사 등급별 인원수 분포")

# File uploader
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file:
    # Load the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    
    # Plot histograms for each subject
    plot_histograms(df)
