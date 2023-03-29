def get_indices(input_list, item):
    indices = []
    for idx, value in enumerate(input_list):
        if value == item:
            indices.append(idx)
    return indices