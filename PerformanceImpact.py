import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analysis of the Impact of Online Learning on Student Performance During COVID-19")

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/refs/heads/main/ONLINE%20EDUCATION%20SYSTEM%20REVIEW.csv"

# Read the dataset
df = pd.read_csv(url)

# Mapping traditional marks to 1–10 scale
traditional_mapping = {
    '1-10': 1, '11-20': 2, '21-30': 3, '31-40': 4, '41-50': 5,
    '51-60': 6, '61-70': 7, '71-80': 8, '81-90': 9, '91-100': 10
}
df['Traditional_Score'] = df['Average marks scored before pandemic in traditional classroom'].map(traditional_mapping)

# Dropdown to select Level of Education
education_option = st.selectbox(
    "Select Level of Education",
    df['Level of Education'].unique()
)

# Filter dataframe based on selection
df_filtered = df[df['Level of Education'] == education_option]

# Count frequency of each score (before vs after)
before_counts = df_filtered['Traditional_Score'].value_counts().sort_index()
after_counts = df_filtered['Performance in online'].value_counts().sort_index()

# Combine into a DataFrame
compare_df = pd.DataFrame({
    'Score': range(1, 11),
    'Before COVID-19': before_counts.reindex(range(1, 11), fill_value=0),
    'During COVID-19': after_counts.reindex(range(1, 11), fill_value=0)
})

# Melt for line chart
compare_melted = compare_df.melt(id_vars='Score', value_vars=['Before COVID-19','During COVID-19'], 
                                 var_name='Period', value_name='Number of Students')

# Create line chart
fig = px.line(
    compare_melted,
    x='Score',
    y='Number of Students',
    color='Period',
    markers=True,
    title=f'Student Performance: {education_option} Level',
    labels={'Score':'Performance Score'}
)

st.plotly_chart(fig)
