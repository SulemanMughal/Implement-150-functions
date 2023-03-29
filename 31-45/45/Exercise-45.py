def get_headers():
    with open('app_store.csv', 'r') as file:
        headers = file.readline().strip().split(',')
        result = [header.replace(' ', '_').lower() for header in headers]
    return result