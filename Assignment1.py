import streamlit as st

st.set_page_config(
    page_title="Online Learning Survey"
)

visualise = st.Page('StudentSatisfaction.py', title='Pencapaian Akademik Pelajar', icon=":material/school:")

visualise1 = st.Page('PerformanceImpact.py', title='Pencapaian Akademik Pelajar', icon=":material/AssignmentTurnedIn:")

home = st.Page('Homepage.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, visualise, visualise1]
        }
    )

pg.run()
