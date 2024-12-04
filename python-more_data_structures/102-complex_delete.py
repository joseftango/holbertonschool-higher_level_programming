def complex_delete(a_dictionary, value):
    if not value or value not in a_dictionary.values():
        return a_dictionary
    cp_dict = a_dictionary.copy()
    for k, v in cp_dict.items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
