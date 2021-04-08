from data import *

def sum(values):
    """
    :param values: a list of floats
    :return: the sum of all numbers in values
    """
    answer = 0
    for value in values:
        answer += value
    return answer


def mean(values):
    """
    :param values: a list of floats
    :return: the mean of all numbers in values
    """
    return int(len(values) > 0) and sum(values) / len(values)


def median(values):
    """
    :param values: a list of floats
    :return: the median of all numbers in values
    """
    sorted_values = sorted(values)
    n = len(sorted_values)
    return (sorted_values[n // 2 - (n%2 == 0)] + sorted_values[n // 2]) / 2


def population_statistics(feature_description, data, treatment, target, threshold, is_above
                          , statistic_functions):
    """
    prints the results of statistic functions on the target feature values of
    hours in which the feature_description fits to the category and the treatment feature
    is above of below the threshold, depends on the value of is_above
    :param feature_description: a string
    :param data: a dictionary, keys are strings and
    the values are lists of floats
    :param treatment: a string
    :param target: a string
    :param threshold: a float
    :param is_above: a boolean
    :param statistic_functions: a list of functions
    :return: none
    """
    WORD_TO_FEATURE = {"spring": ("season", 0), "summer": ("season", 1), "fall": ("season", 2),
                       "winter": ("season", 3), "holiday": ("is_holiday", 1), "weekday": ("is_holiday", 0)}
    categories = list(filter(lambda x: x in WORD_TO_FEATURE, feature_description.lower().split(" ")))
    population = [WORD_TO_FEATURE[x] for x in categories]
    new_data = data
    for feature in population:
        new_data = filter_by_feature(new_data, feature[0], [feature[1]])[0]
    z = zip(new_data[treatment], new_data[target])
    new_data = {target: [x[1] for x in list(filter(lambda x: (is_above ^ (x[0] <= threshold)), z))]}
    print_details(new_data, [target], statistic_functions)