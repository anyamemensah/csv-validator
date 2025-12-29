# SDP Data Validation Tool

A simple Streamlit app showcasing how to validate CSV datasets with custom data quality checks, such as expected values, ranges, and other conditions, using Polars and Pandera. This example project demonstrates how to combine modern Python data tools with an interactive UI for efficient and user-friendly data validation.

## Features

* Upload a CSV file via a Streamlit interface.
* Validate:
    * Presence of required columns.
    * Uniformity of the 'school_year' column against user input.
    * Schema compliance using Pandera for Polars.
* Cast boolean columns to proper Boolean type.
* Save validated data to a configured directory.

## Tools

* [Streamlit](https://streamlit.io/): for building the interactive UI.
* [Polars](https://pola.rs/): for DataFrame operations.
* [Pandera](https://pandera.readthedocs.io/): for schema validation.
* YAML: for configuration management.

## Data Source

This project uses data from the [School District of Philadelphia](https://www.philasd.org/research/#opendata) and was lightly cleaned as part of another project.

## How to use

Clone the repository 

```terminal
git clone https://github.com/anyamemensah/csv-validator.git

cd csv-validator
```

Install dependencies

```terminal
uv sync
```

Although the project uses `uv` for dependency management and syncing via pyproject.toml, a `requirements.txt` file is also included for convenience if you prefer using pip:

```terminal
pip install -r requirements.txt
```

Start the Streamlit app:

```terminal
uv run streamlit run app.py
```

Test the app using the sample files in the 'data_raw' folder:

The following file is designed to pass all validation checks:

* sdp_info_2022-2023.csv

The following files are designed to fail validation checks:

* sdp_info_2018-2019_invalid.csv
* sdp_info_2020-2021_invalid.csv
* sdp_info_2023-2024_invalid.csv

