import streamlit as st
import numpy as np
from PIL import Image

from preprocessing.image_preprocessing import (
    prepare_for_comparison,
    calculate_difference
)

from detection.change_detection import (
    detect_changes,
    calculate_affected_area
)


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="Satellite Disaster Detection",
    page_icon="🛰️",
    layout="wide"
)


# -----------------------------
# CUSTOM CSS
# -----------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #081b29, #123b4a, #0b2635);
    color: white;
}

.main-title {
    font-size: 45px;
    font-weight: bold;
    text-align: center;
    color: #00e5ff;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #b8e8f2;
    margin-bottom: 30px;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    background: rgba(255,255,255,0.08);
    text-align: center;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# TITLE
# -----------------------------

st.markdown(
    '<div class="main-title">🛰️ SATELLITE DISASTER DETECTION</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Based Flood Detection & Damage Assessment</div>',
    unsafe_allow_html=True
)

st.divider()


# -----------------------------
# INFORMATION
# -----------------------------

st.write(
    """
    Upload satellite images captured **before and after a disaster**.
    The system compares the images and identifies significant changes
    that may indicate flood-affected regions.
    """
)


# -----------------------------
# IMAGE UPLOAD
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌍 Before Disaster")

    before_image = st.file_uploader(
        "Upload pre-disaster satellite image",
        type=["jpg", "jpeg", "png"],
        key="before"
    )


with col2:

    st.subheader("🌊 After Disaster")

    after_image = st.file_uploader(
        "Upload post-disaster satellite image",
        type=["jpg", "jpeg", "png"],
        key="after"
    )


# -----------------------------
# ANALYSIS
# -----------------------------

if before_image and after_image:

    st.divider()

    st.subheader("📊 Satellite Image Comparison")

    col1, col2 = st.columns(2)

    with col1:

        before_display = Image.open(before_image)

        st.image(
            before_display,
            caption="Before Disaster",
            use_container_width=True
        )


    with col2:

        after_display = Image.open(after_image)

        st.image(
            after_display,
            caption="After Disaster",
            use_container_width=True
        )


    st.divider()

    analyze = st.button(
        "🔍 ANALYZE DISASTER",
        use_container_width=True
    )


    if analyze:

        with st.spinner("AI is analyzing satellite imagery..."):

            # -----------------------------
            # PREPROCESS IMAGES
            # -----------------------------

            before, after = prepare_for_comparison(
                before_image,
                after_image
            )


            # -----------------------------
            # CALCULATE IMAGE DIFFERENCE
            # -----------------------------

            difference = calculate_difference(
                before,
                after
            )


            # -----------------------------
            # DETECT CHANGES
            # -----------------------------

            change_mask = detect_changes(
                difference
            )


            # -----------------------------
            # CALCULATE AFFECTED AREA
            # -----------------------------

            affected_area = calculate_affected_area(
                change_mask
            )


            # -----------------------------
            # DAMAGE SEVERITY
            # -----------------------------

            if affected_area < 10:

                severity = "🟢 LOW"

            elif affected_area < 30:

                severity = "🟡 MODERATE"

            elif affected_area < 60:

                severity = "🟠 HIGH"

            else:

                severity = "🔴 SEVERE"


        st.success("Analysis completed successfully!")


        # -----------------------------
        # RESULTS
        # -----------------------------

        st.subheader("🚨 Disaster Assessment")


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Affected Area",
                f"{affected_area}%"
            )


        with col2:

            st.metric(
                "Disaster Type",
                "Flood"
            )


        with col3:

            st.metric(
                "Severity",
                severity
            )


        st.divider()


        # -----------------------------
        # CHANGE MASK
        # -----------------------------

        st.subheader("🗺️ Detected Affected Region")

        st.image(
            change_mask,
            caption="Detected Change / Potential Flood Region",
            use_container_width=True
        )


        st.info(
            f"""
            The system detected approximately **{affected_area}%**
            of the analyzed image as significantly changed.

            Estimated severity: **{severity}**
            """
        )


else:

    st.info(
        "👆 Upload both satellite images to begin disaster analysis."
    )
