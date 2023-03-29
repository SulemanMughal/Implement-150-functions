# Solution 1

def preprocess(stream):
    for chunk in stream[:]:
        if not chunk.endswith('.png'):
            stream.remove(chunk)
    return stream


# Solution 2
def preprocess(stream):
    return [chunk for chunk in stream if chunk.endswith('.png')]