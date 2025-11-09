import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analysis of Students’ Challenges and Learning Performance in Online Education")

st.write(
    """
    During the COVID-19 pandemic, students faced several challenges that affected their learning performance in online education. Factors such as having a dedicated study room, economic status, and engagement in group studies influenced their ability to focus, access learning materials, and interact effectively with peers which ultimately shaping their overall academic outcomes in online learning.
    """
)

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/refs/heads/main/ONLINE%20EDUCATION%20SYSTEM%20REVIEW.csv"

# Read the dataset
df = pd.read_csv(url)

col1, col2 = st.columns(2)

col1.metric(
    label="Dedicated Study Room",
    value="Majority",
    help="Most students who achieved good online performance had their own study room.",
    border=True
)

col2.metric(
    label="Group Study Engagement",
    value="Positive",
    help="Participating in group studies is positively associated with higher online performance scores.",
    border=True
)

#------------------------------------------------------------------------------
fig = px.histogram(
    df,
    x='Performance in online',
    color='Have separate room for studying?',
    barmode='group',
    title='Impact of Having a Study Room on Online Learning Performance',
    color_discrete_map={
        'Yes': 'blue',
        'No': 'red'
    }
)

st.plotly_chart(fig)


#---------------------------------------------------------------------------
fig = px.box(
    df,
    x='Engaged in group studies?',
    y='Performance in online',
    title='Online Performance Distribution by Group Study Engagement',
    labels={
        'Engaged in group studies?': 'Engaged in Group Studies?',
        'Performance in online': 'Online Performance Score'
    },
    color='Engaged in group studies?',
    color_discrete_map={
        'Yes': 'blue',
        'No': 'red'
    }
)

fig.update_layout(width=600, height=500)
st.plotly_chart(fig)


#------------------------------------------------------------
# Group performance to reduce noise
df['Performance Group'] = pd.cut(
    df['Performance in online'],
    bins=[0, 3, 7, 10],
    labels=['Low', 'Medium', 'High']
)

# Color scheme
color_map = {
    'Low': '#d62728',    # Red
    'Medium': '#ffcc00', # Yellow
    'High': '#1f77b4'    # Blue
}

# Pie chart with facets
fig = px.pie(
    df,
    names='Performance Group',
    facet_col='Economic status',
    hole=0.35,
    title='Online Performance by Economic Status (Grouped)',
)

# Apply consistent color mapping
fig.update_traces(
    marker=dict(colors=[color_map[v] for v in sorted(df['Performance Group'].unique())]),
    textinfo='percent',
    hovertemplate='%{label}: %{percent} <extra></extra>'
)

# Layout improvements
fig.update_layout(
    width=950,
    height=450,
    title_x=0.5,
    margin=dict(t=60, l=40, r=40, b=40),
    showlegend=True
)

st.plotly_chart(fig)
