import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot histograms for each subject
def plot_histograms(df):
    subjects = df['구   분'].dropna().unique()
    
    for subject in subjects:
        # Filter the data for the current subject
        subject_data = df[df['구   분'] == subject].iloc[0, 3:12]
        grades = subject_data.index
        students = subject_data.values
        
        # Plot the histogram for the current subject
        plt.figure(figsize=(8, 6))
        plt.bar(grades, students)
        plt.title(f'{subject} - Grade Distribution')
        plt.xlabel('Grades')
        plt.ylabel('Number of Students')
        st.pyplot(plt)

# Streamlit app
st.title("모의고사 등급별 인원수 분포")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    # Load the uploaded file
    df = pd.read_excel(uploaded_file)
    
    # Plot histograms for each subject
    plot_histograms(df)
