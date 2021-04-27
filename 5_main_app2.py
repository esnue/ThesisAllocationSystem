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
		def my_widget(key):
			st.subheader(key)
			st.image('img\jankin.jpg')
			clicked = st.button("Learn more about " + key)

		# This works in the main area
		clicked = my_widget("Slava Jankin")
		
	elif choice == "About":
		about()
	elif choice == "Areas of Expertise":
		expertise()


if __name__ == "__main__":
    main()