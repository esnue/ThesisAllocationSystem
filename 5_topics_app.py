"""
This module contains the app for Streamlit. 
"""

import streamlit as st
import numpy as np
import os
import pandas as pd

# =============================================================================
# Header and Options
# =============================================================================

st.set_page_config(layout="centered", initial_sidebar_state="auto", page_title="Hertie Thesis Allocation") 
st.set_option('deprecation.showPyplotGlobalUse', False) # suppress depreciation warning

st.title("Hertie School: Supervisors' Areas of Expertise")

# =============================================================================
# Side Bar
# =============================================================================

st.sidebar.subheader("What is this?")
st.sidebar.markdown("This is an app designed to help you match your research proposal with possible thesis supervisors.")

#st.sidebar.subheader("What should I do?")
#st.sidebar.markdown("1. Copy and paste your research proposal in the box. You can also just type your research interests. \n2. A table of professors will pop up in decreasing order of suitability. You can hover over their names to see keywords used by them in their papers.\n3. Click on any professor to see their specific supervision plan.")

st.sidebar.subheader("How does this work?")
st.sidebar.markdown("We used a Deep Learning topic model called [Contexualized Topic Model](https://github.com/MilaNLProc/contextualized-topic-models) to generate topic proportions for each professor based on their published academic papers. \n\nThe papers we sourced from Google Scholar, so that you don't have to go through the tedious work of reading their papers to get a feeling for the match. \n\nThe supervision plans are also available at [MyStudies](https://mystudies.hertie-school.org/en/).")

st.sidebar.subheader("And then?")
#st.sidebar.markdown("You're free to take up the recommendations or to ignore them. :) \n\nWe strongly encourage you use it even if you have a strong preference for a professor already because who knows? Maybe there's a better fit out there! \n\nWe hope that we can help you making your choices for supervisors and wish you the best of luck with your thesis!")
st.sidebar.markdown("You can use the visualizations to get an overview of the topics represented by each supervisor.")

st.sidebar.subheader("Credits")
st.sidebar.markdown("This project would not have been possible without the ground work done by our [fellow students](https://github.com/cbsobral/python).") 

# =============================================================================
# Load Data and Models
# =============================================================================

topics_df_wide = pd.read_csv('data/train-label_wide.csv')
topics_df_long = pd.read_csv('data/train-label_long.csv')

# =============================================================================
# Supervisors Image Buttons
# =============================================================================
supervisors = ['Anheier', 'Bryson', 'Centre for International Security', 'Cali',
              'Cingolani', 'Costello', 'Flachsland', 'Graf', 'Hallerberg',
              'Hammerschmid', 'Hassel', 'Hirth', 'Hustedt','Iacovone',
              'Jachtenfuchs','Jankin', 'Kayser','Kreyenfeld','Mair','Mena',              
              'Mungiu-Pippidi', 'Munzert','Patz','Reh','Roemmele','Shaikh',
              'Snower','Stockmann','Traxler', 'Wegrich']

st.image("img/Anheier.jpg", width=200)

# =============================================================================
# Visualization Topics
# =============================================================================


##

# =============================================================================
# User's Input
# =============================================================================

# Get text from user
#st.markdown("\n")
#st.header("Your Research Proposal")
#ud_text = st.text_area("Type or paste (Ctrl+V) your text and then press `Fetch Matches`.")

# Run comparison
#run_app = st.button('Fetch Matches')

#if not run_app:
#    st.stop()
#else:

#st.bar_chart(topics_df_wide)