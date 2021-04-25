"""
This module contains the app for Streamlit. 
"""

import numpy as np
import os
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# =============================================================================
# Header and Options
# =============================================================================

st.set_page_config(layout="centered", initial_sidebar_state="auto", page_title="Hertie Supervisor Tool") 

# =============================================================================
# About Page
# =============================================================================

def about():

	st.title("About this Tool")
	st.write('''This is an app designed to help you match your research proposal with possible thesis supervisors by giving you a quick and easy overview over the wide range of academic expertise of supervisors at Hertie.
	We hope to spare you the tedious work of going through each supervision plan, but that you are rather able to narrow down your options. 
	It was created by Lena Wagner and Ba Linh Le for the course Natural Language Processing with Deep Learning taught by Prof. Dr. Slava Jankin.''')
	st.title("How does this work?")
	st.write('''We used a Deep Learning topic model called [Contexualized Topic Model](https://github.com/MilaNLProc/contextualized-topic-models) to generate topic proportions for each professor based on the body of 
	publicy available academic papers. The papers were sourced from Google Scholar. 
	The supervision plans are available at [MyStudies](https://mystudies.hertie-school.org/en/).''')
	st.title("And now?")
	st.write('''
	You can use the different visualizations to get an overview of the topics that were generated from each supervisor's body of research.
	Hopefully, this will make it easier for you to find a thesis supervisor who is suitable for your research proposal.
	''')

# =============================================================================
# Main Page
# =============================================================================

def main():

	# if you want to use your own styling, uncomment the line below and edit a css file
    #local_css("style.css")

	#st.image("thesis.png", width=600)
	activities = ["Home", "About"]
	choice = st.sidebar.selectbox("Navigation", activities)
	if choice == "Home":
		st.title("Master Thesis Supervisor Recommendation")
		st.write("""\n
		\n
			This is a tool to recommend suitable thesis supervisor for Hertie School students.
			
			Here are your professors: 
			""")
		components.html(
		    """
		    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
		    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
		    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

		<style>
			.card img{
				max-width:100%;
				max-height:100%;
				object-fit: contain;
			}
		</style>

		<div class="row">
		<div class="col-sm-6">
			<div class="card" id="jankin" style="width: 18rem;">
				<img class="card-img-top" src="https://sjankin.github.io/images/profile.jpg" alt="Slava Jankin">
				<div class="card-body">
					<h5 class="card-title">Slava Jankin</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Data Science and Public Policy</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm-6">
			<div class="card" id="anheier" style="width: 18rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Anheier/HelmutKAnheier_Copyright_HertieSchool.jpg" alt="Helmut Anheier">
				<div class="card-body">
					<h5 class="card-title">Helmut K. Anheier</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Sociology</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm-6">
			<div class="card" id="bryson" style="width: 18rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/user_upload/Joanna_Bryson_800px.jpg" alt="Joanna Bryson">
				<div class="card-body">
					<h5 class="card-title">Joanna Bryson</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Ethics and Technology</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm-6">
			<div class="card" id="graf" style="width: 18rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/user_upload/Lukas_Graf_Copyright_HertieSchoolofGovernance.jpg" alt="Lukas Graf">
				<div class="card-body">
					<h5 class="card-title">Lukas Graf</h5>
					<h6 class="card-subtitle mb-2 text-muted">Assistant Professor of Educational Governance</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		</div>

		    """,
		    height=620,
		)
	elif choice == "About":
		about()



if __name__ == "__main__":
    main()

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
