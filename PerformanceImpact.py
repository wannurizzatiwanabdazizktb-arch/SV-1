import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.header("Analysis of the Impact of Online Learning on Student Performance During COVID-19")

st.write(
    """
    The findings show that online learning does affect student performance due to limited engagement and distractions. Students who receive supervision at home and devote more time to their studies do better. This suggest that habits and surroundings play a crucial role in the success of remote learning.
    """
)

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/refs/heads/main/ONLINE%20EDUCATION%20SYSTEM%20REVIEW.csv"

# Read the dataset
df = pd.read_csv(url)

col1, col2, col3 = st.columns(3)

col1.metric(
    label="Study Time Impact",
    value="Higher",
    help="Longer study duration correlates with better performance.", 
    border=True
    
)

col2.metric(
    label="Supervision Benefit",
    value="Positive",
    help="Students with supervision are more likely to achieve higher performance.",
    border=True
)

col3.metric(
    label="COVID Performance Gap",
    value="Declined",
    help="Overall performance dropped during online learning compared to pre-pandemic.",
    border=True
)

#add subheader
st.subheader("Does students’ performance get affected during online learning?")

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

st.write(
    """
The graph shows that students’ performance during COVID-19 is slightly lower compared to before the pandemic. During online learning, the highest score students frequently achieved is around 6, and the maximum score recorded is 8. In contrast, before the pandemic, most students managed to score around 9, with some even reaching the maximum score of 10. This indicates a noticeable performance gap between traditional and online learning environments. These findings support the idea that online learning negatively impacted overall academic performance, likely due to reduced engagement, distractions at home, and limited teacher-student interaction.
    """
)


#add subheader
st.subheader("Does having someone monitoring you can lead to better education performance?")

fig = px.histogram(
    df,
    x='Performance in online',
    color='Do elderly people monitor you?',
    barmode='group',        # side-by-side bars instead of overlay
    histnorm='percent',     # show percentage instead of raw count
    opacity=0.8,            # bars are opaque enough to differentiate
    color_discrete_map={
        'Yes': '#1f77b4',  # Blue for supervised
        'No': '#d62728'    # Red for not supervised
    },
    title='Performance Distribution by Elderly Supervision',
    labels={'Performance in online':'Online Performance Score', 
            'Do elderly people monitor you?':'Elderly Supervision'}
)

fig.update_layout(
    width=800,
    height=500,
    xaxis=dict(dtick=1),    # show all integer score values
    yaxis_title="Percentage of Students",
    bargap=0.2              # space between grouped bars
)

st.plotly_chart(fig)


#add subheader
st.subheader("Does studying more lead to better academic performance?")

# Create figure
fig = go.Figure()

# Add traces for each education level
education_levels = df['Level of Education'].unique()

for i, level in enumerate(education_levels):
    subset = df[df['Level of Education'] == level]

    # Calculate average study time by performance level
    avg_study = subset.groupby('Performance in online')['Study time (Hours)'].mean().reset_index()

    fig.add_trace(
        go.Bar(
            x=avg_study['Performance in online'],
            y=avg_study['Study time (Hours)'],
            name=level,
            visible=True if i == 0 else False,  # Only first one visible initially
            hovertemplate='<b>%{x}</b><br>Avg Study Time: %{y:.1f} hrs<extra></extra>',
            text=[f"{val:.1f}h" for val in avg_study['Study time (Hours)']],
            textposition='auto'
        )
    )

# Create buttons for dropdown
buttons = []
for i, level in enumerate(education_levels):
    buttons.append(
        dict(
            label=level,
            method="update",
            args=[{"visible": [j == i for j in range(len(education_levels))]},
                  {"title": f"Average Study Time by Performance: {level}"}]
        )
    )

fig.update_layout(
    title="Average Study Time by Performance: Select Education Level",
    xaxis_title="Performance in Online",
    yaxis_title="Average Study Time (Hours)",
    height=500,
    width=800,
    updatemenus=[dict(buttons=buttons, direction="down", x=0.1, y=1.15)]
)

st.plotly_chart(fig)
