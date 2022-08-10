from rdkit.Chem import AllChem
from rdkit import Chem

def generate_fingerprint(smiles,radius,bits):
    '''
    This function takes a smiles, radius and number of bits 
    and will return a morgan fingerprint as a numpy array.
    
    If the fingerprint fails due to valency errors etc. it will return
    np.nan and print the smiles that failed for debugging.
    
    For a more elaborate discussion of morgan fingerpritns see:https://pubs.acs.org/doi/10.1021/ci100050t
    '''
    try:
        mol=Chem.MolFromSmiles(smiles)
        fp=AllChem.GetMorganFingerprintAsBitVect(mol,radius,bits)
        return(np.array(fp))
    except:
        print(f'{smiles} failed in RDkit')
        return (np.nan)