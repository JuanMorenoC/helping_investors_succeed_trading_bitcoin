# Library imports
# Data treatment
# ==============================================================================
import numpy as np
import pandas as pd

# Dataset reading and obtaining information on dataset size, type of variables and missing data in the dataset
data = pd.read_csv("training_set.csv", sep=",")
print("dataset size")
data.shape
print("dataset information")
data.info()
print("check missing data")
data.isna().sum().sort_values()