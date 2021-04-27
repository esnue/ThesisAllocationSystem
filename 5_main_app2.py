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
# Areas of Expertise Page
# =============================================================================

def expertise():

	st.title("Areas of Expertise")


# =============================================================================
# Main Page
# =============================================================================

def main():

	# if you want to use your own styling, uncomment the line below and edit a css file
    #local_css("style.css")

	#st.image("thesis.png", width=600)
	activities = ["Home", "About", "Areas of Expertise"]
	choice = st.sidebar.selectbox("Navigation", activities)
	if choice == "Home":
		st.title("Master Thesis Supervisor Recommendation")
		st.write("""\n
		\n
			This is a tool to assist Hertie School students in finding a suitable thesis supervisor. By clicking on the 'See more' button, you will get a comprehensive overview of their individual areas of academic expertise based on their body of publications. 
			You can also access their areas of expertise directly by navigating to the page in the navigation.
			
			Here are your professors: 
			""")
		#column layout (7 rows, 4 cols)
		c1, c2, c3, c4 = st.beta_columns((1, 1, 1, 1))

		#refactor this as loop per row if enough time and motivation

		#Jankin
		c1.header('Slava Jankin')
		c1.image('https://sjankin.github.io/images/profile.jpg')
		c1.write('Professor of Data Science and Public Policy')
		#Expander for more info
		exp = c1.beta_expander('Learn more')
		exp.write('Here comes the visualization')

		#Anheier
		c1.header('Helmut K. Anheier')
		c1.image('https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Anheier/HelmutKAnheier_Copyright_HertieSchool.jpg')
		c1.write('Professor of Sociology')
		#Expander for more info
		exp = c1.beta_expander('Learn more')
		exp.write('Here comes the visualization')

		#Bryson
		c1.header('Joanna Bryson')
		c1.image('https://hertieschool-f4e6.kxcdn.com/fileadmin/user_upload/Joanna_Bryson_800px.jpg')
		c1.write('Professor of Ethics and Technology')
		#Expander for more info
		exp = c1.beta_expander('Learn more')
		exp.write('Here comes the visualization')

		#Graf
		c1.header('Lukas Graf')
		c1.image('https://hertieschool-f4e6.kxcdn.com/fileadmin/user_upload/Lukas_Graf_Copyright_HertieSchoolofGovernance.jpg')
		c1.write('Assistant Professor of Educational Governance')
		#Expander for more info
		exp = c1.beta_expander('Learn more')
		exp.write('Here comes the visualization')

		#Shaikh						
		c1.header('Mujaheed Shaikh')
		c1.image('https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_portraits/Shaikh_press.jpg')
		c1.write('Professor of Health Economics')
		#Expander for more info
		exp = c1.beta_expander('Learn more')
		exp.write('Here comes the visualization')


	elif choice == "About":
		about()
	elif choice == "Areas of Expertise":
		expertise()


if __name__ == "__main__":
    main()