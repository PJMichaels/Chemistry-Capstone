from pathlib import Path
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.cluster import MiniBatchKMeans
from utils.generate_morgan_fp import generate_fingerprint


def split_dfs(file_list: list, split_style: str, validation_percent: float, random_seed: int, feature_representation: str, overwrite: bool = False) -> list:
    '''
    Splits a dataframe into train and validate sets by either Random or Cluster methods
    
    Args:
        file_list: A list of paths to pre-prepared datasets
        split_style: (str) Can be "random" or "cluster" where cluster is a mini-batch split for unbalanced datasets
        validation_percent: (float) Should be a float between between 0 and 1
        random_seed: (int) The random state argument for splitting and clustering functions, which enables reproducibility.
        overwrite: (bool) If true existing files are overwritten/re-featurized-split

    Returns a list of tuples where each tuple contains the datasets train and validate paths
    '''

    print("\nInitiating featurization and splitting of dataset(s)")

    split_paths = []
    steps_skipped = False

    if "morganfingerprint" in feature_representation:
        _, radius, bits = tuple(feature_representation.split("-"))

    split_dir = Path.cwd() / "data" / "split"

    if not split_dir.exists():
        split_dir.mkdir()
        print(f"Making output directory: {split_dir}")

    
    for dataset_path in file_list:
        
        ### assign train and validate output paths
        input_path = Path(dataset_path)
        train_path = split_dir / (input_path.name.replace(".csv", f"-{split_style}-train.csv"))
        validate_path = split_dir / (input_path.name.replace(".csv", f"-{split_style}-validate.csv"))

        if (not train_path.exists() and not validate_path.exists()) or overwrite == True:

            print(f"\nGenerating train and test datasets for {input_path}")

            df = pd.read_csv(input_path)

            ### generate morgan fingerprint features and drop values that couldn't be represented
            df['fp'] = df['smiles'].apply(lambda x: generate_fingerprint(x,int(radius),int(bits)))
            df.dropna(subset=["fp"],inplace=True)

            if split_style == "random":
                train_df, validate_df = train_test_split(df, test_size= validation_percent, random_state=random_seed)
        
            if split_style == "cluster":

                ### perform clustering and assign labels to molecules
                clusters=int(df.shape[0]/30)
                kmeans = MiniBatchKMeans(n_clusters=clusters, random_state= random_seed, batch_size=100)
                kmeans.fit(df['fp'].to_list())
                df['cluster']=kmeans.labels_

                # add these clusters to two groups, train and val:
                val_size = validation_percent*len(df)
                train_df = pd.DataFrame()
                validate_df = pd.DataFrame()
                for group, dataframe in df.groupby('cluster'):
                    if dataframe.shape[0] > val_size / 2:
                        train_df = pd.concat([train_df,dataframe])
                    elif len(validate_df) + len(dataframe) <= val_size:
                        validate_df = pd.concat([validate_df,dataframe])
                    else:
                        train_df = pd.concat([train_df,dataframe])

            train_df.to_csv(train_path, index = False)
            validate_df.to_csv(validate_path, index = False)

        else:
            print(f"Train and Validate datasets already exist for {input_path.name}")
            steps_skipped = True

        split_paths.append((str(train_path), str(validate_path)))

    ### output a reminder that you can use overwrite arg
    if steps_skipped:
        print("\nSkipped steps can be reprocessed by including --overwrite parameter")

    return split_paths

