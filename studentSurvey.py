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

    # ==================================
    # Choose the satisfaction column
    # ==================================
    score_column = st.selectbox("Select Satisfaction Score Column", df.columns)

    # ==================================
    # Group by category/aspect
    # ==================================
    if st.checkbox("Group by category column?"):
        category_column = st.selectbox("Select Category Column", df.columns)
        avg_scores = df.groupby(category_column)[score_column].mean().reset_index()
        x = avg_scores[category_column]
        y = avg_scores[score_column]
    else:
        avg_scores = df
        x = df.index
        y = df[score_column]

    # ==================================
    # Color function (Blue = Good, Grey = Average, Red = Bad)
    # ==================================
    def get_color(score):
        if score >= 4:
            return "#1f77b4"  # blue (good)
        elif score >= 2.5:
            return "#7f7f7f"  # grey (average)
        else:
            return "#d62728"  # red (bad)

    colors = y.apply(get_color)

    # ==================================
    # Plot
    # ==================================
    fig, ax = plt.subplots()
    ax.bar(x, y, color=colors)
    ax.set_ylabel("Average Satisfaction Score")
    ax.set_title("Student Satisfaction for Online Learning")

    # Add legend
    blue = mpatches.Patch(color="#1f77b4", label="Good (>= 4.0)")
    grey = mpatches.Patch(color="#7f7f7f", label="Average (2.5 - 3.9)")
    red = mpatches.Patch(color="#d62728", label="Bad (< 2.5)")
    ax.legend(handles=[blue, grey, red])

    # Rotate labels (optional)
    plt.xticks(rotation=15)

    st.pyplot(fig)

else:
    st.info("Please upload a CSV to begin.")
