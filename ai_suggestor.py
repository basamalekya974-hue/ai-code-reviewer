import streamlit as st
from code_parser import parse_code
from error_detector import detect_errors


st.set_page_config(page_title="AI Code Reviewer", layout="centered")

st.title("AI Code Reviewer")
st.write("Paste your Python code below to analyze errors and get suggestions.")

# Text area
code = st.text_area("Paste your Python code here", height=200)

# Buttons
col1, col2 = st.columns(2)

with col1:
    analyze_clicked = st.button("Analyze Code")

with col2:
    refresh_clicked = st.button("Refresh")

# Session state
if "run" not in st.session_state:
    st.session_state.run = False

if analyze_clicked or refresh_clicked:
    st.session_state.run = True

# Analysis
if st.session_state.run:
    if code.strip():
        # Parsing
        parse_code(code)
        st.success("Code parsed successfully!")

        # Errors
        errors = detect_errors(code)
        if errors:
            st.subheader("Errors / Warnings")
            for err in errors:
                st.warning(err["message"])
        else:
            st.info("No errors found.")

        # AI Suggestions (WITH IMPROVED CODE)
        result = suggest_code(code)

        st.subheader("AI Suggestions")
        for s in result["suggestions"]:
            st.write(f"- {s}")

        st.write("**Improved Code:**")
        st.code(result["improved_code"], language="python")

    else:
        st.warning("Please enter some Python code.")













