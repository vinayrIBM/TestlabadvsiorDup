import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

st.set_page_config(page_title="IBM Metis TestLab Advisor", layout="wide")

# ───────────────────────────────
# 📂 Load Helper
@st.cache_data
def load_csv(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"❌ Failed to load {path}")
        return pd.DataFrame()

# ───────────────────────────────
# 💠 IBM Logo + Title
st.image("static/ibm_logo.png", width=160)
st.title("🧠 IBM Metis TestLab Advisor + FabFlow Logger")

# ───────────────────────────────
# 📥 Load CSVs
ref_df = load_csv("data/refcode_fru_map.csv")
rules_df = load_csv("data/metis_model_rules.csv")
cmd_df = load_csv("data/se_command_library.csv")

# ───────────────────────────────
# 🔧 Refcode Diagnostic Section
st.subheader("🔍 Refcode Analysis")

if not ref_df.empty:
    selected_refcode = st.selectbox("Select a Refcode", sorted(ref_df["refcode"].unique()))
    match = ref_df[ref_df["refcode"] == selected_refcode]

    if not match.empty:
        st.markdown(f"**FRU Name:** {match['fru_name'].values[0]}")
        st.markdown(f"**Drawer/Location:** {match['drawer'].values[0]} – {match['location'].values[0]}")
        st.markdown(f"**Recovered:** {'✅' if match['recovered'].values[0]=='Yes' else '❌'}")
        st.markdown(f"**Command:** `{match['se_commands'].values[0]}`")
        st.markdown(f"**Notes:** _{match['notes'].values[0]}_")

        # 🌐 IQYedit Link (IBM Internal)
        iqyedit_url = f"https://jupitrsat.boeblingen.de.ibm.com/iqyedit/cgi-bin/iqyedit/iqysrc/{selected_refcode.lower()}"
        st.markdown("---")
        st.markdown(f"🔗 [View Full Refcode Details in IQYedit]({iqyedit_url})")
        st.info("This opens the IBM internal diagnostic portal for this refcode.")

# ───────────────────────────────
# 📊 Donut Chart for Recovery
if not ref_df.empty:
    rec_counts = ref_df["recovered"].value_counts()
    labels = rec_counts.index.tolist()
    sizes = rec_counts.values
    colors = ['#2ecc71' if l == 'Yes' else '#e74c3c' for l in labels]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90, wedgeprops={'edgecolor': 'white'})
    ax.set_title("Recovery Rate")
    ax.axis('equal')
    st.pyplot(fig)

# ───────────────────────────────
# 📘 FabFlow Logger Section
st.subheader("📘 FabFlow Test Logger")

fab_op_steps = {
    "1000 – Test floor safety checklist": "1000",
    "1030 – Info collection / setup": "1030",
    "9006 – MFG SE code load": "9006",
    "0470 – AMB+ T-sort IO parts": "0470",
    "1225 – MFS comparison": "1225",
    "1227-0 – Card personalization": "1227-0",
    "0472 – IO diagnostics @ Nominal": "0472",
    "0473 – IO diagnostics @ Nominal (Phase 2)": "0473",
    "0476 – IO diagnostics @ Cold": "0476",
    "0474 – IO diagnostics @ Hot": "0474",
    "1407 – Final MFS comparison": "1407",
    "0550 – Post-fab Op": "0550",
    "1500 – Archive process data": "1500"
}

with st.expander("➕ Log New Fab Test Entry", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        op_selected = st.selectbox("Operation Step", list(fab_op_steps.keys()))
        temp = st.radio("Temperature Condition", ["Room", "Cold", "Hot"], horizontal=True)
        result = st.radio("Result", ["Pass", "Fail"], horizontal=True)
    with col2:
        card_id = st.text_input("Card ID / Serial #")
        tech = st.text_input("Technician Initials")
        notes = st.text_area("Notes (optional)", height=100)

    if st.button("📝 Submit Log Entry"):
        if card_id.strip() and tech.strip():
            log_path = "data/fabtest_log.csv"
            new_entry = {
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "OpStep": fab_op_steps[op_selected],
                "OpDescription": op_selected,
                "Temperature": temp,
                "CardID": card_id.strip(),
                "Technician": tech.strip().upper(),
                "Result": result,
                "Notes": notes.strip()
            }

            log_df = pd.DataFrame([new_entry])
            if os.path.exists(log_path):
                log_df.to_csv(log_path, mode='a', header=False, index=False)
            else:
                log_df.to_csv(log_path, index=False)

            st.success("✅ Entry logged successfully.")
        else:
            st.warning("Please provide both Card ID and Technician initials.")

# ───────────────────────────────
# 📋 Show Recent Log Entries
log_path = "data/fabtest_log.csv"
if os.path.exists(log_path):
    log_data = pd.read_csv(log_path)
    st.markdown("### 📂 Recent Fab Test Entries")
    st.dataframe(log_data.tail(15), use_container_width=True)

# 🔽 Add this AFTER the block (no indentation)
st.markdown("---")
st.markdown("💡 Built with pride by the Techs-Rex Team: Juan, Jessey & Vi (2025)")

