#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import streamlit as st

import os

# Get the path to the static folder
static_folder = os.path.join(os.path.dirname(__file__), "static")

# Specify the relative path to the index.html file
index_html_path = os.path.join(static_folder, "index.html")

# Load the index.html file
with open(index_html_path, "r") as file:
    index_html = file.read()

# Display the index.html file in the Streamlit app
st.markdown(index_html, unsafe_allow_html=True)
