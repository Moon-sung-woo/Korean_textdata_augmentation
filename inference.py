# data 증폭시키는 소스코드

from eda import EDA
import pandas as pd
import csv

data_path = 'clean_g2pk_forInfer.csv'
save_file_path = 'clean_g2pk_withEDA.csv'
data = pd.read_csv(data_path)

script_data = data['script'].values
label_data = data['label'].values

f = open(save_file_path, 'w', encoding='utf-8')
wr = csv.writer(f)

for script, label in zip(script_data, label_data):

    eda_data = EDA(script)
    for eda in eda_data:
        print(eda)
        wr.writerow([eda, label])
f.close()