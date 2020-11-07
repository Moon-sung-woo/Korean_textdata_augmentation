#엑셀 파일의 모든 시트의 데이터 가져오고 csv파일로 저장

import openpyxl
import pandas as pd

file_path = 'data/test_script.xlsx'
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
final_df.to_csv('test2.csv', sep=',', index=False, encoding='utf-8')

test_df = pd.read_csv('test2.csv')
print('######################################################################')
print(test_df)


