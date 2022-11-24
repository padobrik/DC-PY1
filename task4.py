import json
from typing import List

INPUT_FILE = "output.csv"


def csv_to_list_dict(delimiter: str = ',', new_line: str = '\n') -> List[dict]:
    output = []
    with open('output.csv', 'r') as input_f:
        headers = next(input_f).strip(new_line).split(',')
        for line in input_f:
            coords = {header: coord for header, coord in zip(headers, line.strip(new_line).split(','))}
            output.append(coords)
    input_f.close()

    return output



print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))