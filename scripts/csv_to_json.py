import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:  # 'utf-8-sig' handles BOM
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            input_json = row.get('\ufeffInput', None)  # Remove BOM from key name
            if input_json:
                input_json = input_json.replace('""', '"')  # Fix JSON formatting
                try:
                    input_data = json.loads(input_json)
                    row['Input'] = input_data
                except json.JSONDecodeError:
                    print(f"Error decoding JSON in row: {row}")
                    continue
            data.append(row)

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Example usage
csv_to_json('evaluation_dataset.csv', 'evaluation_dataset.json')
