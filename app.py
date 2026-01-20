import streamlit as st
from code_parser import parse_code
from error_detector import detect_errors
from ai_suggestor import suggest_code

st.title("AI Code Reviewer")

code = st.text_area("Paste your Python code here", height=300)

if st.button("Analyze Code"):
    if code.strip():
        result = parse_code(code)

        if result["success"]:
            st.success("Code parsed successfully!")

            errors = detect_errors(code)
            suggestions = suggest_code(code)

            st.subheader("Errors / Warnings")
            if errors:
                for err in errors:
                    st.warning(err["message"])
            else:
                st.write("No unused variables found")

            st.subheader("AI Suggestions")
            st.write(suggestions)

        else:
            st.error(result["error"]["message"])
    else:
        st.warning("Please enter some code first")
