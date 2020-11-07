# data 증폭시키는 소스코드

from eda import EDA
import pandas as pd
import csv

data_path = 'test2.csv'
save_file_path = 'final_script.csv'
data = pd.read_csv(data_path)

script_data = data['script'].values
label_data = data['label'].values

f = open(save_file_path, 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(["script", "label"])
for script, label in zip(script_data, label_data):
    #print(script, label)
    #print(EDA(script))
    eda_data = EDA(script)
    for eda in eda_data:
        print(eda)
        wr.writerow([eda, label])
f.close()

df = pd.read_csv('final_script.csv', sep=',')
df = df.drop_duplicates(['script'], keep="last").value_counts()
print(df)