from typing import List

def to_csv_file(
    filename: str, 
    headers: List[str], 
    rows: List[List[str]], 
    delimiter: str = ',', 
    new_line: str = '\n'
    ):
    '''
    Gets required data, delimiters and filename as input,
    prints data into csv file
    '''
    with open(filename, 'w') as output_f:

        output_f.write(headers[0])
        for header in headers[1:]:
            output_f.write(f'{delimiter}{header}') # write headers
        output_f.write(new_line)

        for row in rows:
            output_f.write(row[0])
            for item in row[1:]:
                output_f.write(f'{delimiter}{item}')
            output_f.write(new_line)

    output_f.close()

# Входные данные
OUTPUT_FILE = "output.csv"
headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file(OUTPUT_FILE, headers_list, data)
test = [
    'longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,median_house_value\n',
    '-122.050000,37.370000,27.000000,3885.000000,661.000000,1537.000000,606.000000,6.608500,344700.000000\n',
    '-118.300000,34.260000,43.000000,1510.000000,310.000000,809.000000,277.000000,3.599000,176500.000000\n',
    '-117.810000,33.780000,27.000000,3589.000000,507.000000,1484.000000,495.000000,5.793400,270500.000000\n',
    '-118.360000,33.820000,28.000000,67.000000,15.000000,49.000000,11.000000,6.135900,330000.000000\n'
]

with open(OUTPUT_FILE) as output_f:
    i = 0
    for line in output_f:
        assert line == test[i], 'wtf'
        i += 1
        print(line, end="")