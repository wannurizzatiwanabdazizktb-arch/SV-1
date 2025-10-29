import streamlit as st

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
    """This dashboard presents insights from collected data on students’ experiences in online education. Explore the three sections below to learn about performance impact, satisfaction levels, and challenges faced.
    """
)
