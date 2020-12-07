import json
import pandas as pd
import csv

def write_json_file(dataset, filepath, encoding='utf8'):
    with open(filepath, 'w', encoding=encoding) as file:
        file.write(json.dumps(dataset, ensure_ascii=False))

def read_csv_file(input_dir):
    output = []
    f = open(input_dir, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    rdr = list(rdr)
    for line in rdr[1:]:
        output.append(line)
    f.close()
    print(output)
    return output

def make_prediction_file(input_dir, output_dir):
    dataset = read_csv_file(input_dir)
    result = []
    #del dataset[0]
    for idx, line in enumerate(dataset):
        id = idx
        filename = line[0]
        classcode = -1
        if line[1] == '0':
            classcode = '000001'
        elif line[1] == '1':
            classcode = '020121'
        elif line[1] == '2':
            classcode = '02051'
        elif line[1] == '3':
            classcode = '020811'
        elif line[1] == '4':
            classcode = '020819'
        item = {'id': id, 'file_name': filename, 'class_code': classcode}
        result.append(item)
    result = {'annotations': result}
    write_json_file(result, output_dir)

input_dir = '200_label.csv'
output_dir = 'output.json'

make_prediction_file(input_dir, output_dir)