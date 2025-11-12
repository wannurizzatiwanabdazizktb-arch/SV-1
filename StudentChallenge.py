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

st.subheader("Does not having a study room could be a reason of bad performance in online learning?")

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

st.write(
    """
    The bar chart illustrates the impact of having a separate study room on students’ online learning performance. Students with a dedicated study room generally perform better, with noticeably higher counts in the mid to high-performance range scores 6–8. For instance, around 140 students with a study room achieved a performance score of 6 compared to fewer than 100 students without one.

However, while having a study room seems to support better concentration and productivity, the difference at higher performance levels of score 10 is relatively small between the two groups. This suggests that while the learning environment contributes positively to academic performance, other factors—such as motivation, teaching quality, or time management may also play important roles in determining success in online learning.
    """
)


#---------------------------------------------------------------------------

st.subheader("Does not joining study group can influence the performance in online learning?")

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

st.write(
    """
    The box plot compares online learning performance between students who participated in group studies and those who did not. Overall, both groups display a similar median performance score of around 7, indicating that group study participation does not drastically alter median outcomes.

However, students engaged in group studies show a slightly narrower interquartile range (IQR), suggesting more consistent performance among this group. In contrast, those who did not join group studies have a wider spread of scores, indicating greater variability where some performed very well, while others scored quite low.

This implies that group study engagement may help stabilize performance levels and reduce extreme variations, even if it does not significantly raise the overall median performance.
    """
)

#------------------------------------------------------------

st.subheader("Does economic status affect the performance in online learning?")

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

st.write(
    """
    The bar chart shows that students from rich families exhibit a mixed and uneven performance pattern in online learning. About 40% of them achieved high performance, yet around 50% also fell into the low-performance category, with only a small portion of 10% in the medium range. This suggests that wealth alone does not guarantee consistent academic success—other factors, such as motivation or learning habits, may strongly influence outcomes.

In contrast, students from middle-class and poor backgrounds display more stable results with the majority performing at a medium level approximately 58% and 57% respectively. This indicates that while limited resources may constrain top performance, these groups tend to show steadier and more balanced achievement overall.
    """
)
