import os
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="NED Academy GeoAI Urban Expansion Detection System",
    page_icon="🏛️",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"

PHASE3_IMG = BASE_DIR / "phase_3_fig.png"
PHASE4_IMG = BASE_DIR / "Figure_1.png"
PHASE5_IMG = BASE_DIR / "Phase_5.png"

ALT_PHASE3 = OUTPUT_DIR / "phase3_change_map.png"
ALT_PHASE5 = OUTPUT_DIR / "phase5_clean_change_map.png"
SUMMARY_CSV = OUTPUT_DIR / "phase5_corrected_summary.csv"
REPORT_PDF = BASE_DIR / "GeoAI_Urban_Expansion_Final_Report.pdf"


def show_image(title, path, caption=None):
    st.subheader(title)
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=True)
    else:
        st.warning(f"Image not found: {path}")


def download_file(label, path, mime):
    if path.exists():
        with open(path, "rb") as f:
            st.download_button(label, f, file_name=path.name, mime=mime)


st.sidebar.title("🏛️ NED Academy")
st.sidebar.markdown("""
**Project:** Urban Expansion Detection System  
**Submitted By:** Syed Nasir Shah  
**Supervisor:** Mr. Sajid Majeed  
**Year:** 2021–2026
""")

st.sidebar.divider()
st.sidebar.subheader("Key Results")
st.sidebar.metric("Built-up Area 2021", "162.99 km²")
st.sidebar.metric("Built-up Area 2026", "165.97 km²")
st.sidebar.metric("Net Built-up Change", "+2.98 km²")
st.sidebar.metric("CNN Validation Accuracy", "94.83%")

st.title("🏛️ NED Academy GeoAI Urban Expansion Detection System")
st.markdown("""
### Deep Learning-Based Urban Expansion Monitoring Using Sentinel-2 Satellite Imagery

This dashboard presents a GeoAI workflow for detecting urban expansion, vegetation loss,
and water-body changes between **2021 and 2026** using Sentinel-2 imagery, Random Forest,
CNN-based change detection, and geospatial analysis.
""")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Built-up 2021", "162.99 km²")
col2.metric("Built-up 2026", "165.97 km²")
col3.metric("Net Urban Change", "+2.98 km²")
col4.metric("Growth Percentage", "1.83%")

col5, col6, col7, col8 = st.columns(4)
col5.metric("Urban Growth Area", "24.50 km²")
col6.metric("Urban Loss Area", "21.52 km²")
col7.metric("Vegetation Loss", "3.78 km²")
col8.metric("Water Change", "18.87 km²")

st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📌 Overview",
    "🛰️ Phase 3 Change Detection",
    "🧠 Phase 4 Deep Learning",
    "🏙️ Phase 5 Urban Expansion",
    "📥 Downloads"
])

with tab1:
    st.header("Project Overview")
    st.markdown("""
    This project analyzes land-cover changes in Karachi using Sentinel-2 satellite imagery.

    **Project Phases**
    1. Sentinel-2 Data Acquisition  
    2. Random Forest Land-Cover Classification  
    3. Change Detection  
    4. CNN-Based Deep Learning Change Detection  
    5. Urban Expansion Analysis  
    """)

    st.subheader("Technologies Used")
    st.write("Python, TensorFlow/Keras, Random Forest, Rasterio, NumPy, OpenCV, Matplotlib, Pandas, Streamlit")

    st.success(
        "The analysis detected a net built-up increase of approximately 2.98 km² "
        "and urban growth area of 24.50 km² between 2021 and 2026."
    )

with tab2:
    st.header("Phase 3: Change Detection")
    st.markdown("""
    Phase 3 compares land-cover maps from 2021 and 2026 to detect:
    - Urban Growth
    - Vegetation Loss
    - Water Change
    """)

    if PHASE3_IMG.exists():
        show_image("Phase 3 Change Detection Map", PHASE3_IMG)
    elif ALT_PHASE3.exists():
        show_image("Phase 3 Change Detection Map", ALT_PHASE3)
    else:
        st.warning("Phase 3 image not found. Save it as phase_3_fig.png in the main project folder.")

    st.table(pd.DataFrame({
        "Change Type": ["Urban Growth", "Vegetation Loss", "Water Change"],
        "Area": ["24.4992 km²", "3.7849 km²", "18.8686 km²"]
    }))

with tab3:
    st.header("Phase 4: CNN-Based Deep Learning Change Detection")
    st.markdown("A Convolutional Neural Network was trained on image patches to detect changed and unchanged regions.")

    st.table(pd.DataFrame({
        "Metric": ["Training Accuracy", "Validation Accuracy", "Training Loss", "Validation Loss"],
        "Value": ["94.11%", "94.83%", "0.1351", "0.1203"]
    }))

    if PHASE4_IMG.exists():
        show_image("Phase 4 Deep Learning Change Detection", PHASE4_IMG)
    else:
        st.warning("Phase 4 image not found. Save it as Figure_1.png in the main project folder.")

with tab4:
    st.header("Phase 5: Urban Expansion Analysis")
    st.markdown("""
    Phase 5 calculates built-up area change and produces a clean map showing urban growth,
    urban loss, vegetation loss, and water change.
    """)

    if PHASE5_IMG.exists():
        show_image("Phase 5 Clean Urban Expansion Map", PHASE5_IMG)
    elif ALT_PHASE5.exists():
        show_image("Phase 5 Clean Urban Expansion Map", ALT_PHASE5)
    else:
        st.warning("Phase 5 image not found. Save it as Phase_5.png in the main project folder.")

    summary_data = {
        "Metric": [
            "Built-up Area 2021",
            "Built-up Area 2026",
            "Net Built-up Change",
            "Urban Growth Area",
            "Urban Loss Area",
            "Vegetation Loss Area",
            "Water Change Area",
            "Built-up Growth Percentage"
        ],
        "Value": [
            "162.9894",
            "165.9710",
            "+2.9816",
            "24.4992",
            "21.5176",
            "3.7849",
            "18.8686",
            "1.83"
        ],
        "Unit": ["km²", "km²", "km²", "km²", "km²", "km²", "km²", "%"]
    }

    st.dataframe(pd.DataFrame(summary_data), use_container_width=True)

    if SUMMARY_CSV.exists():
        st.subheader("CSV Summary")
        st.dataframe(pd.read_csv(SUMMARY_CSV), use_container_width=True)

with tab5:
    st.header("Download Project Outputs")

    download_file("Download Final PDF Report", REPORT_PDF, "application/pdf")
    download_file("Download Phase 5 Summary CSV", SUMMARY_CSV, "text/csv")

    if PHASE3_IMG.exists():
        download_file("Download Phase 3 Image", PHASE3_IMG, "image/png")
    if PHASE4_IMG.exists():
        download_file("Download Phase 4 Image", PHASE4_IMG, "image/png")
    if PHASE5_IMG.exists():
        download_file("Download Phase 5 Image", PHASE5_IMG, "image/png")

st.divider()
st.caption("Developed for Deep Learning Project Submission | Submitted by Syed Nasir Shah | NED Academy")
