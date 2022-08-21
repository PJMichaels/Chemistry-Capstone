# University of Michican SIADS 697 & 698 Chemistry-Capstone

Contributers:
<b>Philip Michaels and David Dunstan<b>

## Abstract:

In modeling, users are regularly faced with how to chose between different model types. The general heuristic of selecting the simplest model appropriate for a given task is good, however how does one know what will work best? In the field of drug discovery, advances in automation and high-throughput screening and laboratory techniques have enabled unprecedented creation of datasets. These datasets have fueled a rise in the interest and application of data science techniques to understand and extract value. In this project we aim to explore and compare cutting edge models to those that are popular historically. To achive this, we train and evaluate several models against a series of relevant drug discovery datasets.

## Requirements:

In order to get both the simple and complex models working properly, we generated two environments for this project. The environment for the simple models can be created from the included [requirements.txt](https://github.com/PJMichaels/Chemistry-Capstone/blob/main/requirements.txt) file in this repository. 

The Chemprop environment was created on the University of Michigan Great Lakes cluster as follows. Some more detailed instructions about how we setup the cluster for this project can be found [here](https://github.com/PJMichaels/Chemistry-Capstone/blob/main/Great%20Lakes%20Access%20Instructions.txt)

    $ conda config --add channels conda-forge
    $ conda config --set channel_priority strict
    $ conda create -n chemprop python=3.8 -y
    $ conda init bash
    $ conda activate chemprop
    $ conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch -y
    $ conda install -c conda-forge rdkit -y
    $ pip install git+https://github.com/bp-kelley/descriptastorus
    $ pip install chemprop
    $ conda install -c conda-forge jupyterlab
    $ pip install ipykernel
    $ python -m ipykernel install --user --name=chemprop

Note: This environment can also be created on a non-GPU enabled machine, but the proper version of pytorch should be selected and installed according to the instructions [here](https://pytorch.org/get-started/locally/) 
    
## Overview:

For this project we utilized a blend of several python and shell scripts and notebooks. A flow scheme for our workflow is as follows: 
    
 ![Pipeline](https://user-images.githubusercontent.com/84757402/185464297-184b0268-d1d6-407f-b4fa-49faf03875cd.png)

This repository was designed to easily enable other to reproduce, investigate, and build on this work. While early exploratory work was done in Jupyter notebooks, much of the heavy lifting can now be automatically reproduced by means of a custom pipeline, explained in detail below. The pipeline will allow users to reproduce or iterate on dataset cleaning, data splitting, Sklearn model training, and generation of result files. While the trained models themselves have been left out of this git repository due to storage limitations, this repository does come with a full set of pre-populated evaluation metric files and some visualizations, which can be found in the evaluation directory. While we assume some individuals will want to reproduce the full pipeline, we also made it possible to just iterate on the evaluation portion of the pipeline as well so one could clone this repo, add or remove a new scoring metric, and just reprocess the existing model prediction results.

Chemprop can also be triggered by means of protocols in the Chemprop_Scripts section of this repo, but we encourage individuals to evaluate these scripts using a high performance compute engine. Chemprop was trained using the Greak Lakes Cluster with GPU access and train times still took upwards of 14 hours.

### Overview of Repository Contents:
- src directory: Source code folder containing all pipelines scripts written in python.
- data directory: Contains raw datasets and after pipeline execution also becomes the source of prepared and split datasets.
- evaluation directory: Contains pre-populated results aggregated from a number of combinations of datasets, models, scoring metrics, and splitting parameters. Pipeline execution will also overwrite these result files according to settings in the passed parameter file.
- Simple_Models directory: Contains pre-populated prediction results for a number of different datasets, Sklearn model, and metric combinations. Results get aggregated from here to populate cumulative result files in the evaluation directory. 
- Chemprop_Interpret directory: ????? Dave to write a bit here????
- Chemprop_Scripts directory: ????? Dave to write a bit here????
- Complex_Models directory: Contains pre-populated prediction results for a number of different datasets and metrics produced are the output of a trained Chemprop model. Results get aggregated from here to populate cumulative result files in the evaluation directory. 
- Jupyter Notebooks directory: Notebooks in this directory have been and are intended to be used to learn about this project, as well as evaluate pre-populated results as well as results generated by iterating on training parameters. 
- Jupyter Notebooks/Integrated with pipeline: Contains some early exploration notebooks which have since been integrated into our pipeline. This notebooks are not intended to be run in their current state and location, but are available to explore.
- Great Lakes Access Instructions: A resource we generated as part of this project with instructions for how to get up and running on the Great Lakes Cluster with custom anaconda environments and a git repo. It took us a while to figure out, so we hope it saves someone else a considerable amount of time!
- params.json: This is the default parameter file that the pipeline uses to determine what datasets to process, how to process them, what models to train, what hyperparameters to apply, what random seed to use, and what evaluation metrics to apply.
- params_demo.json: A parameter file containing a subset of the datasets that exist in this project. For someone attempting to clone this repo and execute the pipeline protocol, I highly recommend using this parameter file as a start point and sanity check as it will run in minutes instead of hours.
- requirements.txt: Python package requirements which we recommend installing into an anaconda environment.


# Pipeline User Guide:

If you only want to clone this repository and explore our results, you should start by exploring and running notebooks in the Jupyter Notebooks directory which will read in results pre-populated in the evaluation directory. Cheminformatics_intro.ipynb introduces some useful domain specific concepts, and General_Result_Visuals.ipynb contains an interactive Altair chart that allows you to explore and compare model, dataset, and scoring metric data. This is the most comprehensive visualization for exploring our results.

If you want to reproduce or iterate on our results, you can do so using the automated pipeline, which should be executed via the terminal from the root folder with the following command: (note the example path is for a Windows PC, and will need to be altered depending on your operating system)

$ python src\\process_pipeline.py

By default this pipeline will skip steps that have already been completed, with the exception of the generate evaluation files step.

process_pipeline.py has 3 optional args:
--overwrite or -o: Forces the pipeline to re-process all steps when included
--param_path or -p: Overrides the default params.json file with a parameter.json file of your choosing. Alternative param file must be formatted consistently.
--eval_only or -e: Including this parameter attempts to skip the dataset pre-processing and model training steps of the pipeline. This is most applicable for users who may just want to add or remove a scoring metric. Note that to add a scoring metric beyond the 5 included in our default params.json file will require edits to the evaluate.py file.

We recommend starting to reproduce results by executing the following limited parameter pipeline:

$ python src\\process_pipeline.py --param_file params_demo.json



# Params.json User Guide
The params.json file enables further iteration or modulation of pipeline protocols. It contains 3 main sections.

## params.json ["general"]
### Required:
random_seed: set the random state for all data splitting and model training to enable reproducible results \
split_style: "random" for random splitting or "cluster" for a KNN based unsupervised splitting of train and validate datasets \
validation_percent: percent of data to split off into the validation set \
feature_representation: only morganfingerprint option is available so far, but the two hyphen delimiter numbers can be changed to set the radius (first number), or the number of bits (second number) for chemical featurization (ADD A COUPLE MORE EXAMPLES AND/OR A LINK TO RDKIT PAGE)

## params.json["datasets"]
### Required:
suffix: dataset file suffix that when concatenated to dataset, should represent a dataset file name in the data directory. The only compatible options are ".csv" and ".csv.gz" so far.\
X: Must correspond to a dataset column containing smiles strings \
y: Should correspond to a label binary label column, but can be used in combination with the optional parameter y_process to convert a continuous value to binary classes
### Optional:
short_name: when provide, this will replace the raw dataset name in all pipeline and result artifact files \
y_process: a boolean statement which when provided is used to remap continuous values into a binary 1 or 0 value. This must be formatted such that a value of x would return True. True values are mapped to class 1. \
y_new: provides a new column name for labels in all pipeline and report artifact files

## params.json["models"]
This section enables selection of which models to train against the provided datasets. The model name must match exactly the model class name from Sklearn in order to work, and model dictionary keys must correspond exactly to model class arguements in order for these to work. Currently this is only compatible with the models included in the default params.json file, but this can be easily adapted by adding new import statements into train.py.


# Overview of Results:

To learn more context surrounding this project including inspiration, an introduction to the field of cheminformatics, our results, and suggested next steps you can read our full report here: (LINK TO BLOG POST)

# Link to Detailed Blog and Full Report:

COMBINE THIS SECTION AND SECTION BELOW WITH PREVIOUS SECTION

# Next Steps:



# To do:

Git Hub:
1. Requirements - Done
2. Readme - In progress, need to document code better
3. Testing pipeline/code repository 
4. Clean-up files and remove any old ones - done!

Writing:
1. Model Comparison - Phil in progress - done
2. Discussion - Need results 
3. Editing first pass

Blog Post: 
1. Need to enable Gitpages for our repository (select slate theme)
2. Run this of a second branch gh-pages 
3. Outline - main page - host readme & overview
4. 2nd Page - project inspiration and highlevel results
5. Link to technical report

Video Recording: 
1. Background of project
2. Data spliting overview  
3. Overview of pipeline (how would one run this on their dataset) - ability to quickly test simple models to compare against a more complex result 


