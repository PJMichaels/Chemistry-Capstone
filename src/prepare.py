import yaml
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


try:
    params = yaml.safe_load(open("params.yaml"))["prepare"]
    file_name = params['dataset']
    split = params['split']
    random_seed = params['seed']
except:
    print('There is a problem during import of params.yaml')
    exit()


data_path = Path.cwd() / 'data' / file_name
processed_dir = Path.cwd() / 'data' / "processed"

if not processed_dir.exists():
    processed_dir.mkdir()

if not data_path.exists():
    print(f"Path to data not found:\n\t{data_dir}")
    exit()

# if we end up 
if data_path.suffix == ".csv":
    df = pd.read_csv(data_path)
else:
    print(f'Could not process data format: \n\t{data_path.suffix}')
    exit()

# split dataset to train test
train, test = train_test_split(
    df,
    test_size= split,
    random_state = random_seed
    )
    
print(f"\nDataset split into train:test at ratio of {1 - split}:{split}")
print(f"Row counts are: \nTrain: {len(train)}\nTest: {len(test)}\n")


# write out csvs
train.to_csv(processed_dir / "train.csv", index=False)
test.to_csv(processed_dir / "test.csv", index=False)


# Thoughts for future development:

# - Determine if this is train and test, or train/test and validate
#     - train/test and validate may make more sense which could enable
#       the train.py file to handle the train/test and/or cross validation etc.. 
# - This might be a place to record some dataset statistics for final analysis
#   but this could also be done as part of the eval step after featurization is done
#     - record train vs test datasets

### it also might be a good place to capture some basic dataset statistics such as 
### how many of each class exist in the labels section, how many training rows there are
### etc...

### it could also be a place to automatically edit/append instructions to the
### YAML params file...

# df['HIV_active'].value_counts()

# df['HIV_active'].value_counts()/df.shape[0]