def f(dictionary_list, key):
    sorted_list = sorted(dictionary_list, key=lambda x: x[key])
    return sorted_list