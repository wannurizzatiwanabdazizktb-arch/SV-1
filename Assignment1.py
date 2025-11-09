import streamlit as st

st.set_page_config(
    page_title="Online Learning Survey"
)

page1 = st.Page('StudentSatisfaction.py', title='Students Satisfaction in Online Learning', icon=":material/thumb_up_off_alt:")

page2 = st.Page('PerformanceImpact.py', title='Impact of Online Learning', icon=":material/assignment_turned_in:")

page3 = st.Page('StudentChallenge.py', title='Challenge During Online Learning', icon=":material/outlined_flag:")

home = st.Page('Homepage.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home, page1, page2, page3]
        }
    )

pg.run()
