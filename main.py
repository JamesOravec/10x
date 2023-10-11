import csv_transformer
import filter_helper
import os
import json

######
# This file is used as a sandbox I used for testing various modules/commands, etc. The various things here eventually made their way to other files and/or tests.
# Keeping as a reference for myself, in case I decide to continue playing with this more as a side project.
######
curr_dir = os.path.dirname(__file__)

# CSV to JSON file.
csv_relative_path = "./resources/seattle-weather.csv"
csv_abs_file_path = os.path.join(curr_dir, csv_relative_path)
json_relative_path = "./resources/seattle-weather.json"
json_abs_file_path = os.path.join(curr_dir, json_relative_path)
csv_transformer.csv_file_to_json_file(csv_abs_file_path, json_abs_file_path)

# Get CSV as List
list = csv_transformer.csv_file_to_list(csv_abs_file_path)

# Filtering Tests
# Manual filtering tests. 
filtered_list = [d for d in list if d["weather"] == "rain"]
# # print(filtered_list)
# print(filtered_list[0])

filtered_list2 = [d for d in list if d["date"] == "2015-12-09"]
# print("2:" + str(filtered_list2))

# # Test Negative to get empty list. 
# filtered_list3 = [d for d in list if d["date"] == "2015-12-09asdfdasf"]
# print("3:" + str(filtered_list3))

# Single Filter Test
filters0 = []   # 1461, since no filter.
filters1 = [["weather", "rain"]]    #641
filters1a = [["weather", "sun"]]    #640
filters1b = [["weather", "fog"]]    #101
filters2 = [["date", "2015-12-09"]] #1
filters3 = [["limit", "5"]]         #5

# Multi Filter Test
filters4 = [["weather", "rain"], ["limit", "3"]]            # 3
filters4a = [["weather", "not a valid type"], ["limit", "3"]]

filters5 = [["date", "2015-12-09"], ["weather", "rain"]]
filters6 = [["date", "2015-12-09"], ["limit", "99"]]        # Ensure we don't break anything if we put a split larger than the size.

filters7a = [["date", "2015-12-09"], ["limit", "-1"]]       # 0
filters7b = [["date", "2015-12-09"], ["limit", "0"]]        # 0

# output1 = filter_helper.filter(list, filters1)
# print("output1: " + str(output1))
# print(len(output1))         # 641
# print("*********")

# output1a = filter_helper.filter(list, filters1a)
# print("output1a: " + str(output1a))
# print(len(output1a))      # 640
# print("*********")        

# output1b = filter_helper.filter(list, filters1b)
# print("output1b: " + str(output1b))
# print(len(output1b))      # 101
# print("*********")

# output2 = filter_helper.filter(list, filters2)
# print("output2: " + str(output2))
# print(len(output2))      # 1
# print("*********")

# output3 = filter_helper.filter(list, filters3)
# print("output3: " + str(output3))
# print(len(output3))      # 5

# output4 = filter_helper.filter(list, filters4)
# print("output4: " + str(output4))
# print(len(output4))      # 3

# output4a = filter_helper.filter(list, filters4a)
# print("output4a: " + str(output4a))
# print(len(output4a))      # 0

# output0 = filter_helper.filter(list, filters0)
# print("output0: " + str(output0))
# print(len(output0))      # 0

# output5 = filter_helper.filter(list, filters5)
# print("output5: " + str(output5))
# print(len(output5))      # 1

# output6 = filter_helper.filter(list, filters6)
# print("output6: " + str(output6))
# print(len(output6))      # 1

output7a = filter_helper.filter(list, filters7a)
print("output7a: " + str(output7a))
print(len(output7a))      # 0

output7b = filter_helper.filter(list, filters7b)
print("output7b: " + str(output7b))
print(len(output7b))      # 0

