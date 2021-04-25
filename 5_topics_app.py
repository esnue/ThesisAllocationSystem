"""
This module contains the app for Streamlit. 
"""

import streamlit as st
import numpy as np
import os
import pandas as pd
import streamlit.components.v1 as components


# =============================================================================
# Header and Options
# =============================================================================

st.set_page_config(layout="centered", initial_sidebar_state="auto", page_title="Hertie Thesis Allocation") 
st.set_option('deprecation.showPyplotGlobalUse', False) # suppress depreciation warning

#st.title("Hertie School: Supervisors' Areas of Expertise")

# =============================================================================
# Side Bar
# =============================================================================
def about():

	st.sidebar.subheader("About")
    st.sidebar.markdown("This app is created by Lena Wagner and Ba Linh Le for the course Natural Language Process with Deep Learning at Hertie School taught by Prof. Dr. Slava Jankin.")

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

	# if you want to use your own styling, uncomment the line below and edit a css file
    # local_css("style.css")
def main():

	#st.image("thesis.png", width=600)
	activities = ["Home", "About"]
	choice = st.sidebar.selectbox("Pick something fun", activities)
	if choice == "Home":
		st.title("Master Thesis Supervisor Recommendation")
		st.write("""Here are your  
			""")
		components.html(
		    """
		    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
		    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
		    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

			<div class="card" style="width: 18rem;">
			  <img class="card-img-top" src="https://sjankin.com/images/profile.jpg" alt="Slava Jankin">
			  <div class="card-body">
			    <h5 class="card-title">Slava Jankin</h5>
			    <p class="card-text">Slava Jankin is Professor of Data Science and Public Policy at the Hertie School. He is the Director of the Hertie School Data Science Lab. His research and teaching is primarily in the field of natural language processing and machine learning.</p>
			    <a href="#" class="btn btn-primary">See more</a>
			  </div>
			</div>
		    """,
		    height=620,
		)
	elif choice == "About":
		about()

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

# =============================================================================
# Call functions
# =============================================================================

if __name__ == "__main__":
    main()