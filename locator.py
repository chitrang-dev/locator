import streamlit as st
import pandas as pd
import duckdb

con = duckdb.connect(database=':memory:', read_only=False)

st.set_page_config(page_title="Infusion Center Search by Zip", page_icon="", layout="centered", initial_sidebar_state="expanded")

st.header("Infusion Center Search", divider="gray")

# Input field for search terms
search_term = st.text_input("Zip Code:")

# Function to retrieve results from API
# Display results in a table
zip = ''

if search_term:
    zip = search_term.split()[0]
    # todo: parse 
    # city = 
    # state =

    results = con.query(f"SELECT hco_name_cda__v, address_line_1__v, postal_code__v, latitude__v, longitude__v FROM cd_hco.csv WHERE postal_code__v like '{zip}%'")
    st.map(results, latitude='latitude__v', longitude='longitude__v')
    st.dataframe(results)

    st.divider()

