"""
This module contains the app for Streamlit. 
"""
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import os
import pandas as pd
import itertools
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


		##COL 1 (7 per row)
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

		#Wucherpfennig						
		c1.header('Julian Wucherpfennig')
		c1.image('https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Wucherpfenning/JulianWucherpfennig_Copyright_HertieSchool.jpg')
		c1.write('Professor of International Affairs and Security')
		#Expander for more info
		exp = c1.beta_expander('Learn more')
		exp.write('Here comes the visualization')

		##COL 2 (try out loop)

		prof2 = ['Dennis Snower', 'Christian Traxler', 'Daniela Stockmann', 'Kai Wegrich', 'Başak Çalı', 'Cathryn Costello', 'Luciana Cingolani']

		url2 = ['https://www.ifw-kiel.de/fileadmin/_processed_/9/5/csm_049_GS_PwC_290518_7768_3bf25ae294.jpg', 
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Traxler/ChristianTraxler_Copyright_HertieSchool.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Stockmann/Copyright_DanielaStockmann.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Wegrich/KaiWegrich_Copyright_HertieSchool.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Cali/BasakCali_Copyright_HertieSchool.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/_processed_/3/6/csm_Costello_WEB_size_171cd2cda6.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Cingolani/LucianaCingolani_Copyright_HertieSchool.jpg']

		tl2 = ['Macroeconomics and Sustainability', 'Economics', 'Digital Governance', 'Public Administration and Public Policy', 'International Law',
		'Fundamental Rights', 'Public Administration']

		def fill_col(a,b,c):

			c2.header(a)
			c2.image(b)
			c2.write('Professor of ' + c)
			#Expander for more info
			exp2 = c2.beta_expander('Learn more')
			exp2.write('Here comes the visualization')

		for (d,e,f) in itertools.zip_longest(prof2, url2, tl2):
			fill_col(d,e,f)

		##COL 3
		prof3 = ['Christian Flachsland', 'Mark Hallerberg', 'Gerhard Hammerschmid', 'Anke Hassel', 'Thurid Hustedt', 'Mark Kayser']

		url3 = ['https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Flachsland/ChristianFlachsland_Copyright_HertieSchool.jpg', 
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Hallerberg/MarkHallerberg_Copyright_HertieSchool.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Hammerschmid/GerhardHammerschmid__Copyright_HertieSchool.JPG',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Hassel/AnkeHassel_Copyright_HertieSchool.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Hustedt/ThuridHustedt_Copyright_HertieSchool_ThomasLobenwein.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Kayser/MarkKayser_Copyright_HertieSchool.jpg']

		tl3 = ['Sustainability', 'Public Management and Political Economy', 'Public and Financial Management', 'Public Policy', 'Public Administration and Management', 
		'Applied Methods and Comparative Politics']

		def fill_col(a,b,c):

			c3.header(a)
			c3.image(b)
			c3.write('Professor of ' + c)
			#Expander for more info
			exp3 = c3.beta_expander('Learn more')
			exp3.write('Here comes the visualization')

		for (d,e,f) in itertools.zip_longest(prof3, url3, tl3):
			fill_col(d,e,f)

		#exception: Hirth
		c3.header('Lion Hirth')
		c3.image('https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_portraits/Hirth.jpg')
		c3.write('Assistant Professor of Governance of Digitalisation and Energy Policy')
		#Expander for more info
		exp3 = c3.beta_expander('Learn more')
		exp3.write('Here comes the visualization')

		##COL 4
		prof4 = ['Alina Mungiu-Pippidi','Michaela Kreyenfeld', 'Sébastien Mena', 'Andrea Römmele', 'Johanna Mair', 'Leonardo Iacovone']

		url4 = ['https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Mungiu-Pippidi/AlinaMungiu-Pippidi_Copyright_HertieSchool.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Kreyenfeld/MichaelaKreyenfeld_Copyright_HertieSchool.jpg',
		'https://www.cass.city.ac.uk/__data/assets/image/0003/272487/Mena,-Sebastien.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Roemmele/AndreaRoemmele_Copyright_HertieSchool.jpg',
		'https://hertieschool-f4e6.kxcdn.com/fileadmin/5_WhoWeAre/1_People_directory/Faculty_downloads/Mair/JohannaMair_Copyright_HertieSchool.jpg',
		'https://www.worldbank.org/content/dam/photos/220x220/2019/sep/iacovone_220.jpg'		
		]

		tl4 = ['Democracy Studies', 'Sociology', 'Organization and Governance', 'Communication in Politics and Civil Society',
		'Organization, Strategy and Leadership', 'Economics']

		def fill_col(a,b,c):

			c4.header(a)
			c4.image(b)
			c4.write('Professor of ' + c)
			#Expander for more info
			exp4 = c4.beta_expander('Learn more')
			exp4.write('Here comes the visualization')

		for (d,e,f) in itertools.zip_longest(prof4, url4, tl4):
			fill_col(d,e,f)

		#exception: Munzert
		c4.header('Simon Munzert')
		c4.image('https://simonmunzert.github.io/images/munzertportrait2019.jpg')
		c4.write('Assistant Professor of Data Science and Public Policy')
		#Expander for more info
		exp4 = c4.beta_expander('Learn more')
		exp4.write('Here comes the visualization')

	elif choice == "About":
		about()
	elif choice == "Areas of Expertise":
		expertise()


if __name__ == "__main__":
    main()
