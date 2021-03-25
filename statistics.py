from data import filter_by_feature,filter_by_threshold,print_details


def sum(values):
    """returns the sum of all numbers in values (a list)"""
    answer = 0
    for value in values:
        answer += value
    return answer


def mean(values):
    """returns the mean of all numbers in values (a list)"""
    return int(len(values) > 0) and sum(values) / len(values)


def median(values):
    """returns the median of all numbers in values (a list)"""
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n == 0: return 0
    return (sorted_values[n // 2 - (n%2 == 0)] + sorted_values[n // 2]) / 2


def decode_feature_description(feature_description):
    """
    returns a list of all features from feature_description (a string)
    word_to_feature - a dict, the keys are adjectives and the values
    are (category, value of this adjective in that category)
    """
    features = feature_description.split(" ")
    word_to_feature = {"spring": ("season", 0),"summer": ("season", 1),"fall": ("season", 2),
                       "winter": ("season", 3),"holiday": ("is_holiday", 1),"weekday": ("is_holiday", 0)}
    translated_features = []
    for feature in features:
        if feature.lower() in word_to_feature.keys():
            translated_features.append(word_to_feature[feature.lower()])
    return translated_features


def population_statistics(feature_description, data, treatment, target, threshold, is_above
                          , statistic_functions):
    """prints the results of statistic functions on the target feature values of
    hours in which the feature_description fits to the category and the treatment feature
    is above of below the threshold, depends on the value of is_above"""
    population = decode_feature_description(feature_description)
    new_data = data
    for feature in population:
        new_data = filter_by_feature(new_data, feature[0], [feature[1]])[0]
    new_data = filter_by_threshold(new_data, treatment, threshold, is_above)[0]
    print_details(new_data, [target], statistic_functions)
