import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analysis of Students’ Satisfaction with Online Learning During COVID-19")

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/refs/heads/main/ONLINE%20EDUCATION%20SYSTEM%20REVIEW.csv"

# Read the dataset
df = pd.read_csv(url)

# Map satisfaction levels to numerical values
satisfaction_mapping = {'Bad': 1, 'Average': 2, 'Good': 3}
df['Satisfaction_Score'] = df['Your level of satisfaction in Online Education'].map(satisfaction_mapping)

# Group and calculate average satisfaction score per internet quality
avg_satisfaction_by_internet = df.groupby(
    'Internet facility in your locality'
)['Satisfaction_Score'].mean().reset_index()

# Map internet facility labels
internet_labels = {1: 'Very Poor', 2: 'Poor', 3: 'Average', 4: 'Good', 5: 'Excellent'}
avg_satisfaction_by_internet['Internet Facility'] = avg_satisfaction_by_internet[
    'Internet facility in your locality'
].map(internet_labels)

# Plot bar chart (BLUE → GREY → RED continuous palette)
fig = px.bar(
    avg_satisfaction_by_internet,
    x='Internet Facility',
    y='Satisfaction_Score',
    title='Average Online Education Satisfaction by Internet Facility',
    labels={
        'Internet Facility': 'Internet Facility Quality',
        'Satisfaction_Score': 'Average Satisfaction'
    },
    color='Satisfaction_Score',
    color_continuous_scale='RdBu_r'  # Reverse to get Blue=Good, Red=Bad
)

# Keep proper order
fig.update_layout(
    xaxis={
        'categoryorder': 'array',
        'categoryarray': [internet_labels[i] for i in sorted(internet_labels)]
    },
    width=800,
    height=500,
    coloraxis_colorbar=dict(title="Satisfaction Score"),
)

# Add legend explanation
fig.add_annotation(
    text="Scale: Red = Bad, Grey = Average, Blue = Good",
    xref="paper", yref="paper",
    x=0, y=-0.2,
    showarrow=False,
    font=dict(size=10)
)

st.plotly_chart(fig, use_container_width=True)

#-----------------------------------------------------------------------------

# Create a cross-tabulation of online interaction mode and satisfaction level
interaction_satisfaction_counts = pd.crosstab(
    df['Your interaction in online mode'],
    df['Your level of satisfaction in Online Education']
)

# Map interaction levels to descriptive labels for better readability
interaction_labels = {1: 'Very Low', 2: 'Low', 3: 'Average', 4: 'High', 5: 'Very High'}
interaction_satisfaction_counts.index = interaction_satisfaction_counts.index.map(interaction_labels)

# Reorder columns for consistent stacking (Bad, Average, Good)
interaction_satisfaction_counts = interaction_satisfaction_counts[['Bad', 'Average', 'Good']]

# Create stacked bar chart
fig = px.bar(
    interaction_satisfaction_counts,
    x=interaction_satisfaction_counts.index,
    y=['Bad', 'Average', 'Good'],
    title='Online Interaction vs. Online Education Satisfaction',
    labels={
        'x': 'Your Interaction in Online Mode',
        'value': 'Number of Students',
        'variable': 'Satisfaction Level'
    },
    color_discrete_map={'Bad': 'red', 'Average': 'grey', 'Good': 'blue'} # Assign colors
)

# Ensure the x-axis order is correct
fig.update_layout(
    xaxis={'categoryorder': 'array', 'categoryarray': [interaction_labels[i] for i in sorted(interaction_labels)]}
)

st.plotly_chart(fig, use_container_width=True)
