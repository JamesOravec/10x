import csv
import json
import os
import pytest
import csv_transformer
import filter_helper

list = None
curr_dir = os.path.dirname(__file__)
# We have a static copy of csv data that will not change for tests. The main resource folder for the app can change freely.
csv_relative_path = "./resources/seattle-weather-for-testing.csv"
csv_abs_file_path = os.path.join(curr_dir, csv_relative_path)
json_relative_path = "./resources/seattle-weather-for-testing.json"
json_abs_file_path = os.path.join(curr_dir, json_relative_path)


# TODO: Not having luck with getting setup to auto run with unit tests. Will need to figure out, in meantime calling method directly for each test.
# @pytest.fixture()
def setup():
    """Method does initial setup to help us with our tests."""
    global list
    global json_data

    csv_transformer.csv_file_to_json_file(csv_abs_file_path, json_abs_file_path)
    list = csv_transformer.csv_file_to_list(
        csv_abs_file_path
    )  # Get CSV Data as List, for easy unit test checks.


def tear_down():
    # TODO: add this back to "setup()" in the `yield` section, so it auto tears down, once its figured out how to auto setup/teardown for tests.
    """Clean up section"""
    os.remove(json_abs_file_path)


def test_seattle_csv_import_record_count():
    """Test import of CSV, verify number of entries aligns with what we expect."""
    setup()
    length = len(list)
    tear_down()
    assert length == 1461


def test_first_record():
    """Test to see all values of specific import are what we expect from the Seattle that we know."""
    setup()
    tear_down()

    assert list[0]["date"] == "2012-01-01"
    assert list[0]["precipitation"] == "0.0"
    assert list[0]["temp_max"] == "12.8"
    assert list[0]["temp_min"] == "5.0"
    assert list[0]["wind"] == "4.7"
    assert list[0]["weather"] == "drizzle"


def test_query_all():
    """Test api call returns all records."""
    setup()
    filters = []  # 1461, since no filter.
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 1461


def test_query_filter_limit_5():
    """Test filter works with limit and returns only 5 records."""
    setup()
    filters = [["limit", "5"]]  # 5
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 5


def test_query_filter_limit_negative1():
    """Test invalid requests return no values."""
    setup()
    filters = [["limit", "-1"]]  # 0
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 0


def test_query_filter_limit_abc():
    """Test invalid requests return no values."""
    setup()
    filters = [["limit", "abc"]]  # Is an invalid number, so should do nothing.
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 1461


def test_query_filter_zero():
    """Test zero value returns no values."""
    setup()
    filters = [["limit", "0"]]  # 0
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 0


def test_query_filter_date():
    """Test filter by Date - Exact Match Only for Exercise, keep generic so will work for any field/value as string value."""
    setup()
    filters = [["date", "2015-12-09"]]  # 1
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 1


def test_query_filter_weather_rain():
    """Test filter by Weather - Exact Match Only for Exercise, keep generic so will work for any field/value as string value."""
    setup()
    filters = [["weather", "rain"]]  # 641
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 641


def test_query_filter_weather_sun():
    """Test filter by Weather - Exact Match Only for Exercise, keep generic so will work for any field/value as string value."""
    setup()
    filters = [["weather", "sun"]]  # 640
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 640


def test_query_filter_weather_fog():
    """Test filter by Weather - Exact Match Only for Exercise, keep generic so will work for any field/value as string value."""
    setup()
    filters = [["weather", "fog"]]  # 101
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 101


def test_query_multi_filter_weather_limit():
    """Test multi filter, exact matches. Weather and Limit."""
    setup()
    filters = [["weather", "rain"], ["limit", "3"]]
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 3


def test_query_multi_filter_weather_limit_with_non_valid_value():
    """Test multi filter, exact matches. Weather and Limit."""
    setup()
    filters = [["weather", "not a valid type"], ["limit", "3"]]
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 0


def test_query_multi_filter_date_weather1():
    """Test multi filter, exact matches. Date and Weather."""
    setup()
    filters = [["date", "2015-12-09"], ["weather", "rain"]]
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 1


def test_query_multi_filter_date_weather2():
    """Test multi filter, exact matches. Date and Weather."""
    setup()
    filters = [
        ["weather", "rain"],
        ["date", "2015-12-09"],
    ]  # Reverse order of filters from test_query_multi_filter_date_weather1()
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 1


def test_query_multi_filter_date_limit_case1():
    """Test multi filter, exact matches. Date and Limit."""
    setup()
    filters = [["date", "2015-12-09"], ["limit", "99"]]
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 1


def test_query_multi_filter_date_limit_case2():
    """Test multi filter, exact matches. Date and Limit."""
    setup()
    filters = [["date", "2015-12-09"], ["limit", "-1"]]
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 0


def test_query_multi_filter_date_limit_case3():
    """Test multi filter, exact matches. Date and Limit."""
    setup()
    filters = [["date", "2015-12-09"], ["limit", "0"]]
    filtered_list = filter_helper.filter(list, filters)
    tear_down()
    assert len(filtered_list) == 0
