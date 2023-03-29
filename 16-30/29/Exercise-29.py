def convert(text):
    pascal_case = text.replace('_', ' ').title().replace(' ', '')
    return pascal_case[0].lower() + pascal_case[1:]