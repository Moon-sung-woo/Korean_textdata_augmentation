# data 증폭시키는 소스코드

from eda import EDA
import pandas as pd
import csv

data_path = 'data/clean_data_forEDA.csv'
save_file_path = 'output_data/EDA_data.csv'

data = pd.read_csv(data_path)

#data.columns = ['Column1', 'Column2'] #컬럼명 추가해 주는 부분

script_data = data['Column1'].values
label_data = data['Column2'].values

f = open(save_file_path, 'w', encoding='utf-8')
wr = csv.writer(f)

for script, label in zip(script_data, label_data):

    eda_data = EDA(script)
    for eda in eda_data:
        print(eda)
        wr.writerow([eda, label])
f.close()