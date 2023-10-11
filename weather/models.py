from django.db import models
import csv_transformer
import os

class WeatherData(models.Model):
    # TODO: Update code to follow the standard pattern for data access, etc. Note sure if these are pure models working with with ORM, etc. If so, this may not align perfectly with the code I wrote, which is more flexible to work with various csvs and not a specific csv layout of columns/fields.

    # curr_dir = os.path.dirname(__file__)
    # csv_relative_path = "../resources/seattle-weather.csv"
    # csv_abs_file_path = os.path.join(curr_dir, csv_relative_path)

    # weather_data = csv_transformer.csv_file_to_list(csv_abs_file_path)
    pass
