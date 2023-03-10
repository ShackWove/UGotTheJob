import pandas as pd
import seaborn as sbs
import numpy as np

dataFrame = pd.read_csv("Job_Placement_Data.csv")
dataFrame = pd.get_dummies(dataFrame, columns=['gender'])
print(dataFrame['gender'])