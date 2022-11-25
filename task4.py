import json
from typing import List

def csv_to_list_dict(filename: str, delimiter: str = ",", new_line: str = '\n') -> List[dict]:
    print(delimiter)
    output = []
    with open(filename, 'r') as input_f:
        headers = next(input_f).strip(new_line).split(delimiter)
        for line in input_f:
            coords = {header: coord for header, coord in zip(headers, line.strip(new_line).split(delimiter))}
            output.append(coords)
    input_f.close()

    return output

INPUT_FILE = "output.csv"
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))