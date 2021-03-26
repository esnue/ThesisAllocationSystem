# Thesis Allocation System for the Hertie School 

This project's goal is to facilitate easier matching of thesis supervisors with students based on their thesis proposals. The multi-label text classification model is based on pre-trained DistilBERT pretrained and Huggingface Transformers. 

# Navigation 

* preprocessing.ipynb: steps taken to prepare raw PDF data for the model
* BERTopic.ipynb: alternative solution to manual and superficial labelling of the data 
* model.ipynb: model configurations, training and testing

# Instruction

The required packages can be automatically installed by running the script. Due to GPU constraints, the model was developed in Google Colab. Therefore, we strongly recommend cloning the repository to your local GDrive. 
```
!git clone https://github.com/esnue/ThesisAllocationSystem.git
```
Alternatively, you could open the notebook using the GitHub feature of Google Colab.

![image](https://user-images.githubusercontent.com/60604030/111357666-ce04e180-8689-11eb-992e-30da66470323.png)

Please make sure to upload sample data from [this folder](https://drive.google.com/drive/folders/1ExS7M2OOkbYS5Z5O9pbPbaCpSa0rhGet?usp=sharing). 
