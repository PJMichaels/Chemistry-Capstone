### this would be the place to preprocess raw data into a standardized "processed"
### file format.

### it also might be a good place to capture some basic dataset statistics such as 
### how many of each class exist in the labels section, how many training rows there are
### etc...

### it could also be a place to automatically edit/append instructions to the
### YAML params file...

df['HIV_active'].value_counts()

df['HIV_active'].value_counts()/df.shape[0]

### this might be the place that we choose as a YAML parameter, which raw dataset
### we need, and then convert this to a very generic dataset format for all other
### steps