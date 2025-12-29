import os
import yaml
import polars as pl
import streamlit as st
import pandera.polars as pa
from schema import DataSchema
from utils import app_instructions

with open("config.yml", "r") as file:
    params = yaml.safe_load(file)
    required_cols = params["required_cols"]
    school_year_col = params["school_year_col"]
    data_valid_dir = params["data_valid_dir"]
    bools_cols = params["bool_cols"]

st.set_page_config(page_title="SDP Data Validation", layout="wide")
st.title("SDP Data Validation Tool")
app_instructions()

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    st.success(f"File uploaded successfully! ✅")

    # Make 'data_valid' directory if it doesn't exist
    if not os.path.exists(data_valid_dir):
        os.makedirs(data_valid_dir, exist_ok = True)

    # Read CSV into Polars DataFrame
    df = pl.read_csv(uploaded_file)
     
    # Prep for pre-validation checks
    current_cols = df.columns
    school_year_expected = st.text_input(f"Enter the school year for which you are uploading data in the format 'YYYY-YYYY'.", "")

    if st.button("Validate"):
        # Check 1: Validate all required columns are present 
        missing_cols = set(required_cols) - set(df.columns)
        if missing_cols:
            st.error(
                f"Validation failed. ❌  \n"
                f"The following columns are missing from the dataset:  \n"
                f"{', '.join(missing_cols)}"
            )
            st.stop()
        else:
            st.success(f"All required columns are present in the dataset! ✅")
            st.info(f"Proceeding to check the {school_year_col} column...")

        # Check 2: Validate the 'school_year' column 
        # (all values must be identical and equal to 'school_year_expected')
        unique_vals_list = df.select(pl.col(school_year_col).unique()).to_series().to_list()
        is_uniform = all(val == school_year_expected for val in unique_vals_list)

        if len(unique_vals_list) != 1 or not is_uniform:
            st.error(f"Validation failed. ❌  \n"
                     f"All values in the '{school_year_col}' column do not equal '{school_year_expected}'.  \n"
                     f"The following unique values were found in '{school_year_col}':  \n"
                     f"'{', '.join(unique_vals_list)}'.")
            st.stop()
        else:
            st.success(f"All values in '{school_year_col}' equal '{school_year_expected}'! ✅")
            st.info(f"Proceeding with schema validation...")
        
        # Check 3: Validate 'df'; a Polars Data Frame
        try:
            validated_df = DataSchema.validate(df, lazy=True)
        except pa.errors.SchemaErrors as exc:
            st.error(f"Validation failed. ❌  \nSchema errors and failure cases:")
            all_failures = exc.failure_cases
            st.dataframe(all_failures) 
        else:
            # If sucessful, cast 'bools_cols' to true boolean, 
            # (input values are 0/1) and write to 'data_valid_dir'
            st.success("All schema validation checks passed! ✅")
            df_valid = df.with_columns(pl.col(bools_cols).cast(pl.Boolean))
            filename = "".join(["sdp_info_", school_year_expected, "_valid.csv"])
            df_valid.write_csv(file = os.path.join(data_valid_dir, filename))
            st.success("Data upload successful! ✅")
            st.info("The file has been saved to the validation directory.")

