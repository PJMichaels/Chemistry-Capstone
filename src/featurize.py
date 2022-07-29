import yaml
import pandas as pd
from pathlib import Path
from rdkit import Chem
# discussion of circular fingerprints: https://pubs.acs.org/doi/10.1021/ci100050t
from rdkit.Chem import AllChem
import numpy as np
from tqdm import tqdm
tqdm.pandas()


def generate_fingerprint(smiles,radius,bits):
    mol=Chem.MolFromSmiles(smiles)
    fp=AllChem.GetMorganFingerprintAsBitVect(mol,radius,bits)
    return(np.array(fp))


try:
    params = yaml.safe_load(open("params.yaml"))["featurize"]
    gen_params = yaml.safe_load(open("params.yaml"))["general"]
    X_id = gen_params['X']
    y_id = gen_params['y']
    mol_rep = params['mol_representation']
except:
    print('There is a problem during import of params.yaml for featurize.py')
    exit()

###load train and test dfs
prepared_dir = Path.cwd() / 'data' / "prepared"
featurized_dir = Path.cwd() / 'data' / "featurized"

if not featurized_dir.exists():
    featurized_dir.mkdir()

train_df = pd.read_csv(prepared_dir / "train.csv")
test_df = pd.read_csv(prepared_dir / "test.csv")


if "morganfingerprint" in mol_rep:
    _, radius, bits  = mol_rep.split("-")
    radius = int(radius)
    bits = int(bits)
    
    ### do this for train and test
    print("\nFeaturizing Train Data")
    new_train_df = pd.DataFrame([generate_fingerprint(mol,2,1024) for mol in tqdm(train_df[X_id])])
    new_train_df[y_id] = train_df[y_id]
    new_train_df.to_csv(featurized_dir / "train.csv", index=False)
    
    print("\nFeaturizing Test Data")
    new_test_df = pd.DataFrame([generate_fingerprint(mol,2,1024) for mol in tqdm(test_df[X_id])])
    new_test_df[y_id] = test_df[y_id]
    new_test_df.to_csv(featurized_dir / "test.csv", index=False)



###### Some artifact code to clean up later##########################

# X=[generate_fingerprint(mol, radius, bits) for mol in df[X_id]]
# y=df['HIV_active'].to_list()
# print(radius, bits)



###write train and test to csvs



### note that somewhere in YAML feature params, I need to put a boolean that determines
### whether or not to do the featurization, or just pass params into a file for the
### advanced models that do featurization already


#Other fingerprint types to explore? 
#useful example: https://medium.com/@gurkamaldeol/predicting-environmental-carcinogens-with-logistic-regression-knn-gradient-boosting-and-7973f88eb8b3





# AllChem.GetMorganFingerprintAsBitVect(m1,2,nBits=1024)



# X=[generate_fingerprint(mol,2,1024) for mol in df['smiles']]
# y=df['HIV_active'].to_list()

# ### get YAML PARAMS DATASET, Radius, bits
# ### dataset might have to be a prepare-data-step set making sure smiles  is properly labeled
# ### it would also be cool to use the dvc stream feature that checks for the latest/updated dataset...
# # build a test case with HIV data: - eventually just any data set
# radius=2
# bits=1024
# df=pd.read_csv('data_cleaned/HIV.csv')
# df['fp']=df['smiles'].progress_apply(lambda x: generate_fingerprint(x,radius,bits))

# # no need to return things in this, but maybe add a print statement to track in cmdline
# # df.head(2) 

# ### write out intermediate data to "processed.data type format" - maybe in an artifacts folder