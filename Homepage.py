import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# Add a header title
st.header("Impact of Online Learning During COVID-19")

# Add the main introduction paragraph
st.write(
    """
    An analysis of student satisfaction, performance, and challenges during the pandemic.
    """
)

# Add a banner image at the top
banner_image = 'https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/main/OnlineLearning.jpg' 
st.image(banner_image, use_container_width=True)

# Add the extended explanation
st.write(
    """This dashboard presents insights from collected data on students’ experiences in online education. Explore the three sections below to learn about performance impact, satisfaction levels, and challenges faced from students during COVID-19.
    """
)

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/refs/heads/main/ONLINE%20EDUCATION%20SYSTEM%20REVIEW.csv"

# Read the dataset
df = pd.read_csv(url)

# Add the header title
st.header("Demographic Overview")

# Add the subtitle header
st.subheader("1. Gender Distribution")

# Set theme
pio.templates.default = "plotly_white"

# Blue–Red palette
colors = ["#1f77b4", "#d62728", "#7f7f7f"]

# ==============================
# 1️⃣ Gender Distribution (Pie)
# ==============================
gender_counts = df["Gender"].value_counts()

fig = go.Figure(
    data=[go.Pie(
        labels=gender_counts.index,
        values=gender_counts.values,
        marker_colors=colors[:len(gender_counts)]
    )]
)

fig.update_layout(
    title="Gender Distribution",
    legend_title="Gender"
)

fig.show()


# =======================================
# 2️⃣ Level of Education Distribution (Bar)
# =======================================
edu_counts = df["Level of Education"].value_counts()

fig = go.Figure(
    data=[go.Bar(
        x=edu_counts.index,
        y=edu_counts.values,
        marker_color=colors[:len(edu_counts)]
    )]
)

fig.update_layout(
    title="Level of Education Distribution",
    legend_title="Education Level",
    xaxis_title="Education Level",
    yaxis_title="Count"
)

fig.show()


# =======================
# 3️⃣ Age Distribution
# =======================
fig = go.Figure(
    data=[go.Histogram(
        x=df["Age(Years)"],
        marker_color=colors[0]
    )]
)

fig.update_layout(
    title="Age Distribution",
    xaxis_title="Age (Years)",
    yaxis_title="Frequency",
    bargap=0.2
)

fig.show()


# ================================
# 4️⃣ Home Location Distribution
# ================================
home_counts = df["Home Location"].value_counts()

fig = go.Figure(
    data=[go.Bar(
        x=home_counts.index,
        y=home_counts.values,
        marker_color=colors[:len(home_counts)]
    )]
)

fig.update_layout(
    title="Home Location Distribution",
    xaxis_title="Home Location",
    yaxis_title="Count"
)

fig.show()


# =========================
# 5️⃣ Economic Status (Donut)
# =========================
econ_counts = df["Economic status"].value_counts()

fig = go.Figure(
    data=[go.Pie(
        labels=econ_counts.index,
        values=econ_counts.values,
        hole=0.4,
        marker_colors=colors[:len(econ_counts)]
    )]
)

fig.update_layout(
    title="Economic Status Distribution",
    legend_title="Economic Class"
)

fig.show()



