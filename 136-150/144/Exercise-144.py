import re
    
    
def find_phone_number(text):
    result = re.search(r'\d\d\d-\d\d\d-\d\d\d', text)
    return result.group()