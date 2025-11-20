# Read the csv file
import csv

def read_csv(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

# Parse the csv lines into rows and columns

def parse_csv(lines, delimiter=','):
    data = []
    for line in lines:
        row = line.strip().split(delimiter)
        data.append(row)
    return data

# Combine it all

def load_csv(filepath, delimiter=','):
    lines = read_csv(filepath)
    return parse_csv(lines, delimiter)

def load_csv_using_csv_module(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

if __name__ == "__main__":
    filepath = 'data.csv'
    data = load_csv(filepath)
    data2 = load_csv_using_csv_module(filepath)
    print("Custom Parser Output:")
    for row in data:
        print(row)
    print("\nCSV Module Output:")
    for row in data2:
        print(row)

