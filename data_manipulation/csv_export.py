import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw_data = {
    'first_name' : ['Sagar','Nikhil','Raghwendra','Rajesh'],
    'last_name' : ['Mukherjee','Asati','Tiwari','Ramesh'],
    'age' : [22,23,23,13],
    'gender' : ['M','M','M',np.nan]
}


df = pd.DataFrame(raw_data, columns = ['first_name','last_name','age','gender'])

df.to_csv('data_folder/data.csv')

print(df)