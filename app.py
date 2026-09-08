import streamlit as st

st.set_page_config(
    page_title="Satellite Disaster Detection",
    page_icon="🛰️",
    layout="wide"
)

st.title("🛰️ AI-Based Satellite Disaster Detection")
st.subheader("Flood Detection & Damage Assessment System")

st.markdown("""
This AI-powered system analyzes satellite imagery to detect
disaster-affected regions, estimate damage severity, and visualize
affected areas.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Disaster Type", "Flood")

with col2:
    st.metric("Affected Area", "0%")

with col3:
    st.metric("Severity", "Pending")

st.divider()

st.info(
    "Upload pre-disaster and post-disaster satellite images "
    "to begin the analysis."
)

before_image = st.file_uploader(
    "📷 Upload BEFORE disaster image",
    type=["jpg", "jpeg", "png"]
)

after_image = st.file_uploader(
    "📷 Upload AFTER disaster image",
    type=["jpg", "jpeg", "png"]
)

if before_image and after_image:

    st.success("Both satellite images uploaded successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Before Disaster")
        st.image(before_image, use_container_width=True)

    with col2:
        st.write("### After Disaster")
        st.image(after_image, use_container_width=True)

    if st.button("🔍 Analyze Disaster"):

        st.success("Analysis started...")

        st.metric(
            "Estimated Affected Area",
            "Calculating..."
        )

        st.metric(
            "Damage Severity",
            "Analyzing..."
        )
