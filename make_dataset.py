#엑셀 파일의 모든 시트의 데이터 가져오고 csv파일로 저장

import openpyxl
import pandas as pd
import glob
import os

def sum_sheet():
    file_path = 'data/11_08_script2.xlsx'
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
    final_df.to_csv('sum_script2.csv', sep=',', index=False, encoding='utf-8')

    test_df = pd.read_csv('sum_script2.csv')
    print('######################################################################')
    print(test_df)

def sum_csv():
    input_file = r'new_data' # csv파일들이 있는 디렉토리 위치
    output_file = r'total_data.csv'

    allFile_list = glob.glob(os.path.join(input_file, 'sum_*')) #sum_으로 되어있는 파일들을 모은다.
    print(allFile_list)
    allData = []

    for file in allFile_list:
        df = pd.read_csv(file)
        allData.append(df)

    dataCombine = pd.concat(allData, axis=0, ignore_index=True)

    dataCombine.to_csv(output_file, index=False, encoding='utf-8')

#sum_sheet()
sum_csv()