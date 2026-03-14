# AI Code Reviewer

AI Code Reviewer is a simple web application built using **Python and Streamlit** that analyzes Python code and provides feedback on possible issues and improvements.

The application allows users to paste Python code into a text area, analyze it, detect certain warnings (such as unused variables), and generate suggestions to improve the code. It also displays an improved version of the code based on basic code quality rules.

---

## Features

- Paste Python code and analyze it instantly
- Detects warnings such as unused variables
- Provides improvement suggestions
- Displays an improved version of the code
- Refresh button to regenerate suggestions
- Simple and interactive Streamlit web interface

---

## Technologies Used

- **Python**
- **Streamlit**
- **AST (Abstract Syntax Tree)** for code parsing
- **GitHub** for version control

---

## Project Structure
# AI Code Reviewer

AI Code Reviewer is a simple web application built using **Python and Streamlit** that analyzes Python code and provides feedback on possible issues and improvements.

The application allows users to paste Python code into a text area, analyze it, detect certain warnings (such as unused variables), and generate suggestions to improve the code. It also displays an improved version of the code based on basic code quality rules.

---

## Features

- Paste Python code and analyze it instantly
- Detects warnings such as unused variables
- Provides improvement suggestions
- Displays an improved version of the code
- Refresh button to regenerate suggestions
- Simple and interactive Streamlit web interface

---

## Technologies Used

- **Python**
- **Streamlit**
- **AST (Abstract Syntax Tree)** for code parsing
- **GitHub** for version control

---

## Project Structure
ai-code-reviewer/
│
├── app.py # Main Streamlit application
├── code_parser.py # Parses Python code using AST
├── error_detector.py # Detects issues like unused variables
├── ai_suggestor.py # Generates suggestions and improved code
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---
## How It Works

1. The user pastes Python code into the text area in the app.
2. The code is parsed using Python's **AST module**.
3. The application detects basic issues such as unused variables.
4. AI suggestions are generated based on simple rule-based logic.
5. The application also displays an improved version of the code.

---

## Running the Application Locally

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run the Streamlit app
streamlit run app.py


The application will open in your browser.

---

## Live Application

You can access the deployed Streamlit application here:

https://ai-code-reviewer-cm3gm8gbcneeyffkalqgdz.streamlit.app/

---

## Author

Alekya Basam
