import streamlit as st

st.title("👨‍⚕️ Therapist Dashboard")

st.metric("Current Stage", "Bargaining")

st.metric("PGD Risk Score", "62%")

st.warning("Patient requires monitoring")

st.write("### Recent Sessions")

st.write("""
Session 1 - Risk 45%

Session 2 - Risk 52%

Session 3 - Risk 62%
""")