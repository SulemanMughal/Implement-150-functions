def get_indices(input_list):
    indices = []
    for idx, value in enumerate(input_list):
        if isinstance(value, str):
            indices.append(idx)
    return indices