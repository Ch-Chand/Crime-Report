import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

df = pd.read_csv("C:/Users/Ch Chand/Downloads/Compressed/2020-01/1.csv");
data = df[['Crime ID', 'Month', 'Longitude', 'Latitude', 'Location', 'LSOA code', 'Crime type']];
print(data);