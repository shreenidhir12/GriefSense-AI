import streamlit as st
import pandas as pd

st.set_page_config(page_title="GriefSense AI")

st.title("💙 GriefSense AI")
st.subheader("Welcome")

user_input = st.text_area(
    "How are you feeling today?"
)

if st.button("Analyze"):

    text = user_input.lower()

    if "can't believe" in text:
        stage = "Denial"
        confidence = "82%"

    elif "angry" in text:
        stage = "Anger"
        confidence = "80%"

    elif "what if" in text:
        stage = "Bargaining"
        confidence = "74%"

    elif "empty" in text:
        stage = "Depression"
        confidence = "79%"

    else:
        stage = "Acceptance"
        confidence = "70%"

    st.write("## Analysis Results")

    st.success(f"Stage: {stage}")

    st.info(f"Confidence: {confidence}")

    if stage == "Depression":
        risk = 85

    elif stage == "Anger":
        risk = 70

    elif stage == "Bargaining":
        risk = 65

    elif stage == "Denial":
        risk = 50

    else:
        risk = 25

    st.write("### PGD Risk Score")

    st.metric(
        "Current Risk",
        f"{risk}%"
    )

    st.progress(risk)

    st.write("### Risk Trend")

    risk_data = pd.DataFrame(
        {
            "Risk Score": [45, 52, 65, risk]
        }
    )

    st.line_chart(risk_data)

    if stage == "Denial":
        message = "It is okay if the loss still feels unreal."

    elif stage == "Anger":
        message = "Strong emotions are a normal part of grief."

    elif stage == "Bargaining":
        message = "Many people revisit past decisions after a loss."

    elif stage == "Depression":
        message = "You do not have to carry these feelings alone."

    else:
        message = "Acceptance does not mean forgetting. It means learning to move forward."

    st.write("### Support Message")

    st.write(message)