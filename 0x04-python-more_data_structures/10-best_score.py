#!/usr/bin/python3
def best_score(a_dictionary):
    # if a_dictionary is None:
    #     return None
    # x = ""
    # for k1 in a_dictionary.keys():
    #     for k2 in a_dictionary.keys():
    #         if a_dictionary[k1] >= a_dictionary[k2]:
    #             x = k1
    # return x
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
