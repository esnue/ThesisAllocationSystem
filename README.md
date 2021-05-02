# Supervisor Recommendation Tool for the Hertie School 

This project's goal is to facilitate matching of thesis supervisors with students by improving access to information on areas of expertise that can be covered by the school faculty.

We used a Deep Learning topic model called [Contexualized Topic Model](https://github.com/MilaNLProc/contextualized-topic-models) to generate topic proportions for each professor based on their published academic papers. The papers we sourced from Google Scholar. The supervision plans are also available at [MyStudies](https://mystudies.hertie-school.org/en/).

# Navigation 

We used Google Colab for computation-heavy tasks. These files have an .ipynb-ending and can also be run in Jupyter Notebooks. Moreover, the files are labelled in the order of the working process.

* 1_pdf-to-csv.ipynb: convert multiple raw pdf files to one single csv file. 
* 2_WPpreprocessing.py: simple preprocessing to remove punctuation, common and customized stopwords, etc. 
* 3_contextualized_topic_modeling.ipynb: Deep Learning topic model training, validation and evaluation
* 4_Visualization.ipynb: visualization of model output
* 5_main_app.py: contains code for the streamlit web app  
* Pipfile.lock and Pipfile: necessary components of the streamlit implementation 
* data: final data for streamlit implementation
* .old: bin folder for files that were created during research and exploration process, i.e. zero-shot topic model and DistilBERT model

# Instruction

The required packages can be automatically installed by running the script. Due to GPU constraints, the model was developed in Google Colab. Therefore, we strongly recommend cloning the repository to your local GDrive. 
```
!git clone https://github.com/esnue/ThesisAllocationSystem.git
```
Alternatively, you could open the notebook using the GitHub feature of Google Colab.

![image](https://user-images.githubusercontent.com/60604030/111357666-ce04e180-8689-11eb-992e-30da66470323.png)

Please make sure to upload sample data from [this folder](https://drive.google.com/drive/folders/1ExS7M2OOkbYS5Z5O9pbPbaCpSa0rhGet?usp=sharing). 

To peek at the web app, you'll have to install streamlit. Please follow the [instructions here](https://docs.streamlit.io/en/stable/) to install streamlit.
