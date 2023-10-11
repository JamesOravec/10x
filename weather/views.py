from django.shortcuts import render
from django.http import HttpResponse

import os
import json
# TODO: Get is so that we consume data from the data model and follow appropriate patterns, if it makes sense. 
import csv_transformer
import filter_helper


def weather_query_view(request):
    filters = build_filters(request.GET)

    # TODO: Update this to follow a data access pattern. 
    curr_dir = os.path.dirname(__file__)
    csv_relative_path = "../resources/seattle-weather.csv"
    csv_abs_file_path = os.path.join(curr_dir, csv_relative_path)
    weather_data = csv_transformer.csv_file_to_list(csv_abs_file_path)

    # http://127.0.0.1:8000/weather/query?blah=2&foo=3  # TODO: Fails, would need to address so if parameters don't align with columns that it wouldn't fail like it currently does.
    # http://127.0.0.1:8000/weather/query?limit=5               # Works
    # http://127.0.0.1:8000/weather/query?date=2012-06-04       # Works
    # http://127.0.0.1:8000/weather/query?weather=rain          # Works
    # http://127.0.0.1:8000/weather/query?weather=rain&limit=5  # Works

    filtered_data = filter_helper.filter(weather_data, filters)
    output = json.dumps(filtered_data)
    return HttpResponse(output)

def build_filters(request_get):
    filters = []
    for key in request_get:
        filter = []
        filter.append(str(key))
        filter.append(request_get.get(key))
        filters.append(filter)
        print("key: " + str(key) + " value: " + str(request_get.get(key)))
    return filters

