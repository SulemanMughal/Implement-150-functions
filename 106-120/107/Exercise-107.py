def get_slices(sequence, length):
    if length < 1:
        raise ValueError('The length cannot be less than 1.')
    if length > len(sequence):
        raise ValueError(
            'The length cannot be greater than sequence.'
        )
    return [
        sequence[i : i + length]
        for i in range(len(sequence) - length + 1)
    ]