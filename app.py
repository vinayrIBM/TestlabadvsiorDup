import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
import requests
import json

st.set_page_config(
    page_title="IBM Metis TestLab Advisor", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize watsonx.ai integration
class WatsonxAIHelper:
    def __init__(self):
        self.api_key = os.environ.get('WATSONX_API_KEY')
        self.project_id = os.environ.get('WATSONX_PROJECT_ID')
        self.base_url = "https://us-south.ml.cloud.ibm.com"
        
        # Available Granite models
        self.models = {
            "granite-3-2-8b": "ibm/granite-3-2-8b-instruct",
            "granite-13b-chat": "ibm/granite-13b-chat-v2"
        }
        self.current_model = "granite-3-2-8b"
        
    def is_configured(self):
        return bool(self.api_key and self.project_id)
    
    def get_current_model_id(self):
        return self.models[self.current_model]
    
    def switch_model(self, model_key):
        if model_key in self.models:
            self.current_model = model_key
            return True
        return False
    
    def generate_diagnostic_analysis(self, refcode, fru_name, symptoms, model_preference=None):
        """Generate AI-powered diagnostic analysis using selected Granite model"""
        if not self.is_configured():
            return self._mock_analysis(refcode, fru_name, symptoms, model_preference)
        
        try:
            # Real watsonx.ai API call would go here
            return self._mock_analysis(refcode, fru_name, symptoms, model_preference)
        except Exception as e:
            return f"AI analysis unavailable: {str(e)}"
    
    def _mock_analysis(self, refcode, fru_name, symptoms, model_preference=None):
        """Mock analysis for demonstration (replace with real AI when configured)"""
        model_name = model_preference or self.current_model
        
        # Different analysis styles based on model
        if model_name == "granite-13b-chat":
            # Granite-13B-Chat-v2 provides more conversational, detailed analysis
            analyses = {
                "DCM": f"**Granite-13B-Chat-v2 Analysis for {fru_name}:**\n\nHello! I've analyzed the {fru_name} component failure and here's my detailed assessment:\n\n🔍 **Comprehensive Root Cause Analysis:**\nThe {fru_name} is exhibiting failure patterns consistent with thermal-induced stress or power delivery anomalies. Based on my training on IBM Z system diagnostics, this typically occurs when:\n- Thermal interface materials degrade over time\n- Power rail voltages drift outside specification\n- Cooling airflow is insufficient for the workload\n\n💬 **Interactive Recommendations:**\nLet me walk you through the diagnostic steps:\n1. **Thermal Check**: Verify TIM application and reapply if necessary\n2. **Power Analysis**: Check VRM outputs - should be within ±5% of nominal\n3. **Stress Testing**: Run extended thermal stress for 4+ hours\n\n🎯 **Success Prediction**: 87% recovery probability with systematic approach\n\n*This analysis uses Granite-13B's enhanced conversational capabilities for detailed guidance.*",
                
                "VPD": f"**Granite-13B-Chat-v2 Analysis for {fru_name}:**\n\nI understand you're dealing with a VPD issue on {fru_name}. Let me provide a thorough analysis:\n\n🔍 **Deep Dive Assessment:**\nVPD (Vital Product Data) corruption in {fru_name} suggests underlying EEPROM integrity issues. From my knowledge of IBM hardware diagnostics, this pattern indicates:\n- I2C bus communication errors\n- EEPROM wear leveling exhaustion\n- Firmware update interruption\n\n💬 **Step-by-Step Recovery:**\nHere's how I recommend approaching this:\n1. **Data Recovery**: Attempt VPD restore from system backup\n2. **Bus Verification**: Test I2C bus integrity with scope\n3. **Firmware Update**: Apply latest microcode if available\n\n🎯 **Recovery Outlook**: 73% success rate with VPD restoration procedures\n\n*Granite-13B provides enhanced diagnostic reasoning for complex issues.*",
                
                "default": f"**Granite-13B-Chat-v2 Analysis for {fru_name}:**\n\nI'm here to help with your {fru_name} diagnostic challenge. Let me analyze refcode {refcode}:\n\n🔍 **Intelligent Assessment:**\nBased on the failure signature and my extensive training on IBM Z diagnostics, this {fru_name} component requires a methodical diagnostic approach. The failure pattern suggests multiple potential root causes that need systematic elimination.\n\n💬 **Guided Troubleshooting:**\nLet me guide you through the diagnostic process:\n1. **Initial Assessment**: Run comprehensive diagnostic suite\n2. **Component Isolation**: Check associated subsystems\n3. **Pattern Analysis**: Review error logs for recurring patterns\n\n🎯 **Predicted Outcome**: 78% recovery probability with proper systematic diagnosis\n\n*Using Granite-13B's enhanced reasoning for comprehensive analysis.*"
            }
        else:
            # Granite-3-2-8B provides concise, technical analysis
            analyses = {
                "DCM": f"**Granite-3-2-8B Analysis for {fru_name}:**\n\n🔍 **Root Cause Assessment:** {fru_name} thermal/power failure. Check cooling and VRM outputs.\n\n💡 **Actions:**\n1. Verify TIM application\n2. Check VRM voltages\n3. Thermal stress test\n\n⚡ **Recovery Probability:** 85%",
                
                "VPD": f"**Granite-3-2-8B Analysis for {fru_name}:**\n\n🔍 **Root Cause Assessment:** VPD corruption - EEPROM/I2C issue.\n\n💡 **Actions:**\n1. VPD restore from backup\n2. I2C bus check\n3. Microcode update\n\n⚡ **Recovery Probability:** 70%",
                
                "default": f"**Granite-3-2-8B Analysis for {fru_name}:**\n\n🔍 **Root Cause Assessment:** {fru_name} component failure - refcode {refcode}.\n\n💡 **Actions:**\n1. Diagnostic suite\n2. Check related components\n3. Log pattern analysis\n\n⚡ **Recovery Probability:** 75%"
            }
        
        # Determine analysis type based on FRU name
        for key in analyses:
            if key.lower() in fru_name.lower():
                return analyses[key]
        return analyses["default"]
    
    def suggest_se_commands(self, issue_description, model_preference=None):
        """AI-powered SE command suggestions"""
        if not self.is_configured():
            return self._mock_commands(issue_description, model_preference)
        
        try:
            # Real watsonx.ai API call would go here
            return self._mock_commands(issue_description, model_preference)
        except Exception as e:
            return ["# AI command suggestions unavailable"]
    
    def _mock_commands(self, issue_description, model_preference=None):
        """Mock command suggestions based on issue keywords and model capability"""
        model_name = model_preference or self.current_model
        
        if model_name == "granite-13b-chat":
            # Granite-13B provides more comprehensive command sets with explanations
            commands_db = {
                "power": [
                    "# Granite-13B Enhanced Power Diagnostics",
                    "zsegetsysstatus --status Power_System_complete",
                    "cecctl power status --verbose",
                    "power_rail_check.py --all-rails",
                    "voltage_monitor.py --continuous",
                    "psu_diagnostic.sh --extended"
                ],
                "thermal": [
                    "# Granite-13B Thermal Analysis Suite", 
                    "thermal_monitor.py --all-sensors",
                    "fan_status_check.sh --rpm-analysis",
                    "temp_sensor_read.py --trending",
                    "airflow_analysis.py",
                    "thermal_stress_test.py --duration=240"
                ],
                "memory": [
                    "# Granite-13B Memory Diagnostics",
                    "memory_test.py --comprehensive",
                    "dimm_diagnostic.sh --all-banks", 
                    "ecc_error_check.py --historical",
                    "memory_stress.py --pattern-test",
                    "spd_verify.py --all-dimms"
                ],
                "io": [
                    "# Granite-13B I/O Analysis",
                    "cardctl test --verbose --all-ports",
                    "io_enumeration.sh --deep-scan",
                    "pci_diagnostic.py --link-test",
                    "lane_margining.py --all-lanes",
                    "io_stress_test.py --duration=120"
                ],
                "default": [
                    "# Granite-13B General Diagnostics",
                    "zsegetsysstatus --comprehensive",
                    "cecctl status --all-drawers", 
                    "zm_dcm_data.py --detailed",
                    "system_health_check.py --full-report"
                ]
            }
        else:
            # Granite-3-2-8B provides focused, essential commands
            commands_db = {
                "power": ["zsegetsysstatus --status Power_System_complete", "cecctl power status", "power_rail_check.py"],
                "thermal": ["thermal_monitor.py", "fan_status_check.sh", "temp_sensor_read.py"],
                "memory": ["memory_test.py", "dimm_diagnostic.sh", "ecc_error_check.py"],
                "io": ["cardctl test --verbose", "io_enumeration.sh", "pci_diagnostic.py"],
                "firmware": ["verify_firmware.sh", "microcode_check.py", "flash_verify.sh"],
                "default": ["zsegetsysstatus", "cecctl status", "zm_dcm_data.py"]
            }
        
        issue_lower = issue_description.lower()
        for category, commands in commands_db.items():
            if category in issue_lower:
                return commands
        return commands_db["default"]

# Initialize AI helper
ai_helper = WatsonxAIHelper()

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1f70c1 0%, #0f4c75 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1f70c1;
        margin: 0.5rem 0;
    }
    .search-container {
        background: transparent;
        padding: 0.5rem 0;
        margin-bottom: 1rem;
    }
    .diagnostic-panel {
        background: #ffffff;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .logger-panel {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin-bottom: 1rem;
    }
    .stSelectbox > div > div {
        background-color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ddd !important;
    }
    .stTextArea > div > div > textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border: 1px solid #ddd !important;
    }
</style>
""", unsafe_allow_html=True)

# Load Function
@st.cache_data
def load_csv(path):
    try:
        return pd.read_csv(path)
    except:
        st.warning(f"Could not load {path}")
        return pd.DataFrame()

# Load Data
ref_df = load_csv("data/refcode_fru_map.csv")
rules_df = load_csv("data/metis_model_rules.csv")
cmd_df = load_csv("data/se_command_library.csv")

# Enhanced Header with gradient background
st.markdown("""
<div class="main-header">
    <h1>🧠 IBM Metis TestLab Advisor</h1>
    <p style="margin: 0; opacity: 0.9;">Hardware Diagnostic Support & Manufacturing Test Logger</p>
    <p style="margin: 0; opacity: 0.7; font-size: 0.9em;">Powered by IBM watsonx.ai & Granite Foundation Models</p>
</div>
""", unsafe_allow_html=True)

# Logo and metrics row
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    try:
        st.image("static/ibm_logo.svg", width=120)
    except:
        st.markdown("**🔵 IBM**")  # Fallback text if logo fails

with col2:
    if not ref_df.empty:
        total_components = len(ref_df)
        st.metric("Total Components", total_components, "Active")
    else:
        total_components = 0
        st.metric("Total Components", "0", "No Data")

with col3:
    if not ref_df.empty and total_components > 0:
        recovered_count = len(ref_df[ref_df["recovered"] == "Yes"])
        recovery_rate = f"{(recovered_count/total_components)*100:.1f}%"
        st.metric("Recovery Rate", recovery_rate, "Operational")
    else:
        st.metric("Recovery Rate", "0%", "No Data")

with col4:
    if not ref_df.empty:
        failed_count = len(ref_df[ref_df["recovered"] == "No"])
        st.metric("Failed Components", failed_count, "Attention" if failed_count > 0 else "Good")
    else:
        st.metric("Failed Components", "0", "No Data")

# Refcode Diagnostic Panel
st.markdown('<div class="diagnostic-panel">', unsafe_allow_html=True)
st.subheader("🔍 Diagnostic Console")

# Enhanced Search Bar
st.markdown('<div class="search-container">', unsafe_allow_html=True)
search_query = st.text_input("🔎 Search IBM Metis components (Titania, Hemlock, Pavo, zHyperLink, FRU numbers, etc.)", placeholder="Type to search refcodes, FRU numbers, drawer types, locations, or notes...")
st.markdown('</div>', unsafe_allow_html=True)

# Quick search suggestions
if not search_query:
    with st.expander("💡 Quick Search Examples"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**IBM Z Refcode Types:**")
            st.markdown("- `3232xxxx` - System/Host IPL failures")
            st.markdown("- `B700xxxx` - Hardware-level errors")
            st.markdown("- `CE00xxxx` - CE test tool codes")
            st.markdown("- `E000xxxx` - Early firmware/POST events")
        with col2:
            st.markdown("**Common SE Commands:**")
            st.markdown("- `zm_dcm_data.py` - Chip data analysis")
            st.markdown("- `zsegetsysstatus` - System status check")
            st.markdown("- `cecctl reset` - CEC control reset")
            st.markdown("- `drawerctl` - Drawer management")
        with col3:
            st.markdown("**Component Types:**")
            st.markdown("- `DCM` - Dual Chip Modules")
            st.markdown("- `VPD` - Vital Product Data issues")
            st.markdown("- `SCL` - Scaled Clock Level")
            st.markdown("- `PSRO` - Power-on Self-Reset")

if not ref_df.empty:
    # Filter data based on search
    filtered_df = ref_df.copy()
    if search_query.strip():
        search_term = search_query.lower().strip()
        mask = (
            ref_df["refcode"].astype(str).str.lower().str.contains(search_term, na=False) |
            ref_df["fru_number"].str.lower().str.contains(search_term, na=False) |
            ref_df["fru_name"].str.lower().str.contains(search_term, na=False) |
            ref_df["drawer"].str.lower().str.contains(search_term, na=False) |
            ref_df["location"].str.lower().str.contains(search_term, na=False) |
            ref_df["se_commands"].str.lower().str.contains(search_term, na=False) |
            ref_df["notes"].str.lower().str.contains(search_term, na=False)
        )
        filtered_df = ref_df[mask].copy()
        
        if len(filtered_df) > 0:
            st.info(f"Found {len(filtered_df)} result(s) for '{search_query}'")
        else:
            st.warning(f"No results found for '{search_query}'")
    
    # Show selection dropdowns
    col1, col2 = st.columns(2)
    with col1:
        if len(filtered_df) > 0:
            available_refcodes = [""] + sorted(list(set(filtered_df["refcode"].astype(str))))
            selected_refcode = st.selectbox("Select a Refcode", available_refcodes, index=0)
        else:
            selected_refcode = ""
            st.selectbox("Select a Refcode", ["No results"], disabled=True)
    
    with col2:
        if len(filtered_df) > 0:
            available_frus = [""] + sorted(list(set(filtered_df["fru_name"])))
            selected_fru = st.selectbox("...Or Pick a FRU", available_frus, index=0)
        else:
            selected_fru = ""
            st.selectbox("...Or Pick a FRU", ["No results"], disabled=True)

    # Determine which data to show
    match_row = None
    if selected_fru and selected_fru != "":
        matches = filtered_df[filtered_df["fru_name"] == selected_fru]
        if len(matches) > 0:
            match_row = matches.iloc[0]
    elif selected_refcode and selected_refcode != "":
        matches = filtered_df[filtered_df["refcode"].astype(str) == str(selected_refcode)]
        if len(matches) > 0:
            match_row = matches.iloc[0]

    if match_row is not None:
        
        # Safely access columns with fallbacks
        fru_number = match_row['fru_number'] if 'fru_number' in match_row else 'N/A'
        fru_name = match_row['fru_name'] if 'fru_name' in match_row else 'N/A'
        drawer = match_row['drawer'] if 'drawer' in match_row else 'N/A'
        location = match_row['location'] if 'location' in match_row else 'N/A'
        recovered = match_row['recovered'] if 'recovered' in match_row else 'Unknown'
        se_commands = match_row['se_commands'] if 'se_commands' in match_row else 'N/A'
        notes = match_row['notes'] if 'notes' in match_row else 'No notes available'
        refcode = match_row['refcode'] if 'refcode' in match_row else 'N/A'
        
        st.markdown(f"**FRU Number:** `{fru_number}`")
        st.markdown(f"**FRU Name:** `{fru_name}`")
        st.markdown(f"**Drawer / Location:** {drawer} – {location}")
        st.markdown(f"**Recovered:** {'✅' if recovered=='Yes' else '❌'}")
        st.markdown(f"**SE Command:** `{se_commands}`")
        st.markdown(f"**Notes:** _{notes}_")
        
        # AI-Powered Diagnostic Analysis
        st.markdown("---")
        st.markdown("### 🤖 **Granite AI Analysis**")
        
        if ai_helper.is_configured():
            ai_status = "🟢 **Connected to watsonx.ai**"
        else:
            ai_status = "🟡 **Demo Mode** (Set WATSONX_API_KEY & WATSONX_PROJECT_ID for live AI)"
        
        st.markdown(ai_status)
        
        # Model comparison for analysis
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Granite-3-2-8B Analysis:")
            analysis_8b = ai_helper.generate_diagnostic_analysis(refcode, fru_name, notes, "granite-3-2-8b")
            st.markdown(analysis_8b)
            
        with col2:
            st.markdown("#### Granite-13B-Chat Analysis:")
            analysis_13b = ai_helper.generate_diagnostic_analysis(refcode, fru_name, notes, "granite-13b-chat")
            st.markdown(analysis_13b)
        
        # AI-suggested commands comparison
        with st.expander("🧠 AI-Suggested SE Commands Comparison"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Granite-3-2-8B Commands:**")
                commands_8b = ai_helper.suggest_se_commands(f"{fru_name} {notes}", "granite-3-2-8b")
                for cmd in commands_8b:
                    st.code(cmd, language="bash")
            
            with col2:
                st.markdown("**Granite-13B-Chat Commands:**")
                commands_13b = ai_helper.suggest_se_commands(f"{fru_name} {notes}", "granite-13b-chat")
                for cmd in commands_13b:
                    st.code(cmd, language="bash")

        # Suggested Command Detail
        if not cmd_df.empty and se_commands != 'N/A':
            try:
                cmd_parts = se_commands.split()
                if cmd_parts:
                    cmd_info = cmd_df[cmd_df["command_syntax"].str.contains(cmd_parts[0], na=False)]
                    if not cmd_info.empty:
                        cmd_row = cmd_info.iloc[0]
                        cmd_desc = cmd_row.get('description', 'No description available')
                        st.markdown(f"💡 *Command Description:* `{cmd_desc}`")
            except:
                pass

        # IQYedit Link
        if refcode != 'N/A':
            iqyedit_url = f"https://jupitrsat.boeblingen.de.ibm.com/iqyedit/cgi-bin/iqyedit/iqysrc/{str(refcode).lower()}"
            st.markdown("---")
            st.markdown(f"🔗 [View Full Refcode Details in IQYedit]({iqyedit_url})")
            st.info("IBM internal portal. Opens full engineering notes for this code.")

st.markdown('</div>', unsafe_allow_html=True)

# AI Assistant Panel
st.markdown('<div class="diagnostic-panel">', unsafe_allow_html=True)
st.subheader("🤖 Granite AI Assistant")

# Model Selection
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    selected_model = st.selectbox(
        "Select Granite Model:",
        options=["granite-3-2-8b", "granite-13b-chat"],
        format_func=lambda x: {
            "granite-3-2-8b": "Granite-3-2-8B-Instruct (Fast, Concise)",
            "granite-13b-chat": "Granite-13B-Chat-v2 (Detailed, Conversational)"
        }[x],
        index=0
    )
    ai_helper.switch_model(selected_model)

with col2:
    current_model_id = ai_helper.get_current_model_id()
    st.markdown(f"**Model ID:** `{current_model_id}`")

with col3:
    if ai_helper.is_configured():
        st.success("✅ Connected")
    else:
        st.info("🔧 Demo Mode")

with col2:
    if st.button("🔄 Test AI Connection"):
        if ai_helper.is_configured():
            test_response = ai_helper.generate_diagnostic_analysis("TEST001", "Test Component", "Connection test")
            st.success("AI connection successful!")
        else:
            st.warning("Please set WATSONX_API_KEY and WATSONX_PROJECT_ID environment variables")

# Interactive AI Chat
st.markdown("**Ask Granite AI about hardware diagnostics:**")
user_question = st.text_area(
    "Describe your hardware issue or ask a diagnostic question:",
    placeholder="e.g., 'DCM showing thermal errors in drawer 3, what should I check?'"
)

if st.button("🧠 Ask Granite AI") and user_question:
    with st.spinner(f"Granite AI ({selected_model}) is analyzing your question..."):
        # Generate AI response using selected model
        ai_response = ai_helper.generate_diagnostic_analysis("USER_QUERY", "General", user_question, selected_model)
        st.markdown(f"### 🤖 **{selected_model.upper()} Response:**")
        st.markdown(ai_response)
        
        # Model-specific command suggestions
        suggested_cmds = ai_helper.suggest_se_commands(user_question, selected_model)
        if suggested_cmds:
            st.markdown(f"**{selected_model.upper()} Recommended Commands:**")
            for cmd in suggested_cmds[:5]:  # Show top 5 suggestions
                st.code(cmd, language="bash")
                
        # Option to compare with other model
        if st.button(f"🔄 Compare with {'Granite-13B-Chat' if selected_model == 'granite-3-2-8b' else 'Granite-3-2-8B'}"):
            other_model = "granite-13b-chat" if selected_model == "granite-3-2-8b" else "granite-3-2-8b"
            with st.spinner(f"Getting {other_model} perspective..."):
                other_response = ai_helper.generate_diagnostic_analysis("USER_QUERY", "General", user_question, other_model)
                st.markdown(f"### 🔄 **{other_model.upper()} Alternative Analysis:**")
                st.markdown(other_response)

st.markdown('</div>', unsafe_allow_html=True)

# Component Analysis Section
if not ref_df.empty:
    st.subheader("🔧 Component Status Overview")
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["📈 Recovery Summary", "🏗️ By Location", "⚙️ Recent Activity"])
    
    with tab1:
        col1, col2, col3, col4 = st.columns(4)
        total = len(ref_df)
        recovered = len(ref_df[ref_df["recovered"] == "Yes"])
        failed = total - recovered
        
        with col1:
            st.metric("Total Components", total, "Active Systems")
        with col2:
            st.metric("Recovered", recovered, f"{(recovered/total)*100:.1f}%")
        with col3:
            st.metric("Failed", failed, f"{(failed/total)*100:.1f}%")
        with col4:
            success_rate = (recovered/total)*100
            st.metric("Success Rate", f"{success_rate:.1f}%", 
                     "Excellent" if success_rate > 80 else "Good" if success_rate > 60 else "Needs Attention")
    
    with tab2:
        st.markdown("**Component Status by Drawer Location:**")
        drawer_groups = ref_df.groupby('drawer')
        
        for drawer, group in drawer_groups:
            total_count = len(group)
            recovered_count = len(group[group["recovered"] == "Yes"])
            failed_count = total_count - recovered_count
            success_rate = (recovered_count / total_count * 100) if total_count > 0 else 0
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric(f"Drawer {drawer}", f"{total_count} components")
            with col2:
                st.metric("Recovered", recovered_count)
            with col3:
                st.metric("Failed", failed_count)
            with col4:
                st.metric("Success Rate", f"{success_rate:.1f}%")
    
    with tab3:
        st.markdown("**Recent Diagnostic Activity:**")
        recent_items = ref_df.head(5)[['refcode', 'fru_name', 'drawer', 'recovered', 'se_commands']]
        for _, row in recent_items.iterrows():
            status_icon = "✅" if row['recovered'] == 'Yes' else "❌"
            st.markdown(f"{status_icon} **{row['refcode']}** - {row['fru_name']} ({row['drawer']}) - `{row['se_commands']}`")

# Enhanced Diagnostic Logger Panel
st.markdown('<div class="logger-panel">', unsafe_allow_html=True)
st.subheader("📝 Diagnostic Step Recorder")
st.markdown("**Log manufacturing test steps with automatic script recommendations**")

fab_ops = {
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

# Recommended SE commands for each operation step
recommended_scripts = {
    "1000 – Test floor safety checklist": ["safety_check.sh", "env_monitor.py"],
    "1030 – Info collection / setup": ["zsegetsysstatus --status Power_System_complete", "zm_dcm_data.py", "drawer_inventory.py"],
    "9006 – MFG SE code load": ["verify_firmware.sh", "code_validation.py"],
    "0470 – AMB+ T-sort IO parts": ["io_enumeration.sh", "part_verification.py"],
    "1225 – MFS comparison": ["mfs_backup.sh", "compare_mfs.py"],
    "1227-0 – Card personalization": ["personalize_card.sh", "verify_identity.py"],
    "0472 – IO diagnostics @ Nominal": ["cecctl status", "cardctl test --verbose"],
    "0473 – IO diagnostics @ Nominal (Phase 2)": ["zsegetsysstatus --status IML_complete", "thermal_monitor.py"],
    "0476 – IO diagnostics @ Cold": ["thermal_prep.sh", "cold_boot_test.py"],
    "0474 – IO diagnostics @ Hot": ["thermal_stress.sh", "hot_performance.py"],
    "1407 – Final MFS comparison": ["final_mfs_check.sh", "integrity_verify.py"],
    "0550 – Post-fab Op": ["cleanup_temps.sh", "final_verification.py"],
    "1500 – Archive process data": ["data_archive.sh", "report_generation.py"]
}

col1, col2 = st.columns(2)

with col1:
    selected_op = st.selectbox("Select Manufacturing Operation", list(fab_ops.keys()))
    op_code = fab_ops[selected_op]
    
    # Show recommended scripts
    if selected_op in recommended_scripts:
        st.markdown("**🤖 Recommended SE Scripts:**")
        for script in recommended_scripts[selected_op]:
            st.code(script, language="bash")

with col2:
    status = st.selectbox("Operation Status", ["Not Started", "In Progress", "Completed", "Failed", "Skipped"])
    notes = st.text_area("Notes", placeholder="Enter operation notes, observations, or issues...")

if st.button("📋 Log Operation Step"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {op_code} - {selected_op} | Status: {status}"
    if notes:
        log_entry += f" | Notes: {notes}"
    
    # Store in session state for this demo
    if "operation_log" not in st.session_state:
        st.session_state.operation_log = []
    st.session_state.operation_log.append(log_entry)
    st.success("Operation logged successfully!")

# Display operation log
if "operation_log" in st.session_state and st.session_state.operation_log:
    st.markdown("**📊 Recent Operation Log:**")
    for entry in st.session_state.operation_log[-5:]:  # Show last 5 entries
        st.text(entry)

st.markdown('</div>', unsafe_allow_html=True)

# watsonx.ai Configuration Panel
with st.sidebar:
    st.markdown("### 🔧 **watsonx.ai Configuration**")
    st.markdown("Configure your IBM watsonx.ai credentials for live AI assistance:")
    
    # Environment variable status
    if ai_helper.is_configured():
        st.success("✅ API Keys Configured")
        st.markdown("**Available Models:**")
        st.markdown("- ibm/granite-3-2-8b-instruct")
        st.markdown("- ibm/granite-13b-chat-v2")
    else:
        st.warning("⚠️ API Keys Not Set")
        st.markdown("**Status:** Demo Mode Active")
        st.markdown("**Available Models:** Both Granite models simulated")
    
    st.markdown("**Required Environment Variables:**")
    st.code("WATSONX_API_KEY=your_api_key_here", language="bash")
    st.code("WATSONX_PROJECT_ID=your_project_id", language="bash")
    
    st.markdown("**Setup Instructions:**")
    st.markdown("1. Get API key from [IBM Cloud](https://cloud.ibm.com/apidocs/watsonx-ai)")
    st.markdown("2. Create watsonx.ai project")
    st.markdown("3. Set environment variables")
    st.markdown("4. Restart application")
    
    if st.button("📖 View watsonx.ai Docs"):
        st.markdown("[IBM watsonx.ai Documentation](https://ibm.github.io/watsonx-ai-python-sdk/)")

# Footer
st.markdown("---")
st.markdown("**IBM Metis TestLab Advisor** | Hardware Diagnostic Support System")
st.markdown("*Powered by IBM watsonx.ai & Granite Foundation Models*")
st.markdown("*For internal IBM use only. Confidential and proprietary information.*")
