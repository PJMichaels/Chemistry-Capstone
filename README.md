# University of Michican SIADS 697 & 698 Chemistry-Capstone

Contributers:
<b>Philip Michaels and David Dunstan<b>

## Summary: 

This is for our University of Michigan Masters of Applied Data Science Capstone project. The goal of this project is to produce a browser hosted user-interface, which allows users to evaluate the drug-like properties of chemical entities. Provided values will be made available through a multitude of machine learning models, and possibly known data sources. As a part of this project we aim to allows end users to view the trade-offs of different types of ML approaches for the same prediction tasks, and the associated uncertainty in those predictions. More details to come as this project evolves...

## Abstract:

In modeling, users are regularly faced with how to chose between different model types. The general heuristic of selecting the simplest model appropriate for a given task is good, however how does one know what will work best? In the field of drug discovery, advances in automation and high-throughput screening and laboratory techniques have enabled unprecedented creation of datasets. These datasets have fueled a rise in the interest and application of data science techniques to understand and extract value. In this project we aim to explore and compare cutting edge models to those that are popular historically. To achive this, we train and evaluate several models against a series of relevant drug discovery datasets.  

## Requirements:

In order to get both the simple and complex models working properly, we generated two environments for this project. The environment for the simple models can be created from the included requirements.txt file in this repository. 

The Chemprop environment was created on the University of Michigan Great Lakes cluster as follows. Some more detailed instructions about how we setup the cluster for this project can be found [here](Great Lakes Access Instructions.txt)

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
