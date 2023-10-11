import csv
import json
import os

def csv_file_to_json_file(csv_file_path, json_file_path, indents=2):
    """Convert a CSV file to JSON file.

    Keyword Arguments:
    csv_file_path -- Absolute file path of source csv file.
    json_file_path -- Absolute file path of output json file.
    indents -- Option, number spaces per indent in your json file.
    """
    list = csv_file_to_list(csv_file_path)
    jsonfile = open(json_file_path, "w")
    json.dump(list, jsonfile, indent=indents)


def csv_file_to_list(csv_file_path):
    """Gets data from a csv file and return it in list format.

    Keyword Arguments:
    csv_file_path -- Absolute file path of source csv file.

    Returns:
    A list with data from csv file.
    """
    # TODO: Although this works, it we need to be made more robust before going into production. Also have little things to clean up, like header versus data.
    csvfile = open(csv_file_path, "r")

    # Build a list of column names dynamically, so will work for any CSV.
    with open(csv_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        col_names = []
        # Get data from first row, then break. TODO: There is a better way to do this, don't like how we have to reference [0] after we do this.
        for row in csv_reader:
            col_names.append(row)
            break
    field_names = col_names[0]

    # Get the data
    reader = csv.DictReader(csvfile, field_names)
    list = []
    for row in reader:
        list.append(row)
    # Remove first row, which are the headers. TODO: This works but should be cleaned up before production.
    list.pop(0)

    return list
