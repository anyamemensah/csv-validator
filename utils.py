import streamlit as st

def app_instructions():
    st.markdown(
        """
        ## Instructions

        Welcome to the SDP Data Validation Tool! This tool is designed to help you check that the SDP data you are uploading is in the correct format and meets all required guidelines.

        Here's what you can expect as you use the tool:

        ### Step 1: Upload Your Data (CSV format)

        Begin by uploading your data in CSV format. Please make sure the file follows the required structure and column headers as described in the documentation.

        ### Step 2: Enter the Data School Year

        You'll be prompted to enter the school year for the data you are uploading, using the `YYYY-YYYY` format.

        ### Step 3: Validation Feedback

        - If your data passes all validation checks, you'll see a series of ✅ check marks letting you know everything looks good.
        - If any data does not pass a check, you'll see a ❌ cross mark symbol. The specific issues will be shown on the screen.

          \n

        If you have questions or need help with the tool, or if you're not sure why your data did not pass, please email [data-team@company.com](data-team@company.com).
        
        ***

        ## Begin validating your data:
        """
)

