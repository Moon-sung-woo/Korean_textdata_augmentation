import pandas as pd

def split_csv(input_path, output_path):

    df = pd.read_csv(input_path)

    for i in range(2):
        df_s = df.loc[df['id'] == i, :]
        df_s.to_csv(output_path + '/nlp_output_{}.csv'.format(i), sep=',', index=False)

input_path = 'data/nlp_output_sample.csv'
output_path = 'data'

split_csv(input_path, output_path)