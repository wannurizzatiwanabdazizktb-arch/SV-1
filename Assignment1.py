import streamlit as st

st.set_page_config(
    page_title="Online Learning Survey"
)

visualise = st.Page('StudentSatisfaction.py', title='Pencapaian Akademik Pelajar', icon=":material/school:")

visualise = st.Page('PerformanceImpact.py', title='Pencapaian Akademik Pelajar', icon=":material/result:")

home = st.Page('Homepage.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, visualise, visualise]
        }
    )

pg.run()
