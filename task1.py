from pprint import pprint

output = []

for i in range(0, 16):
    convert = {'bin': bin(i), 'dec': i, 'oct': oct(i), 'hex': hex(i)}
    output.append(convert)

test = [{'bin': '0b0', 'dec': 0, 'hex': '0x0', 'oct': '0o0'},
 {'bin': '0b1', 'dec': 1, 'hex': '0x1', 'oct': '0o1'},
 {'bin': '0b10', 'dec': 2, 'hex': '0x2', 'oct': '0o2'},
 {'bin': '0b11', 'dec': 3, 'hex': '0x3', 'oct': '0o3'},
 {'bin': '0b100', 'dec': 4, 'hex': '0x4', 'oct': '0o4'},
 {'bin': '0b101', 'dec': 5, 'hex': '0x5', 'oct': '0o5'},
 {'bin': '0b110', 'dec': 6, 'hex': '0x6', 'oct': '0o6'},
 {'bin': '0b111', 'dec': 7, 'hex': '0x7', 'oct': '0o7'},
 {'bin': '0b1000', 'dec': 8, 'hex': '0x8', 'oct': '0o10'},
 {'bin': '0b1001', 'dec': 9, 'hex': '0x9', 'oct': '0o11'},
 {'bin': '0b1010', 'dec': 10, 'hex': '0xa', 'oct': '0o12'},
 {'bin': '0b1011', 'dec': 11, 'hex': '0xb', 'oct': '0o13'},
 {'bin': '0b1100', 'dec': 12, 'hex': '0xc', 'oct': '0o14'},
 {'bin': '0b1101', 'dec': 13, 'hex': '0xd', 'oct': '0o15'},
 {'bin': '0b1110', 'dec': 14, 'hex': '0xe', 'oct': '0o16'},
 {'bin': '0b1111', 'dec': 15, 'hex': '0xf', 'oct': '0o17'}]

assert output == test, 'Ожидалось совпадение с переменной test'

pprint(output)