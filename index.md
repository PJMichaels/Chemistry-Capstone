---
title: Main Page
permalink: /
---
# Welcome to the Chemistry Capstone Project:

## Introduction: 

In modeling, users are regularly faced with how to chose between different model types. The general heuristic of selecting the simplest model appropriate for a given task is good, however how does one know what will work best? In the field of drug discovery, advances in automation and high-throughput screening and laboratory techniques have enabled unprecedented creation of datasets. These datasets have fueled a renewed interest and application of data science techniques to understand and extract value. In this project we aim to explore and compare cutting edge models to those that are popular historically. To achive this, we train and evaluate several models against a series of relevant drug discovery datasets. We then take an in-depth look at the model performance for a dataset of compounds for potential alczheimer's treatment. 

### If you are new to chemistry please consider exploring our [Cheminformatics Introduction](Chemistry_Intro/index.md). 

### Abstract:

Model selection is an important aspect to any data science project. With new model frameworks being published regularly, there have been increasing calls for standardized datasets across industries to help compare the results. We herein describe an evaluation of different models of varying complexity in the drug-discovery context. We rely on cheminformatics to process and featurize 6 datasets that cover a range of sizes and drug discovery related tasks. We trained several common classification models as well as a directed message passing neural network from the Chemprop package for each dataset. We then compared the models using a range of metrics and found roc-auc to be the most useful for our examples. From our results, while Chemprop was amongst the highest scoring in all cases, it did not always outperform the simpler models. Therefore, we find that exploring a wide range of models to be prudent in establishing baselines and providing comparative insight. 

### For more details, please click [here](BlogPost.pdf) to view the in-depth technical report.

## Code:

All of the code is available in the linked Git-hub repository. We have included both a set of notebooks that provide visualization and a quick way to explore the results, as well as a end-to-end pipeline which will provide facile duplication of this work. We hope that this pipeline will be of use and can be expanded to include additional featurization, models and datasets in the future. <br><br>

We have also provided a brief [video](https://drive.google.com/file/d/1VzaYKBJP9WgfkLmqmSXuuMPifh6q9_iX/view?usp=sharing) overview and Q&A on this pipeline to help users get started. 

## acknowledgements:

We would like to thank both Dr. Elle O'Brien and Michelle LeBlanc for their continued support and guidance over the course of this project.
