import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analysis of Students’ Satisfaction with Online Learning During COVID-19")

# =========================
# Load dataset
# =========================
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of data:")
    st.dataframe(df)

   import plotly.express as px

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

fig.show()


    st.pyplot(fig)

else:
    st.info("Please upload a CSV to begin.")
