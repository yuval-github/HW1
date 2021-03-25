import sys
import statistics
from data import load_data


def main(argv):
    """argv: main.py path_to_data important_features
    question1 : prints population_statistics about Summer, Holiday and All
    of the features hum, t1 and cnt
    question2 : prints population_statistics about Winter holiday and weekday,
    on the cnt feature, with a threshold of a 13.0, one time above the threshold
    and one time below it"""
    path = argv[1]
    features = argv[2]
    data = load_data(path, features)
    # -----------------question 1-----------------
    question1_statistics_functions = [statistics.sum, statistics.mean, statistics.median]
    print("Question 1")
    question1_categories = ["Summer", "Holiday", "All"]
    question1_features = ["hum", "t1", "cnt"]
    for category in question1_categories:
        print(category+":")
        for feature in question1_features:
            statistics.population_statistics(category, data, "cnt"
                                             , feature, -1, True, question1_statistics_functions)
    # -----------------question 2-----------------
    question2_statistics_functions = [statistics.mean, statistics.median]
    question2_categories = ["holiday", "weekday"]
    question2_threshold = 13.0
    question2_is_above = [False, True]
    print("\nQuestion 2")
    for is_above in question2_is_above:
        print("If t1" +("<="*(not is_above)+">"*is_above)+ "13.0, then:")
        for category in question2_categories:
            print("Winter " + category + " records:")
            statistics.population_statistics("Winter " + category, data, "t1", "cnt", question2_threshold,
                                             is_above, question2_statistics_functions)


if __name__ == '__main__':
    main(sys.argv)
