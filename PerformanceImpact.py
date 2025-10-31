import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Analysis of the Impact of Online Learning on Student Performance During COVID-19")

# Load CSV from GitHub
url = "https://raw.githubusercontent.com/wannurizzatiwanabdazizktb-arch/SV-1/refs/heads/main/ONLINE%20EDUCATION%20SYSTEM%20REVIEW.csv"

# Read the dataset
df = pd.read_csv(url)
