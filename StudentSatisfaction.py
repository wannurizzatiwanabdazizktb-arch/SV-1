import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analysis of Students’ Satisfaction with Online Learning During COVID-19")

st.write(
    """
    Student satisfaction during online learning became a critical concern throughout the COVID-19 period, as traditional face-to-face teaching was replaced with digital platforms. Satisfaction levels were largely influenced by factors including internet connectivity, communication with lecturers, and opportunities for interaction. These factors collectively shaped the quality and effectiveness of the learning process.
    """
)

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/refs/heads/main/ONLINE%20EDUCATION%20SYSTEM%20REVIEW.csv"

col1, col2, col3 = st.columns(3)

col1.metric(
    label="Internet Facility Satisfaction",
    value="High",
    help="Students show higher satisfaction when internet connectivity is excellent.",
    border=True
)

col2.metric(
    label="Online Interaction Impact",
    value="Moderate–High",
    help="Satisfaction levels improve when students interact more during online classes.",
    border=True
)

col3.metric(
    label="Faculty Accessibility",
    value="Moderate–High",
    help="Students report better satisfaction when they can easily reach lecturers or faculties online.",
    border=True
)

# Read the dataset
df = pd.read_csv(url)

#add subheader
st.subheader("Are students satisfied with internet facilities during online learning?")

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
    text="Scale: Red = Good, Grey = Average, Blue = Bad",
    xref="paper", yref="paper",
    x=0, y=-0.2,
    showarrow=False,
    font=dict(size=10)
)

st.plotly_chart(fig, use_container_width=True)

st.write(
    """
    The graph indicates that students with excellent internet connectivity report the highest satisfaction with online learning with average score of 2.09, while those with very poor connectivity report the lowest satisfaction of 1.59. This demonstrates a clear link between internet quality and the perceived effectiveness of online education which highlight the importance of reliable internet for student engagement and satisfaction.
    """
)

#-----------------------------------------------------------------------------

#add subheader
st.subheader("Does higher interaction in online classes lead to greater student satisfaction?")

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

st.write(
    """
    The graph shows a clear positive relationship between students’ online interaction and their satisfaction with online learning. Students with Very High interaction report the highest satisfaction with 68 out of 93 students indicating ‘Good’ satisfaction. Conversely, students with Very Low interaction have the lowest satisfaction with 86 out of 129 students reporting ‘Bad’ satisfaction. Those with Average interaction form the largest group consist of 433 students, where most report neutral satisfaction. This demonstrates that higher engagement in online classes correlates with higher satisfaction which emphasise the importance of active participation for a better online learning experience.
    """
)

# --------------------------------------------------------------------

#add subheader
st.subheader("Does having quick and easy communication with faculty improve students’ satisfaction in online learning?")

# Create a cross-tabulation of clearing doubts and satisfaction level
doubts_satisfaction_counts = pd.crosstab(
    df['Clearing doubts with faculties in online mode'],
    df['Your level of satisfaction in Online Education']
)

# Map clearing doubts levels to descriptive labels
doubts_labels = {1: 'Very Difficult', 2: 'Difficult', 3: 'Average', 4: 'Easy', 5: 'Very Easy'}
doubts_satisfaction_counts.index = doubts_satisfaction_counts.index.map(doubts_labels)

# Reorder columns for consistent grouping (Bad, Average, Good)
doubts_satisfaction_counts = doubts_satisfaction_counts[['Bad', 'Average', 'Good']]

# Create grouped bar chart
fig = px.bar(
    doubts_satisfaction_counts,
    x=doubts_satisfaction_counts.index,
    y=['Bad', 'Average', 'Good'],
    barmode='group',  # Use 'group' for grouped bars
    title='Clearing Doubts with Faculties vs. Online Education Satisfaction',
    labels={
        'x': 'Clearing Doubts with Faculties',
        'value': 'Number of Students',
        'variable': 'Satisfaction Level'
    },
    color_discrete_map={'Bad': 'red', 'Average': 'grey', 'Good': 'blue'} # Assign colors
)

# Ensure the x-axis order is correct
fig.update_layout(
    xaxis={'categoryorder': 'array', 'categoryarray': [doubts_labels[i] for i in sorted(doubts_labels)]}
)

st.plotly_chart(fig, use_container_width=True)

st.write(
    """
    The graph shows a positive relationship between students’ access to faculty and their satisfaction with online learning. Students with very high access to faculty report good satisfaction, with approximately 64 students in this group. Those with very low access are mostly dissatisfied, with around 102 students reporting bad satisfaction. Most students fall in the middle, where 112 students with low access, 246 students with average access, and 102 students with high access report average satisfaction. This indicates that better access to faculty supports higher student satisfaction and emphasizes the importance of responsive communication in online learning.
    """
)
