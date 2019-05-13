# Clustering_BreastCancer
Unsupervised analysis to cluster breast cancer

## Description
This work is part of my capstone project 'Machine Learning Engineer Nanodegree' at Udacity (Dec, 2017).
I performed an unsupervised analysis to cluster breast cancer using the dataset, pam50 protein levels, described in the paper:
'Proteogenomics connects somatic mutations to signalling in breast cancer’. Philipp Mertins and co.Nature. 2016. 
The dataset is also posted in Kaggle.

The project is written in Python and can be run using notebook:                                                
          **'clustering_kmeans_pca.ipynb'**. 


#### Following files contain the data:
'data_analysis.csv': normalized protein levels of the pam50 genes                                                            
'protein_description.csv': description of the complete proteins dataset 

#### Procedures:
'procedures_cluster.py': procedure to apply silhouette analysis, which is an adaptation of the one shown by scikit-learn.org 
'pca.py': procedure to apply Principal components analysis
