def f(list1, list2):
    common_elements = list(set(list1) & set(list2))
    not_common_elements = list(set(list1) ^ set(list2))
    return common_elements, not_common_elements