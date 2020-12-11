#엑셀 파일의 모든 시트의 데이터 가져오고 csv파일로 저장

import openpyxl
import pandas as pd
import glob
import os
import csv
#from g2pk import G2p

#g2p = G2p()
#print(g2p("어제는 날씨가 맑았는데, 오늘은 흐리다."))

def sum_sheet():
    file_path = 'data/11_09_script3.xlsx'
    output_path = 'new_data/sum_script3.csv'
    sheetList = []

    wb = openpyxl.load_workbook(file_path)

    for name in wb.sheetnames:
        sheetList.append(name)

    print(sheetList)

    xlsx = pd.ExcelFile(file_path)


    datalist = []

    for j, sheet in enumerate(sheetList):
        df = pd.read_excel(xlsx, sheet, header=None) #header를 None으로 하면 맨 윗열을 컬럼명으로 안쓴다.
        df['label'] = j
        #print(df)
        datalist.append(df)

    print(datalist)
    final_df = pd.concat(datalist, ignore_index=True)
    final_df.columns = ['script', 'label']
    final_df.to_csv(output_path, sep=',', index=False, encoding='utf-8')

    test_df = pd.read_csv(output_path)
    print('######################################################################')
    print(test_df)

def sum_csv(input_file, output_file):

    allFile_list = glob.glob(os.path.join(input_file, '*')) #sum_으로 되어있는 파일들을 모은다.
    print(allFile_list)
    allData = []

    for file in allFile_list:
        df = pd.read_csv(file, header=None)
        print(df.head(5))
        allData.append(df)

    dataCombine = pd.concat(allData, axis=0, ignore_index=False)

    #dataCombine.columns = ['Column1', 'Column2'] #컬럼명 추가해 주는 부분

    dataCombine.to_csv(output_file, index=False, encoding='utf-8', header=False) #header = False로 하면 컬럼 이름 저장 안함.

def change_csv():
    input_file = 'sampledata.csv'
    output_file = 'sampledata2.csv'
    df = pd.read_csv(input_file, encoding='cp949')
    df.to_csv(output_file, index=False, encoding='utf-8')

def add_column_name():
    input_file = 'data/clean_v3.csv'
    output_file = 'output_data/clean_v3_forEDA.csv'
    df = pd.read_csv(input_file, encoding='utf-8')
    df.columns = ['Column1', 'Column2']  # 컬럼명 추가해 주는 부분
    df.to_csv(output_file, index=False, encoding='utf-8')

def mix_data(mix_num):
    input_file = 'data/clean_g2pk_EDA_asr_v5.csv'
    output_file = 'mix'

    df = pd.read_csv(input_file)
    df.columns = ['Column1', 'Column2'] #컬럼명 추가해 주는 부분

    for i in range(5):
        df_s = df.loc[df['Column2'] == i, :]

        df_s = df_s.sample(frac=1).reset_index(drop=True) # shuffle

        f = open(output_file + '/mix_data_{}.csv'.format(i), 'w', encoding='utf_8')
        wr = csv.writer(f)

        for j in range(len(df_s) - mix_num + 1):
            n_gram = df_s.iloc[j:j+mix_num, 0]
            new_script = []

            for n_script in n_gram:
                print(n_script)
                new_script.append(n_script)

            print(' '.join(new_script))
            result = ' '.join(new_script)
            wr.writerow([result, i])

        f.close()

    sum_input_path = r'mix' # csv파일들이 있는 디렉토리 위치
    output_path = r'output_data/clean_g2pk_EDA_asr_{}gram_v5.csv'.format(mix_num)
    sum_csv(sum_input_path, output_file=output_path)


# mix_data(mix_num=7)


input_file = r'data'
output_file = r'output_data/sum67_gram_clean_g2pk_EDA_asr_v7.csv'

sum_csv(input_file=input_file, output_file=output_file)

#add_column_name()