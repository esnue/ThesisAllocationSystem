"""
This module contains the app for Streamlit. 
"""

import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import os
import pandas as pd
# =============================================================================
# Header and Options
# =============================================================================

st.set_page_config(layout="wide", initial_sidebar_state="auto", page_title="Hertie Supervisor Tool") 

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
			This is a tool to assist Hertie School students in finding a suitable thesis supervisor. By clicking on the 'See more' button, you will get a comprehensive overview of their individual areas of academic expertise.
			
			Here are your professors: 
			""")
		components.html(
		    """
		    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
		    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
		    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

		<style>

			.card-img-top {
				width: 100%;
    			height: 15vw;
    			object-fit: cover;
			}
		</style>

		<div class="row">
		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://sjankin.github.io/images/profile.jpg" alt="Slava Jankin">
				<div class="card-body">
					<h5 class="card-title">Slava Jankin</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Data Science and Public Policy</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Anheier/HelmutKAnheier_Copyright_HertieSchool.jpg" alt="Helmut Anheier">
				<div class="card-body">
					<h5 class="card-title">Helmut K. Anheier</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Sociology</h6>					
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/user_upload/Joanna_Bryson_800px.jpg" alt="Joanna Bryson">
				<div class="card-body">
					<h5 class="card-title">Joanna Bryson</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Ethics and Technology</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/user_upload/Lukas_Graf_Copyright_HertieSchoolofGovernance.jpg" alt="Lukas Graf">
				<div class="card-body">
					<h5 class="card-title">Lukas Graf</h5>
					<h6 class="card-subtitle mb-2 text-muted">Assistant Professor of Educational Governance</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_portraits/Shaikh_press.jpg" alt="Mujaheed Shaikh">
				<div class="card-body">
					<h5 class="card-title">Mujaheed Shaikh</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Health Economics</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://eu.daad.de/medien/eu.daad.de.2016/dokumente/die-nationale-agentur/30-jahre-erasmus/alumni/profilfoto_patz._300x300jpg.jpg" alt="Ronny Patz">
				<div class="card-body">
					<h5 class="card-title">Ronny Patz</h5>
					<h6 class="card-subtitle mb-2 text-muted">Lecturer of International Political Economy</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Wucherpfenning/JulianWucherpfennig_Copyright_HertieSchool.jpg" alt="Julian Wucherpfennig">
				<div class="card-body">
					<h5 class="card-title">Julian Wucherpfennig</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of International Affairs and Security</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://www.ifw-kiel.de/fileadmin/_processed_/9/5/csm_049_GS_PwC_290518_7768_3bf25ae294.jpg" alt="Dennis Snower">
				<div class="card-body">
					<h5 class="card-title">Dennis Snower</h5>
					<h6 class="card-subtitle mb-2 text-muted">Senior Professor of Macroeconomics and Sustainability </h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Traxler/ChristianTraxler_Copyright_HertieSchool.jpg" alt="Christian Traxler">
				<div class="card-body">
					<h5 class="card-title">Christian Traxler</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Economics</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Stockmann/Copyright_DanielaStockmann.jpg" alt="Daniela Stockmann">
				<div class="card-body">
					<h5 class="card-title">Daniela Stockmann</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Digital Governance</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Wegrich/KaiWegrich_Copyright_HertieSchool.jpg" alt="Kai Wegrich">
				<div class="card-body">
					<h5 class="card-title">Kai Wegrich</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Public Administration and Public Policy</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Cali/BasakCali_Copyright_HertieSchool.jpg" alt="Başak Çalı">
				<div class="card-body">
					<h5 class="card-title">Başak Çalı</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of International Law</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>
		
		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/_processed_/3/6/csm_Costello_WEB_size_171cd2cda6.jpg" alt="Cathryn Costello">
				<div class="card-body">
					<h5 class="card-title">Cathryn Costello</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Fundamental Rights</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Cingolani/LucianaCingolani_Copyright_HertieSchool.jpg" alt="Luciana Cingolani">
				<div class="card-body">
					<h5 class="card-title">Luciana Cingolani</h5>
					<h6 class="card-subtitle mb-2 text-muted">Assistant Professor of Public Administration</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Flachsland/ChristianFlachsland_Copyright_HertieSchool.jpg" alt="Christian Flachsland">
				<div class="card-body">
					<h5 class="card-title">Christian Flachsland</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Sustainability</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>

		<div class="col-sm">
			<div class="card h-100" style="width: 13rem;">
				<img class="card-img-top" src="https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Hallerberg/MarkHallerberg_Copyright_HertieSchool.jpg" alt="Mark Hallerberg">
				<div class="card-body">
					<h5 class="card-title">Mark Hallerberg</h5>
					<h6 class="card-subtitle mb-2 text-muted">Professor of Public Management and Political Economy</h6>
					<a href="#" class="btn btn-primary">See more</a>
				</div>
			</div>
		</div>					

		</div>

		    """,
		    height=3000,
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
