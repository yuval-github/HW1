import pandas


def load_data(path, features):
    """returns a dictionary, the keys are features and the
    values are lists of numbers from the data in path that
    match the features"""
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")
    features.split(", ")
    all_features = data.keys()
    to_delete = []
    for feature in all_features:
        if feature not in features:
            to_delete.append(feature)
    for feature in to_delete:
        data.pop(feature)
    return data


def filter_by_feature(data, feature, values):
    """returns two dictionaries, data1 contains the hours in which
    the category feature value is from values and data2 is what ever
    is left in data"""
    data1 = {}
    data2 = {}
    for key in data.keys():
        data1[key] = []
        data2[key] = []
    for idx, val in enumerate(data[feature]):
        for key in data.keys():
            if val in values:
                data1[key].append(data[key][idx])
            else:
                data2[key].append(data[key][idx])
    return data1, data2


def filter_by_threshold(data, treatment, target, threshold, is_above):
    """returns a dictionary that contains the hours in which
        the value of feature is above or below the threshold , depends
        on the value of is_above"""
    z = zip(data[treatment], data[target])
    return {target: [x[1] for x in list(filter(lambda x: (is_above ^ (x[0] <= threshold)), z))]}


def print_details(data, features, statistic_functions):
    """prints the results of the functions in statistic_functions
    on the values of features in data"""
    for feature in data.keys():
        if feature in features:
            values = data[feature]
            answer = ""
            for func in statistic_functions:
                answer += ", " + str(func(values))
            print(feature + ": " + answer[2:])

