def sort_dict_by_keys(d: dict) -> dict:
    myKeys = list(d.keys())
    myKeys.sort()
    sorted_dict = {i: d[i] for i in myKeys}
    return sorted_dict