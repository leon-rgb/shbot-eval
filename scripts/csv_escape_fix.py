import csv
import re

def escape_json(json_string):
    # Replace " with \\" and then wrap the entire string in escaped quotes
    escaped_json = json_string.replace('"', '\\"')
    return f'"{escaped_json}"'

def correct_escapes_in_csv(input_csv, output_csv):
    with open(input_csv, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_csv, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile, delimiter=';')
        writer = csv.writer(outfile, delimiter=';')

        for row in reader:
            # Correct the JSON escaping in the first column
            row[0] = escape_json(row[0])
            writer.writerow(row)

# Example usage
input_csv = 'evaluation_dataset2.csv'
output_csv = 'output.csv'
correct_escapes_in_csv(input_csv, output_csv)
