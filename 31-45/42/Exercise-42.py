def truncate(heading, length=30):
    if len(heading) <= length:
        return heading
    return heading[:length - 3] + '...'