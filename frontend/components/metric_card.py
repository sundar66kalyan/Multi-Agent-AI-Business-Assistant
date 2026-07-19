import streamlit as st


def metric_card(title, value, delta, icon):
    """Reusable Metric Card component"""
    st.markdown(
        f"""
<div style="
background:white;
padding:20px;
border-radius:15px;
box-shadow:0 4px 10px rgba(0,0,0,.1);
border-left:5px solid #2563eb;">

<h4>{icon} {title}</h4>

<h1>{value}</h1>

<p style="color:green;">▲ {delta}</p>

</div>
""",
        unsafe_allow_html=True,
    )