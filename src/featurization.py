import pandas as pd
from rdkit import Chem
# discussion of circular fingerprints: https://pubs.acs.org/doi/10.1021/ci100050t
from rdkit.Chem import AllChem
import numpy as np
from tqdm import tqdm
tqdm.pandas()

### note that somewhere in YAML feature params, I need to put a boolean that determines
### whether or not to do the featurization, or just pass params into a file for the
### advanced models that do featurization already


#Other fingerprint types to explore? 
#useful example: https://medium.com/@gurkamaldeol/predicting-environmental-carcinogens-with-logistic-regression-knn-gradient-boosting-and-7973f88eb8b3

AllChem.GetMorganFingerprintAsBitVect(m1,2,nBits=1024)

def generate_fingerprint(smiles,radius,bits):
    mol=Chem.MolFromSmiles(smiles)
    fp=AllChem.GetMorganFingerprintAsBitVect(mol,radius,bits)
    return(np.array(fp))


### get YAML PARAMS DATASET
dataset_path = "DATASET PLACE HOLDER"


### get YAML PARAMS DATASET, Radius, bits
### dataset might have to be a prepare-data-step set making sure smiles  is properly labeled
### it would also be cool to use the dvc stream feature that checks for the latest/updated dataset...
# build a test case with HIV data: - eventually just any data set
radius=2
bits=1024
df=pd.read_csv('data_cleaned/HIV.csv')
df['fp']=df['smiles'].progress_apply(lambda x: generate_fingerprint(x,radius,bits))

# no need to return things in this, but maybe add a print statement to track in cmdline
# df.head(2) 

### write out intermediate data to "processed.data type format" - maybe in an artifacts folder