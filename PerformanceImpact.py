import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analysis of the Impact of Online Learning on Student Performance During COVID-19")

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/refs/heads/main/ONLINE%20EDUCATION%20SYSTEM%20REVIEW.csv"

# Read the dataset
df = pd.read_csv(url)

# Mapping for traditional scores
traditional_mapping = {
    '1-10': 1, '11-20': 2, '21-30': 3, '31-40': 4, '41-50': 5,
    '51-60': 6, '61-70': 7, '71-80': 8, '81-90': 9, '91-100': 10
}
df['Traditional_Score'] = df['Average marks scored before pandemic in traditional classroom'].map(traditional_mapping)

# Dropdown for graph selection
option = st.selectbox(
    "Select Graph to Display",
    ("Overall Performance Before vs During", "Performance by Education Level", "Elderly Supervision Impact")
)

if option == "Overall Performance Before vs During":
    # Prepare overall counts
    before_counts = df['Traditional_Score'].value_counts().sort_index()
    after_counts = df['Performance in online'].value_counts().sort_index()
    compare_df = pd.DataFrame({
        'Score': range(1, 11),
        'Before COVID-19': before_counts.reindex(range(1, 11), fill_value=0),
        'During COVID-19': after_counts.reindex(range(1, 11), fill_value=0)
    })
    compare_melted = compare_df.melt(id_vars='Score', value_vars=['Before COVID-19','During COVID-19'])
    
    fig = px.line(compare_melted, x='Score', y='value', color='variable', markers=True,
                  title='Overall Student Performance: Before vs During Online Learning',
                  labels={'Score':'Performance Score','value':'Number of Students','variable':'Period'})
    st.plotly_chart(fig)

elif option == "Performance by Education Level":
    # Aggregate by education level
    before_counts = df.groupby(['Level of Education','Traditional_Score']).size().reset_index(name='Before COVID-19')
    after_counts = df.groupby(['Level of Education','Performance in online']).size().reset_index(name='During COVID-19')
    after_counts.rename(columns={'Performance in online':'Traditional_Score'}, inplace=True)
    compare_df = pd.merge(before_counts, after_counts, on=['Level of Education','Traditional_Score'], how='outer').fillna(0)
    compare_melted = compare_df.melt(id_vars=['Level of Education','Traditional_Score'], value_vars=['Before COVID-19','During COVID-19'],
                                     var_name='Period', value_name='Count')
    
    fig = px.line(compare_melted, x='Traditional_Score', y='Count', color='Level of Education', line_dash='Period', markers=True,
                  title='Student Performance Distribution by Education Level',
                  labels={'Traditional_Score':'Performance Score','Count':'Number of Students','Level of Education':'Education Level','Period':'Period'})
    st.plotly_chart(fig)

elif option == "Elderly Supervision Impact":
    fig = px.box(df, x='Do elderly people monitor you?', y='Performance in online',
                 color='Do elderly people monitor you?',
                 color_discrete_map={'Yes':'#1f77b4','No':'#d62728'},
                 points='all',
                 title='Impact of Elderly Supervision on Online Performance',
                 labels={'Do elderly people monitor you?':'Elderly Supervision','Performance in online':'Online Performance Score'})
    st.plotly_chart(fig)
