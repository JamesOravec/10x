def filter(list, filters):
    """Helper method, which can apply multiple filter criteria and return the filtered results.
    This helper reserves "limit" as reserved word that should not be a field name. If it is, our filter logic will take
    precidence over trying to make a match on that filter.

    Keyword Arguments:
    list -- The unfiltered list
    filters -- A list of filters. Each filter includes two items in the list, the field and the value. Criteria for exact match filtering.

    A filter is in the format of ["field_name", "value"]. Since we support multiple filters, even a single filter must be passed in as a list of filter.
    An example of a single filter is [["weather", "rain"]]
    An example of multiple filters is [["weather", "rain"], ["limit", "3"]]

    Returns:
    A filtered list based on the exact match of criterias/filters.
    """
    # TODO: The above will help meet the requirements, however a real production solution should be more robust over exact matches. E.g. support inequalities and ranges.
    filtered_list = list
    for filter in filters:
        print("filter: " + str(filter))
        # Basic filter validation
        if filter is None or len(filter) != 2:
            continue
        if type(filter[0]) != str or type(filter[1]) != str:
            continue

        if filter[0].lower() != "limit":
            filtered_list = [d for d in filtered_list if d[filter[0]] == filter[1]]
        elif filter[0].lower() == "limit" and is_integer_castable(filter[1]):
            amount = int(filter[1])
            # Baic validation to ensure non-negative number
            if amount < 0:
                amount = 0
            filtered_list = filtered_list[0:amount:]

    return filtered_list


def is_integer_castable(string):
    try:
        int(string)
        return True
    except ValueError:
        return False
    return False
