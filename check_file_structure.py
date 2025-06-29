import os
import pandas as pd

# Expected file paths
expected_files = {
    "refcode_fru_map.csv": "data/refcode_fru_map.csv",
    "metis_model_rules.csv": "data/metis_model_rules.csv",
    "se_command_library.csv": "data/se_command_library.csv",
    "ibm_logo.png": "static/ibm_logo.png",
    "sample_output.txt": "static/sample_output.txt"
}

print("\n🔍 Verifying TestLabAdvisor File Structure...\n")

# Check folders
for folder in ["data", "static"]:
    if not os.path.isdir(folder):
        print(f"❌ Folder missing: {folder}/")
    else:
        print(f"✅ Folder exists: {folder}/")

print("\n📦 Checking Required Files:\n")

# Check files
for label, path in expected_files.items():
    if os.path.isfile(path):
        try:
            if path.endswith(".csv"):
                df = pd.read_csv(path)
                print(f"✅ {label} found — {len(df)} rows")
            elif path.endswith(".txt"):
                with open(path, "r") as f:
                    preview = f.readline().strip()
                print(f"✅ {label} found — begins with: '{preview[:50]}...'")
            elif path.endswith(".png"):
                print(f"✅ {label} found (image)")
        except Exception as e:
            print(f"⚠️  {label} exists but failed to load: {e}")
    else:
        print(f"❌ Missing: {label}")

print("\n📊 Structure check complete.")
